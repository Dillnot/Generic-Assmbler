import ParseSpec
import ParseProgram
import DataType
import CreateBS
import System.Environment
import Data.Either
import Text.Read (readMaybe)
import Data.Maybe

main = do
     [specFilePath, programFilePath] <- getArgs
     specFile <- readFile specFilePath
     programFile <- readFile programFilePath
     let spec = head $ rights $  [parseSpec (filter whiteSpaceFilter specFile)]
     --print spec
     let program = parseProgram spec (filter whiteSpaceFilter programFile)
     let allInst = head $ rights $ [program]
     let inst = map fromJust (filter noNothings (map readtest allInst))
     let bin = createBS inst
     print bin
     --BL.putStr bs
-- later use wheres to make nicer error megs



readtest :: String -> Maybe Statement
readtest = readMaybe

noNothings :: Maybe a -> Bool
noNothings Nothing = False
noNothings _ = True

whiteSpaceFilter :: Char -> Bool
whiteSpaceFilter ' ' = False
whiteSpaceFilter '\n' = False
whiteSpaceFilter _ = True
