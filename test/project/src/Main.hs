-- SPDX-License-Identifier: BSD-3-Clause

module Main (main) where

import qualified MyLib (someFunc)

main :: IO ()
main = do
  putStrLn "Hello, Haskell!"
  MyLib.someFunc
