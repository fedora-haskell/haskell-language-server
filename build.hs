#!/usr/bin/env stack
-- stack --resolver lts-23.28 script --package=fedora-releases --package=extra --package=simple-cmd --package=simple-cmd-args

import Control.Monad (forM_, unless, when)
import Data.Either (partitionEithers)
import Data.List ((\\))
import Data.Maybe (mapMaybe)
import Data.Tuple (swap)
import Data.Version.Extra
import Distribution.Fedora.Branch (Branch(..), eitherBranch, getActiveBranches,
                                   showBranch)
import SimpleCmd
import SimpleCmdArgs

main =
  simpleCmdArgs Nothing "hls builder" "hls copr builds" $
  run
  <$> switchWith 'n' "dryrun" "Show what would be done only"
  <*> switchWith 'l' "local" "Do a local build instead"
  <*> (map readArch <$> many (strOptionWith 'a' "arch" "ARCH" "chroot archtectures"))
  <*> (partitionBranches <$> many (strArg "BRANCH... GHCMAJOR..."))

-- https://haskell-language-server.readthedocs.io/en/latest/support/ghc-version-support.html
-- minimum listed GHC version: 9.4
-- 9.2 fails to build ghcide
defaultGHCs = [GHC, GHC9_12, GHC9_10, GHC9_8, GHC9_6, GHC9_4]
allArchs = [X86_64, AARCH64, PPC64LE]
defaultArchs = [X86_64, AARCH64]

run dryrun local reqarchs (reqbrs,reqghcs) =
  if local
  then do
    unless (null reqbrs) $
      error' "can't combine --local with branches"
    when (null reqghcs) $
      error' "specify at least one ghcver"
    -- FIXME doesn't work (branch interferes)
    runLocal dryrun reqghcs
  else runRemote dryrun reqarchs (reqbrs,reqghcs)

runRemote dryrun reqarchs (reqbrs,reqghcs) = do
  branches <-
    if null reqbrs
    then do
      allbrs <- getActiveBranches
      -- EPELMinor 10 0
      return $ allbrs \\ [EPEL 8, EPELNext 8, EPELNext 9]
    else return reqbrs
  let ghcs = if null reqghcs then defaultGHCs else reqghcs
      frpq = "/usr/bin/frpq"
  forM_ branches $ \br -> do
    defaultGhcVer <- readVersion <$> cmd frpq ["-q", showBranch br, "--qf=%{version}", "--latest-limit=1", "ghc"]
    forM_ (ghcs \\ ([GHC | br == EPEL 9] ++ [GHC9_10 | br == EPEL 9] ++ [GHC9_12 | br == EPEL 9])) $
      \ghc -> do
      putChar '\n'
      putStrLn $ "#" +-+ showBranch br +-+ showGHCPkg ghc
      version <- readVersion <$> cmd frpq ["-q", showBranch br, "--qf=%{version}", "--latest-limit=1", showGHCPkg ghc]
      if ghc /= GHC && version == defaultGhcVer
        then putStrLn $ "skipping" +-+ showGHCPkg ghc ++ '-' : showVersion version
        else do
        putStrLn $ showVersion version
        when (ghc /= GHC) $ do
          let latest = latestGHC ghc
          when (version /= latest) $
            error' $ showGHCPkg ghc ++ '-' : showVersion version +-+ "is not" +-+ showVersion latest
        switchGhcMajor ghc
        ghcmajor <- cmd "grep" ["%global ghc_major", specFile]
        --putStrLn ghcmajor
        -- FIXME check ghcmajor
        sed ["s/%global ghc_minor .*/%global ghc_minor " ++ showVersion version ++ "/"]
        let archs =
              if length reqarchs == 1
              then reqarchs
              else mapMaybe (maybeGHCArchs br ghc) $
                   if null reqarchs then defaultArchs else reqarchs
        -- 9.4 fails to link for aarch64 with ld.gold: skip unless explicit req
        unless (reqarchs == [AARCH64] && ghc == GHC9_4 && ghcs /= [GHC9_4]) $
          cmdLog_ "fbrnch" $ "copr" : ["-n" | dryrun] ++ ["--single", "haskell-language-server", showBranch br] ++ map archOpt archs
        where
          maybeGHCArchs :: Branch -> GHCPKG -> Arch -> Maybe Arch
          maybeGHCArchs (EPEL 9) GHC9_4 AARCH64 = Nothing
          maybeGHCArchs (EPEL 9) GHC9_6 AARCH64 = Nothing
          maybeGHCArchs _ _ arch = Just arch
