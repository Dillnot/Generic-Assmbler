spec test;
prog: RRR | LEA ;
RRR: op@op , "," , reg@d ,",", reg@a,",", reg@b -> add(op,d,a,b);
op: "add" -> 0
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

LEA: "leaR1,50[R0]" -> mkLea1()
 | "leaR2,50[R0]" -> mkLea2()
 ;

reg: R , number@num -> return(num);
R: "r" | "R";
#Functions
add(op,d,a,b){
    MCI [
        op:w(16,0):(0,4),
         d:w(16,0):(5,4),
         a:w(16,0):(9,4),
         b:w(16,0):(13,4)
         ]
}
mkLea1(){
op = 0+0;
fixedValue = 15+0;
a = 1+0;
b = 0+0;
num = 50+0;
MCI [
    fixedValue:w(16,0):(0,4),
    op:w(16,0):(13,4),
    a:w(16,0):(5,4),
    num:w(16,1):(0,16),
    b:w(16,0):(9,4)
    ]
}


mkLea2(){
op = 0+0;
fixedValue = 15+0;
a = 2+0;
b = 0+0;
num = 50+0;
MCI [
    fixedValue:w(16,0):(0,4),
    op:w(16,0):(13,4),
    a:w(16,0):(5,4),
    num:w(16,1):(0,16),
    b:w(16,0):(9,4)
    ]
}
