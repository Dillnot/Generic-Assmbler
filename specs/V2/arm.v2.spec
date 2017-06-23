grammer ARM32;
prog: line*;
line = (label)? (Data_processing);

Data_processing:  (DP_one | DP_two) -> h(0):w(32,0):(11,1):(4,2);

DP_one: DP_one_op cond RD shift_op
DP_one_op: "MOV" -> h(13):w(32,0):(7,4)
        | "MVN" -> h(15):w(32,0):(7,4)
        ;

DP_two: DP_two_op cond RD RN shift_OP
DP_two_op: "AND" -> h(0):w(32,0):(7,4)
        | "EOR" -> h(1):w(32,0):(7,4)
        | "SUB" -> h(2):w(32,0):(7,4)
        | "RSB" -> h(3):w(32,0):(7,4)
        | "ADD" -> h(4):w(32,0):(7,4)
        | "ADC" -> h(5):w(32,0):(7,4)
        | "SBC" -> h(6):w(32,0):(7,4)
        | "RSC" -> h(7):w(32,0):(7,4)
        | "TST" -> h(8):w(32,0):(7,4)
        | "TEQ" -> h(9):w(32,0):(7,4)
        | "CMP" -> h(10):w(32,0):(7,4)
        | "CMN" -> h(11):w(32,0):(7,4)
        | "ORR" -> h(12):w(32,0):(7,4)
        | "BIC" -> -> h(14):w(32,0):(7,4)
        ;

shift_op: RM - > h(0):w(32,0):(20,8)
        | Log_shift_li -> h(0):w(32,0):(25,3);
        | Log_shift_lr -> h(1):w(32,0):(24,4);
        | Log_shift_ri -> h(2):w(32,0):(25,3);
        | Log_shift_rr -> h(3):w(32,0):(24,4);
        ;

Log_shift_li: RM , "LSL #" imi -> n(imi):w(32,0):(20,5);
Log_shift_lr: RM , "LSL" RS;

Log_shift_ri: RM , "LSR #" imi -> n(imi):w(32,0):(20,5);
Log_shift_rr: RM , "LSR" RS;


cond: -> h(14)->w(32,0)->(0,4)
    |"{" code "}"
    ;

code: "EQ" -> h(0)->w(32,0)->(0,4)
    | "NE" -> h(1)->w(32,0)->(0,4)
    | "CS" -> h(2)->w(32,0)->(0,4)
    | "CC" -> h(3)->w(32,0)->(0,4)
    | "MI" -> h(4)->w(32,0)->(0,4)
    | "PL" -> h(5)->w(32,0)->(0,4)
    | "VS" -> h(6)->w(32,0)->(0,4)
    | "VC" -> h(7)->w(32,0)->(0,4)
    | "HI" -> h(8)->w(32,0)->(0,4)
    | "LS" -> h(9)->w(32,0)->(0,4)
    | "GE" -> h(10)->w(32,0)->(0,4)
    | "LT" -> h(11)->w(32,0)->(0,4)
    | "GT" -> h(12)->w(32,0)->(0,4)
    | "LE" -> h(13)->w(32,0)->(0,4)
    ;

RM: reg:w(32,0):(28,4)
RD: reg:w(32,0):(16,4);
RN: reg:w(32,0):(12,4);
RS: reg:w(32,0):(20,4);
reg:'R' num -> D(num);
