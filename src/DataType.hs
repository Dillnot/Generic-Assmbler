module DataType where

data Spec = Spec {specName::String, rules::[Rule], functions::[Function]} deriving (Show)

data Rule = Inner {values::[Value], innerCall::Call} | Outer {ruleName::String ,innerRules::[Rule], outerCall::Call} deriving (Show)
data Value = Prim {value::String} | Rcallr {ruleCallWR::String , var::String} | Rcall {ruleCall::String} deriving (Show)
data Call = NOP | Func{ funcCallName::String, funcCallvars::[String]} | Value {callValue::String} deriving (Show)

data Function = Fdef {funcName::String ,funcVars::[String] ,funcStatments::[Statement]} deriving (Show)
data Statement = S {result::String, process::Char, varOrNums::(String,String)} | FC {result::String, callName::String, fcVars::[String]} | MCI [WordSlice] deriving (Show,Read)
data WordSlice = WS {numOrVar::String, location::Location} deriving (Show,Read)
data Location = L {wordSize::String , word::String, startPoint::String, offset::String} deriving (Show,Read)
