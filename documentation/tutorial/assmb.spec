spec assmb;
prog: f1;

f1: op@op , reg@d , reg@a , reg@b -> mkf1(op,d,a,b);
op: "add" -> 0
  | "sub" -> 1
  | "mul" -> 2
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

F2: opX@op ,  reg@d ,  disp@dis , '[' , reg@a , ']' -> mkf2(op,d,dis,a);


reg: R , number@num -> return(num);
R: "r" | "R";
#Functions
mkf1(op,d,a,b){
    MCI [
        op:w(16,0):(0,4),
         d:w(16,0):(5,4),
         a:w(16,0):(9,4),
         b:w(16,0):(13,4)
         ]
}
