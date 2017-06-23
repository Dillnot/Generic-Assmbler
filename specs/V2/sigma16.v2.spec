grammar sigma16;
prog: line*;
line: (label)? (RRR | RRX);
RRR: opR ',' regD ',' regA ',' regB;

opR: 'add' -> h(0):w(16,0):(0,4)
  | 'sub' -> h(1):w(16,0):(0,4)
  | 'mul' -> h(2):w(16,0):(0,4)
  | 'div' -> h(3):w(16,0):(0,4)
  | 'cmplt' -> h(4):w(16,0):(0,4)
  | 'cmpeq' -> h(5):w(16,0):(0,4)
  | 'cmpgt' -> h(6):w(16,0):(0,4)
  | 'inv' -> h(7):w(16,0):(0,4)
  | 'and' -> h(8):w(16,0):(0,4)
  | 'or' -> h(9):w(16,0):(0,4)
  | 'xor' -> h(a):w(16,0):(0,4)
  | 'shiftl' -> h(b):w(16,0):(0,4)
  | 'shiftr' -> h(c):w(16,0):(0,4)
  | 'trap' -> h(d):w(16,0):(0,4)
  ;

RegD: reg:w(16,0):(5,4);
RegA: reg:w(16,0):(9,4);
RegB: reg:w(16,0):(13,4);
reg:'R' num -> D(num);

RRX: opX ',' regD ',' disp '[' regA ']' -> h(f):w(16,0):(0,4);
opX: 'lea' ->  h(0):w(16,0):(13,4)
  | 'load' ->  h(1):w(16,0):(13,4)
  | 'store' ->  h(2):w(16,0):(13,4)
  | 'jump' ->  h(3):w(16,0):(13,4)
  | 'jumpf' ->  h(4):w(16,0):(13,4)
  | 'jumpt' ->  h(5):w(16,0):(13,4)
  | 'jal' ->  h(6):w(16,0):(13,4)
  ;

disp: num -> d(num):w(16,1):(0,16);

num: [0-9]+;
