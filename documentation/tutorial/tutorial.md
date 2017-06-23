# An introduction to the use of the Generic Assembler

# Outline
+ understanding of how to run and use of the program
+ the creation of a simple specification file to gain understanding of its syntax
+ multiple increases to the complexity of the example to show off a real use case
    + should be able to assemble a simple program (if I use some 8080 or arm may be able to run it in an emulator)

# Using the program

the way the program work is similar on all OS

`GenericAssemblerGenerator PathToSpec PathToProgram`

assuming you are on the command line in the folder supplied the command on Linux is

`./linux/GenericAssemblerGenerator PathToSpec PathToProgram`

on windows it is

`windows/GenericAssemblerGenerator.exe PathToSpec PathToProgram`

# Part 1 - Rules

In this part we will take a simple spec, run though its syntax and then you will expand it.

The File `start.spec` is in the provided folder.
This spec describes a syntax that takes in a number then outputs its 8 bit binary representation.

Lets start at line 1
`spec start;`
this line is just boiler plate that is needed at the start. `spec` is a keyword and `start` is the name giving it can be any alphanumeric string. `;` is used to end the line.

The next line is more interesting

`prog: number@num -> output(num);`

`prog` is the name of the rule defined on this line and can be any alphanumeric string ; the first rule in a spec is more important as it will be applied to the supplied program as many times as possible, the name ends after a `:` and what comes after is the rule.

`number@num` is the next section to explain `number` is a call to a rule, a rule call is never in quotes. The number rule is pre-defined by the program and matches a number and returns its value. The `@` symbol is used to capture the return value of a rule call, and in this case the value returned is placed in `num` so that it can be used later.

`-> output(num);` is the side effect of this rule call. Not all rules must have a side effect but most do. In this case, the value captured in `num` is being passed to the output function defined lower down in the file. Try not to worry about functions just now, they will be explained later.

## Task 1 - simple rule

For this task we will change our spec so that `hi` will have to appear before our numbers. This can be done in a few ways, but we will start with the simplest.
If you place `hi` in quotes before the rule this means match this string. Now add a coma so your rule should look like this:
`prog: 'hi', number@num -> output(num);`
the coma means to append parts together so the must happen in order.
Try this new spec out and try changing the word.

## Task 2 - sub rules

Lets expand on this so that the `hi` can be in higher or lower case.
We will start on this task by creating a new rule like so:
`HI: ;` we can add a matcher for a lower case hi so the rules should now look like `HI: 'hi';`. a new piece of syntax an OR using `|` symbol so if we take our HI rule and check for capital hi like so `HI: 'hi' | 'HI';`.
Now lets change our prog rule to use our new rule `prog: HI , number@num -> output(num);`. since the HI is rule name and not in quotes it will call the rule. Run a program thought with the new spec

### Extension
Change the spec so that any combinations of capital and lower case letters can be used in the hi example `hI`.

# Part 2 - Spec Functions and rule returns

The next part we will describes how functions and side effects work. Lets start by describing the next part of `start.spec`.

`#Functions` is boiler plate to start the function implementation.

`output(num){` this is a function declaration for a function called output that takes a input variable called num.

The next line
`MCI [ num:w(8,0):(0,8) ]` is a build in command that can be used in functions `MCI` stands for machine code instructions. This command makes the function return the value of `num` in the zero word of size 8 `w(8,0)` starting at the zero's bit with a displacement of size 8 `:(0,8)`. Lets play with this function to change its behaver.

Lets add a new line
`out = num * 2;` and change num in the MCI command to the new VAR out so it should now look like `MCI [ out:w(8,0):(0,8) ]`. If you try running the program now it should output double the number inputted.

## Task 3 - side effects

Lets change our hi rule slightly so that a value is returned right. It should look like this `HI: 'hi' | 'HI';` lets change this so that a value of two is return every time this rule is matched. All you have to do is add a side effect with `->`. as it is now the rule would be have to be change to   `HI: 'hi' -> 2 | 'HI' -> 2;` since each choice using `|` has separate side effects but this can be simplified using a sub rule like so

`HI:HiChoices -> 2;`

`HiChoices: 'hi' | 'HI' | 'Hi' | 'hI';`

Now we need to capture the value for use change the prog rule to
`prog: HI@h , number@num -> output(num,h);` the value is now captured in a variable called h and sent to output. If you tried to run it now it would cause problems as output dose not expect two values,so we will now change the output function to allow two variables in so output will now look like this `output(num, h){
    out = num * h;
    MCI [
        num:w(8,0):(0.8)
    ]
}`

## Extension - putting it all together
This is an optional extension that is not guided. It is to make a calculator syntax that takes in the string names of single digit numbers , zero one ete, and a mathematical operator, + - * / , and output the result. a valid input might be `one*one` which would output `00000010`

## Extension - simple assembler
### Part 1
There is a second file in the folder provided called `assmb.spec` that describes a incomplete simple assemble language. In this part you will add a new instruction to existing format. There is a rule called `f1` you will finish off the rule by adding a `div` operation that has a op value of 3

### Part 2
For the second part you will implement format 2 in the `assmb.spec`.As  you can see MCI can have multiple values in the one output.
you will create the opx rule that takes `lea` and outputs a zero.
you will also have to create the displacement rule which would be almost the same as the reg rule.
The Function MkF2 will create a MCI where

`15->w(16,0):( 0, 4)`

`op->w(16,0):(13,4)`

`d->w(16,0):(5,4)`

`dis->w(16,1):(0,16)`

`a-> w(16,0):(9,4)`

you should now be able to run and test the spec

## Conclusion
hopefully you can see how this program can be useful for the development of assembly language and I hope you will fill out my evaluation survey
