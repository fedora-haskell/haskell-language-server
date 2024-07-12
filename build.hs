#!/usr/bin/env stack
-- stack --resolver lts-21.25 script

import Control.Monad (forM_, when)
import Data.Either (partitionEithers)
import Data.List ((\\))
import Data.Maybe (mapMaybe)
import Data.Tuple (swap)
import Data.Version.Extra
import Distribution.Fedora.Branch (Branch(..), eitherBranch, getFedoraBranches)
import SimpleCmd
import SimpleCmdArgs

main =
  simpleCmdArgs Nothing "hls builder" "hls copr builds" $
  run
  <$> switchWith 'n' "dryrun" "Show what would be done only"
  <*> (map readArch <$> many (strOptionWith 'a' "arch" "ARCH" "chroot archtectures"))
  <*> (partitionBranches <$> many (strArg "BRANCH... GHCMAJOR..."))

defaultGHCs = [GHC, GHC9_8, GHC9_6, GHC9_4, GHC9_2]
allArchs = [X86_64, AARCH64, PPC64LE]

-- FIXME default branches to: rawhide f40 f39 f38 epel9
-- FIXME default versions to: main 9.8 9.6 9.4 9.2 (for latest hls)
run dryrun archs (brs,ghcs) = do
  branches <-
    if null brs
    then do
      allbrs <- getFedoraBranches
      return $ allbrs \\ [EPEL 8, EPELNext 8, EPELNext 9]
    else return brs
  forM_ branches $ \br ->
    forM_ (if null ghcs then defaultGHCs else ghcs) $ \ghc -> do
    putChar '\n'
    putStrLn $ "=" +-+ show br +-+ showGHCPkg ghc
    version <- cmd "fdrq" ["-q", (show br), "--qf=%{version}", "--latest-limit=1", showGHCPkg ghc]
    if null version
      then error' $ showGHCPkg ghc +-+ "not found" +-+ "for" +-+ show br
      else do
      putStrLn version
      let ghcversion = readVersion version
      when (ghc /= GHC) $ do
        let latest = latestGHC ghc
        when (ghcversion /= latest) $
          error' $ showGHCPkg ghc ++ '-' : showVersion ghcversion +-+ "is not" +-+ showVersion latest
      switchGhcMajor ghc
      ghcmajor <- cmd "grep" ["%global ghc_major", specFile]
      putStrLn ghcmajor
      -- FIXME check ghcmajor
      sed ["s/%global ghc_minor .*/%global ghc_minor " ++ version ++ "/"]
      cmdLog_ "fbrnch" $ "copr" : ["-n" | dryrun] ++ ["--single", "haskell-language-server", show br] ++ map archOpt (mapMaybe (maybeGHCArchs ghc) $ if null archs then [X86_64,AARCH64] else archs)

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

-- (from fbrnch Branches)
partitionBranches :: [String] -> ([Branch],[GHCPKG])
partitionBranches args =
  fmap (map readGHCPkg) . swap . partitionEithers $ map eitherBranch args

maybeGHCArchs :: GHCPKG -> Arch -> Maybe Arch
maybeGHCArchs ghc AARCH64 =
  if ghc `elem` [GHC9_4,GHC9_6] then Nothing else Just AARCH64
maybeGHCArchs _ arch = Just arch

ghcVersion :: Branch -> Version
ghcVersion (EPEL 9) = makeVersion [8,10,7]
ghcVersion (Fedora 38) = makeVersion [9,2,6]
ghcVersion (Fedora 39) = makeVersion [9,4,5]
ghcVersion (Fedora 40) = makeVersion [9,4,5]
ghcVersion Rawhide = makeVersion [9,4,5]

latestGHC :: GHCPKG -> Version
latestGHC GHC9_8 = makeVersion [9,8,2]
latestGHC GHC9_6 = makeVersion [9,6,6]
latestGHC GHC9_4 = makeVersion [9,4,8]
latestGHC GHC9_2 = makeVersion [9,2,8]
latestGHC GHC9_0 = makeVersion [9,0,2]
latestGHC GHC8_10 = makeVersion [8,10,7]
latestGHC GHC = error' "latestGHC not valid for main ghc package"

data GHCPKG = GHC | GHC9_8 | GHC9_6 | GHC9_4 | GHC9_2 | GHC9_0 | GHC8_10
  deriving Eq

readGHCPkg :: String -> GHCPKG
readGHCPkg "main" = GHC
readGHCPkg "" = GHC
readGHCPkg "ghc" = GHC
readGHCPkg ('g':'h':'c':ver) = readGHCPkg ver
readGHCPkg ver =
  case ver of
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
showGHCPkg GHC9_8 = "ghc9.8"
showGHCPkg GHC9_6 = "ghc9.6"
showGHCPkg GHC9_4 = "ghc9.4"
showGHCPkg GHC9_2 = "ghc9.2"
showGHCPkg GHC9_0 = "ghc9.0"
showGHCPkg GHC8_10 = "ghc8.10"

showMajor GHC = ""
showMajor GHC9_8 = "9.8"
showMajor GHC9_6 = "9.6"
showMajor GHC9_4 = "9.4"
showMajor GHC9_2 = "9.2"
showMajor GHC9_0 = "9.0"
showMajor GHC8_10 = "8.10"

data Arch = X86_64 | AARCH64 | PPC64LE

readArch :: String -> Arch
readArch "x86_64" = X86_64
readArch "aarch64" = AARCH64
readArch "ppc64le" = PPC64LE
readArch a = error' $ "unknown arch:" +-+ a

showArch :: Arch -> String
showArch X86_64 = "x86_64"
showArch AARCH64 = "aarch64"
showArch PPC64LE = "ppc64le"
