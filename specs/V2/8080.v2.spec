grammer 8080;
prog: line*;
line = label? inst

inst: CBI | SRI | NOP | DTI | RMTAI
    ;



CBI: "STC" -> h(37):w(8,0)->(0,8)
    | "CMC" ->  h(3f):w(8,0)->(0,8)
    ;

SRI: INR
  | DCR
  | "CMA" ->h(2F):w(8,0)->(0,8)
  ;

INR: "INR" reg:w(8,0):(2,3)  -> h(0):w(8,0):(0,2) -> h(4):w(8,0):(5,3);
DCR: "DCR" reg:w(8,0):(2,3)  -> h(0):w(8,0):(0,2) -> h(5):w(8,0):(5,3);

NOP: "NOP" -> h(0):w(8,0)->(0,8);

DTI: MOV | STAX | LDAX ;
MOV: "mov" reg:w(8,0):(2,3) "," reg:w(8,0):(5,3) -> h(1)->(8,0):(0,2)
STAX:?
LDAX:?

RMTAI: RMTAI_op reg:w(8,0):(5,3) -> h(2)->(8,0):(0,2);
RMTAI_op: "ADD" -> h(0):w(8,0):(2,3)
        | "ADC" -> h(1):w(8,0):(2,3)
        | "SUB" -> h(2):w(8,0):(2,3)
        | "SBB" -> h(3):w(8,0):(2,3)
        | "ANA" -> h(4):w(8,0):(2,3)
        | "XRA" -> h(5):w(8,0):(2,3)
        | "ORA" -> h(6):w(8,0):(2,3)
        | "CMP" -> h(7):w(8,0):(2,3)
        ;

reg: "B" -> h(0)
  | "C" -> h(1)
  | "D" -> h(2)
  | "E" -> h(3)
  | "H" -> h(4)
  | "L" -> h(5)
  | "M" -> h(6)
  | "A" -> h(7)
  ;
