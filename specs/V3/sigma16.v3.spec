spec sigma16;
prog: line;
line: RRR | RRX;
RRR: opR@op , "," , reg@d , "," , reg@a , "," , reg@b -> mkRRR(op,d,a,b);
opR: "add" -> 0
  | "sub" -> 1
  | "mul" -> 2
  | "div" -> 3
  | "cmplt" -> 4
  | "cmpeq" -> 5
  | "cmpgt" -> 6
  | "inv" -> 7
  | "and" -> 8
  | "or" -> 9
  | "xor" -> 10
  | "shiftl" -> 11
  | "shiftr" -> 12
  | "trap" -> 13
  ;

RRX: opX@op , "," , reg@d , "," , number@dis , "[" , reg@a , "]" -> mkRRX(op,d,dis,a);
opX: "lea" ->  0
  | "load" ->  1
  | "store" ->  2
  | "jump" ->  3
  | "jumpf" ->  4
  | "jumpt" ->  5
  | "jal" ->  6
  ;

reg: "R", number@num -> return(num);

#Functions
mkRRR(op,d,a,b){
MCI [
    op:w(16,0):(0,4),
     d:w(16,0):(5,4),
     a:w(16,0):(9,4),
     b:w(16,0):(13,4)
     ]
}

mkRRX(op, d, dis, a){
    fixedValue = 15+0;
    MCI [
        fixedValue:w(16,0):(0,4),
        op:w(16,0):(13,4),
        d:w(16,0):(5,4),
        dis:w(16,1):(0,16),
        a:w(16,0):(9,4)
    ]
}