--            if ghcs == [GHC9_4] && (length ghcs > 1 || then Nothing else Just AARCH64

runLocal dryrun reqghcs =
  forM_ reqghcs $ \ghc -> do
  putChar '\n'
  putStrLn $ "#" +-+ showGHCPkg ghc
  version <- readVersion <$> cmd "rpm" ["-q", "--qf=%{version}", showGHCPkg ghc]
  putStrLn $ showVersion version
  when (ghc /= GHC) $ do
    let latest = latestGHC ghc
    when (version /= latest) $
      error' $ showGHCPkg ghc ++ '-' : showVersion version +-+ "is not" +-+ showVersion latest
  switchGhcMajor ghc
  ghcmajor <- cmd "grep" ["%global ghc_major", specFile]
  --putStrLn ghcmajor
  -- FIXME check ghcmajor
  sed ["s/%global ghc_minor .*/%global ghc_minor " ++ showVersion version ++ "/"]
  when dryrun $ error' "--local does not support --dryrun"
  -- FIXME need to unset GHC_PACKAGE_PATH
  cmdLog_ "fbrnch" ["local"]

switchGhcMajor :: GHCPKG -> IO ()
switchGhcMajor GHC =
  sed ["s/^%global ghc_major .*/#%%global ghc_major 9.4/"]
switchGhcMajor ghc =
  sed ["s/#%%global ghc_major/%global ghc_major/",
       "s/\\(%global ghc_major \\).*/\\1" ++ showMajor ghc ++ "/"]

specFile = "haskell-language-server.spec"

sed :: [String] -> IO ()
sed edits =
  cmd_ "sed" $ ["-i"] ++ map ("--expression=" ++) edits ++ [specFile]

archOpt :: Arch -> String
archOpt arch = "--arch=" ++ showArch arch

-- (from fbrnch Branches) different to fedora-releases
partitionBranches :: [String] -> ([Branch],[GHCPKG])
partitionBranches args =
  fmap (map readGHCPkg) . swap . partitionEithers $ map eitherBranch args

-- ghcVersion :: Branch -> Version
-- ghcVersion (EPEL 9) = makeVersion [8,10,7]
-- ghcVersion (Fedora 38) = makeVersion [9,2,6]
-- ghcVersion (Fedora 39) = makeVersion [9,4,5]
-- ghcVersion (Fedora 40) = makeVersion [9,4,5]
-- ghcVersion (Fedora 41) = makeVersion [9,6,6]
-- ghcVersion Rawhide = makeVersion [9,6,6]

data GHCPKG = GHC | GHC9_12
            | GHC9_10 | GHC9_8 | GHC9_6 | GHC9_4 | GHC9_2 | GHC9_0
            | GHC8_10
  deriving Eq

latestGHC :: GHCPKG -> Version
latestGHC GHC9_12 = makeVersion [9,12,2]
latestGHC GHC9_10 = makeVersion [9,10,3]
latestGHC GHC9_8 = makeVersion [9,8,4]
latestGHC GHC9_6 = makeVersion [9,6,7]
latestGHC GHC9_4 = makeVersion [9,4,8]
latestGHC GHC9_2 = makeVersion [9,2,8]
latestGHC GHC9_0 = makeVersion [9,0,2]
latestGHC GHC8_10 = makeVersion [8,10,7]
latestGHC GHC = error' "latestGHC not valid for main ghc package"

readGHCPkg :: String -> GHCPKG
readGHCPkg "main" = GHC
readGHCPkg "" = GHC
readGHCPkg "ghc" = GHC
readGHCPkg ('g':'h':'c':ver) = readGHCPkg ver
readGHCPkg ver =
  case ver of
    "912" -> GHC9_12
    "9.12" -> GHC9_12
    "910" -> GHC9_10
    "9.10" -> GHC9_10
    "98" -> GHC9_8
    "9.8" -> GHC9_8
    "96" -> GHC9_6
    "9.6" -> GHC9_6
    "94" -> GHC9_4
    "9.4" -> GHC9_4
    "92" -> GHC9_2
    "9.2" -> GHC9_2
    "90" -> GHC9_0
    "9.0" -> GHC9_0
    "810" -> GHC8_10
    "8.10" -> GHC8_10
    _ -> error' $ "unknown GHCVER" +-+ ver

showGHCPkg GHC = "ghc"
showGHCPkg GHC9_12 = "ghc9.12"
showGHCPkg GHC9_10 = "ghc9.10"
showGHCPkg GHC9_8 = "ghc9.8"
showGHCPkg GHC9_6 = "ghc9.6"
showGHCPkg GHC9_4 = "ghc9.4"
showGHCPkg GHC9_2 = "ghc9.2"
showGHCPkg GHC9_0 = "ghc9.0"
showGHCPkg GHC8_10 = "ghc8.10"

showMajor GHC = ""
showMajor GHC9_12 = "9.12"
showMajor GHC9_10 = "9.10"
showMajor GHC9_8 = "9.8"
showMajor GHC9_6 = "9.6"
showMajor GHC9_4 = "9.4"
showMajor GHC9_2 = "9.2"
showMajor GHC9_0 = "9.0"
showMajor GHC8_10 = "8.10"

data Arch = X86_64 | AARCH64 | PPC64LE
  deriving Eq

readArch :: String -> Arch
readArch "x86_64" = X86_64
readArch "aarch64" = AARCH64
readArch "ppc64le" = PPC64LE
readArch a = error' $ "unknown arch:" +-+ a

showArch :: Arch -> String
showArch X86_64 = "x86_64"
showArch AARCH64 = "aarch64"
showArch PPC64LE = "ppc64le"
