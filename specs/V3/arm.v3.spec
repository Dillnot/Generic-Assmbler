grammer ARM32;
prog: line;
line = Data_processing;

Data_processing:  DP_one | DP_two ;

DP_one: DP_one_op@op cond@con RD@RD shift_op@shift -> mkDP_ONE(op,cond,RD,shift);
DP_one_op: "MOV" -> 13
        | "MVN" -> 15
        ;

DP_two: DP_two_op cond RD RN shift_OP -> mkDP_TWO(op,con,rd,rn,shift);
DP_two_op: "AND" -> 0
        | "EOR" -> 1
        | "SUB" -> 2
        | "RSB" -> 3
        | "ADD" -> 4
        | "ADC" -> 5
        | "SBC" -> 6
        | "RSC" -> 7
        | "TST" -> 8
        | "TEQ" -> 9
        | "CMP" -> 10
        | "CMN" -> 11
        | "ORR" -> 12
        | "BIC" -> 14
        ;

shift_op: RM@r - > return(r);
        | Log_shift_li@li -> return(li)
        | Log_shift_lr@lr -> return(lr)
        | Log_shift_ri@ri -> return(ri)
        | Log_shift_rr@rr -> return(rr)
        ;

Log_shift_li: RM@RM , "LSL #" number@num -> vShiftLI(RM,num);
Log_shift_lr: RM@rm , "LSL" RS@rs -> vShiftlr(rm,rs);

Log_shift_ri: RM , "LSR #" number@num ->vShiftRI(RM,num);
Log_shift_rr: RM@rm , "LSR" RS@rs - > vShiftRR(rm,rs);


cond:"" -> 14
    |"{", code@c, "}" -> return(c)
    ;

code: "EQ" -> 0
    | "NE" -> 1
    | "CS" -> 2
    | "CC" -> 3
    | "MI" -> 4
    | "PL" -> 5
    | "VS" -> 6
    | "VC" -> 7
    | "HI" -> 8
    | "LS" -> 9
    | "GE" -> 10
    | "LT" -> 11
    | "GT" -> 12
    | "LE" -> 13
    ;

RM: reg@r -> return(r)
RD: reg@r -> return(r)
RN: reg@r -> return(r)
RS: reg@r -> return(r)
reg:'R', number@num -> return(num);


#Functions
mkDP_ONE(op,cond,RD,shift){
    v=0+0;
    MCI [
        v:w(32,0):(4,2),
        op:w(32,0):(7,4),
        cond:w(32,0):(0,4),
        RD:w(32,0):(16,4),
        shift:w(32,0):(20,12)
    ]
}

mkDP_TWO(op,con,rd,rn,shift){
    v=0+0;
    MCI [
        v:w(32,0):(4,2),
        op:w(32,0):(7,4),
        cond:w(32,0):(0,4),
        rn:w(32,0):(12,4),
        RD:w(32,0):(16,4),
        shift:w(32,0):(20,12)
    ]
}

vShiftLI(RM,num){
    op = 0+0;
    movRm = 2*8;
    newRm = rm+movRm;
    movOP = 2*5;
    newOp = op*movop;
    temp = newOP+newRM;
    return = num+ temp;
}

vShiftRI(RM,num){
    op = 2+0;
    movRm = 2*8;
    newRm = rm+movRm;
    movOP = 2*5;
    newOp = op*movop;
    temp = newOP+newRM;
    return = num+ temp;
}

vShiftlr(rm,rs){
op = 1+0;
movRm = 2*8;
newRm = rm+movRm;
movOP = 2*4;
newOp = op*movop;
temp = newOP+newRM;
return = rs+ temp;
}

vShiftRR(rm,rs){
op = 3+0;
movRm = 2*8;
newRm = rm+movRm;
movOP = 2*4;
newOp = op*movop;
temp = newOP+newRM;
return = rs+ temp;
}
