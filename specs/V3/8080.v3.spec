grammer 8080;
prog: inst;
inst: CBI | SRI | NOP | DTI | RMTAI;



CBI: "STC" -> mkSTC()
    | "CMC" ->  mkCMC()
    ;

SRI: INR
  | DCR
  | "CMA" -> mkCMA()
  ;

INR: "INR" , reg@r  -> mkINR(r) ;
DCR: "DCR", reg@r  -> mkDCR(r);

NOP: "NOP" -> mkNOP();

DTI: MOV;
MOV: "mov", reg@r1 ,",", reg@r2 -> mkMOV(r1,r2) ;


RMTAI: RMTAI_op@op ,reg@r -> mkRMTAI(op,r);
RMTAI_op: "ADD" -> 0
        | "ADC" -> 1
        | "SUB" -> 2
        | "SBB" -> 3
        | "ANA" -> 4
        | "XRA" -> 5
        | "ORA" -> 6
        | "CMP" -> 7
        ;

reg: "B" -> 0
  | "C" -> 1
  | "D" -> 2
  | "E" -> 3
  | "H" -> 4
  | "L" -> 5
  | "M" -> 6
  | "A" -> 7
  ;

#Functions
mkNOP(){
    v=0+0;
    MCI [ v:w(8,0):(0,8) ]
}
mkSTC(){
    v=55+0;
    MCI [v:w(8,0):(0,8)]
}

mkCMC(){
    v=63+0;
    MCI [v:w(8,0):(0,8)]
}

mkCMA(){
    v=47+0;
    MCI [v:w(8,0):(0,8)]
}

mkINR(r){
    z = 0+0;
    v = 4+0;
    MCI [
        r:w(8,0):(2,3),
        z:w(8,0):(0,2),
        v:w(8,0):(5,3)
    ]
}
mkDCR(r){
z = 0+0;
v = 5+0;
MCI [
    r:w(8,0):(2,3),
    z:w(8,0):(0,2),
    v:w(8,0):(5,3)
]
}

mkMOV(r1,r2){
    v = 1+0;
    mci[
        v:w(8,0):(0,2),
        r1:w(8,0):(2,3),
        r2:w(8,0):(5,3)
    ]
}
mkRMTAI(op,r){
    v=2+0;
    MCI [
        op:w(8,0):(2,3),
        r:w(8,0):(5,3),
        v:w(8,0):(0,2)
    ]
}
