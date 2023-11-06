{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -Wno-missing-safe-haskell-mode #-}
module Paths_solve (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,2,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/alex/.cabal/bin"
libdir     = "/home/alex/.cabal/lib/x86_64-linux-ghc-9.0.2/solve-0.2.0.0-inplace-solve"
dynlibdir  = "/home/alex/.cabal/lib/x86_64-linux-ghc-9.0.2"
datadir    = "/home/alex/.cabal/share/x86_64-linux-ghc-9.0.2/solve-0.2.0.0"
libexecdir = "/home/alex/.cabal/libexec/x86_64-linux-ghc-9.0.2/solve-0.2.0.0"
sysconfdir = "/home/alex/.cabal/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "solve_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "solve_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "solve_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "solve_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "solve_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "solve_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
