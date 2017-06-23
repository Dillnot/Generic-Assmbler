data in = label cmd
data cmd = RRR | RRX
data RRR = opr d a b
data RRX = opx d "," dis "[" b "]"
data dis = labal | int
data label= string


data opr = "add" |"sub" |"mul" |"div" |"cmplt" |"cmpeq" |"cmpgt" |"inv" |"and"| "or" |"xor" |"shiftl" |"shiftr" |"trap"
data d = reg
data a = reg
data c = reg
data reg = "R" num
