module ParseSpec where
import Text.Parsec
import DataType

parseSpec :: String -> Either ParseError Spec
parseSpec text = parse start "(unknown)" text

start::Parsec String u Spec
start = do
    string "spec"
    name <- many alphaNum
    char ';'
    listOfRules <- manyTill rule $ string "#Functions"
    listOfFunc <- many getFunc
    return $ Spec name listOfRules listOfFunc

rule :: Parsec String u Rule
rule = do
    name <- many alphaNum
    char ':'
    inner <- sepBy inRule (char '|')
    call <- getcall
    char ';'
    return $ Outer name inner call

inRule :: Parsec String u Rule
inRule = do
    value <- sepBy getValue (char ',')
    call <- getcall
    return $ Inner value call

getValue :: Parsec String u Value
getValue = prim <|> rulec

prim :: Parsec String u Value
prim = do
    usedQ <- oneOf "\"\'"
    value <- manyTill anyChar (char usedQ)
    return $ Prim value

rulec :: Parsec String u Value
rulec = try (withReturn) <|> withoutReturn

withoutReturn :: Parsec String u Value
withoutReturn = do
    value <- many alphaNum
    return $ Rcall value

withReturn :: Parsec String u Value
withReturn = do
    value <- many alphaNum
    char '@'
    var <- many alphaNum
    return $ Rcallr value var

getcall :: Parsec String u Call
getcall = (try returnFunc) <|> returnVa <|> do return NOP

returnVa :: Parsec String u Call
returnVa = do
    string "->"
    va <- many alphaNum
    return $ Value va

returnFunc :: Parsec String u Call
returnFunc = do
    string "->"
    name <- manyTill alphaNum (char '(')
    vars <- sepBy (many alphaNum) (char ',')
    char ')'
    return $ Func name vars

getFunc :: Parsec String u Function
getFunc = do
    name <- manyTill alphaNum (char '(')
    vars <- sepBy (many alphaNum) (char ',')
    char ')'
    char '{'
    statments <- manyTill getstatment (char '}')
    return $ Fdef name vars statments

getstatment :: Parsec String u Statement
getstatment = (try getSum) <|> (try getMCInst) <|> getFuncCall

getSum :: Parsec String u Statement
getSum = do
    result <- many alphaNum
    char '='
    varOrnum <- many alphaNum
    process <- oneOf "+-/*"
    varOrnum2 <- many alphaNum
    char ';'
    return $ S result process (varOrnum, varOrnum2)

getMCInst :: Parsec String u Statement
getMCInst = do
    string "MCI["
    wordSlices <-sepBy getWordSlice (char ',')
    char ']'
    return $ MCI wordSlices

getWordSlice :: Parsec String u WordSlice
getWordSlice = do
    numOrVar <- manyTill alphaNum (char ':')
    string "w("
    wordSize <- manyTill alphaNum (char ',')
    word <- manyTill alphaNum (string "):(")
    startPoint <- manyTill alphaNum (char ',')
    offset <- manyTill alphaNum (char ')')
    return $ WS numOrVar (L wordSize word startPoint offset)

getFuncCall :: Parsec String u Statement
getFuncCall = do
    result <- many alphaNum
    char '='
    name <- manyTill alphaNum (char '(')
    vars <- sepBy (many alphaNum) (char ',')
    char ')'
    char ';'
    return $ FC result name vars
