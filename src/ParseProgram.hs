module ParseProgram where
import Text.Parsec.Combinator
import Text.Parsec
import Text.Parsec.Prim
import Text.Read (readMaybe)
import Data.Maybe
import Data.List
import DataType
import Data.String

-- data CallValue = V String | bubble up data type

parseProgram :: Spec -> String -> Either ParseError [String]
parseProgram spec text = parse (startP spec) "(unknown)" text

startP ::Spec -> Parsec String u [String]
startP spec = do
    ret <- many $ head $ map (parseRule spec) (rules spec)
    return ret

parseRule ::Spec -> Rule -> Parsec String u String
parseRule spec rule =  do
    ret <- choice $ map (parseInnerRule spec) (innerRules rule)
    return ret

parseInnerRule :: Spec -> Rule -> Parsec String u String
parseInnerRule spec rule = try $ do
    ret <- sequence $ map (parseValue spec) (values rule)
    let value =  doCall spec (innerCall rule) (filter retFilter ret)
    return value
    where
        retFilter ("","") = False
        retFilter _ = True


parseValue :: Spec -> Value -> Parsec String u (String,String)
parseValue spec (Prim primValue) = do
    string primValue
    return ("","")

parseValue spec (Rcall ruleName) = do
    ret <- parseRule spec $ head $ filter (testRule ruleName) (rules spec)
    return ("",ret)

parseValue spec (Rcallr "number" var) = do
    num <- choice $ [(many hexDigit), (many digit)] -- still allow hex here but can'y use it in functions
    return (var,num)

parseValue spec (Rcallr ruleName var) = do
    ret <- parseRule spec $ head $ filter (testRule ruleName) (rules spec)
    return (var,ret)


doCall :: Spec -> Call -> [(String,String)] -> String
doCall spec (Func "return" varsNeeded) varsGot = snd $ head varsGot --TODO needs to be change to return the right var
doCall spec (Func name varsNeeded) varsGot = doFunction spec ( head (filter (testFunc name) (functions spec))) varsGot -- TODO need to add some var check here
doCall _ (NOP) [] = ""
doCall _ (NOP) (x:xs) = snd x --needed for outercalls to work since its a bit buged right now
doCall _ (Value v) _ = v

doFunction :: Spec -> Function ->[(String,String)] ->  String
doFunction spec func varsGot = snd $ last $ foldl (exeStatment spec) varsGot (funcStatments func)
--doFunction spec func vars = "I Work"

exeStatment :: Spec -> [(String,String)] -> Statement -> [(String,String)]
exeStatment spec vars (S result process (var1,var2)) = vars ++ [(result, (value))]
    where
        value = (doMath (readMaybeInt var1) (readMaybeInt var2) (func) (var1,var2) vars)
        func
            | process == '+' = (+)
            | process == '-' = (-)
            | process == '/' = (div)
            | process == '*' = (*)

-- function case
exeStatment spec vars (FC result function varsNeeded) = vars ++ [( result, value)]
    where
        value = (doCall spec (Func function varsNeeded) (makeCorrectVars varsNeeded vars varNames))
        varNames = funcVars $ head (filter (testFunc function) (functions spec))

exeStatment spec vars (MCI wordSlices) = [("hi", show value)]
    where
         value = MCI $ map (makeCorrectWS vars) wordSlices

makeCorrectWS :: [(String, String)] -> WordSlice -> WordSlice
makeCorrectWS vars (WS var loc) = WS value loc
    where
        value = getV $ readMaybeInt var
        getV Nothing = show $ getVar vars var
        getV val = show $ fromJust val

makeCorrectVars :: [String] ->  [(String,String)] -> [String] ->  [(String,String)]
makeCorrectVars varsNeeded vars varName = zip varName $  snd $ unzip $ filter func vars
    where
        func var = elem (fst var) varsNeeded


doMath :: Show a => Maybe Int -> Maybe Int -> (Int -> Int -> a) -> (String, String) -> [(String, String)] -> String
doMath Nothing Nothing func (var1,var2) vars = show $ func (getVar vars var1) (getVar vars var2)
doMath (Just x) Nothing func (var1,var2) vars = show $ func x (getVar vars var2)
doMath Nothing (Just y) func (var1,var2) vars = show $ func (getVar vars var1) y
doMath (Just x) (Just y) func (var1,var2) vars = show $ func x y

getVar :: [(String,String)] -> String -> Int
getVar vars var = read $ snd $ head $ filter filt vars
    where
        filt cVar = (fst cVar) == var


-- needed to add a type to what read maby returns
readMaybeInt :: String -> Maybe Int
readMaybeInt = readMaybe

-- filter functions i use in more than one place
testFunc:: String -> Function -> Bool
testFunc functName funct = (funcName funct) == functName

testRule :: String -> Rule -> Bool
testRule ruleWeNeed rule = (ruleName rule) == ruleWeNeed
