# A tutorial on how to write a Specification file for the Generic Assembler

## Introduction
The Specification files used by the GAG is based on extended backus-naur form to describe the syntax
of the assemble language with a few bespoke extensions to allow the description of the object code that should be generated
whenever the syntax has been matched. {? This means that the grammar is now not context free}

## Boilerplate
All of my grammar files must start with

`spec Name;` where `name` is the name of the spec
{? there must be a rule called prog that is the entry point to the program}

## Syntax
a Specification is made up of many Rules and functions that must all be created using a unique name

### Rules
are defined by
`Name: Rule {? -> (functionCall | VALUE)}`
where {?} is optional so a rule to match the text add and return 0 is:
`ADD: ("ADD" | "add") -> 0; `

Also since rules are can have recusing they can be called inside each other so using the previse 'ADD' rule a more complicated rule could be:
`AddOrNot: ADD | ("not");`

Notice that the value return from the 'ADD' is ignored if this result had to be used it can be captured using the `@` symbol after a call to a rule with a rule or any match with a **Call?**, with unique name following so as it can be referenced in function calls within the rule example
`AddOrNot2: (ADD@result | ("not")) -> doSomething(result);`
notice that due to the logical **_OR_** in the AddOrNot2 result could not be filed as the ADD rule may not be used in the match, when this occurs a non value Nothing will be used and may cause some errors if your function's do not handle this case correctly.
Also no1tice that this is the first example of a function call I have shown

### Functions
Functions are defined using standard syntax that should be familiar to anyone that has used any high level language
`Name(parameters){ body }`
where name is a unique function names and parameters is the values that are passed into the function, the body contains the logic of what to do.
the syntax allowed in a function is very simple
#### function Syntax
| Symbol | Meaning |
|--------|---------|
| :=     | assessment|
| +-*\\  | arithmetic operators|


#### Predefined Functions
