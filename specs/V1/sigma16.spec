input:
  RRR

RRR:
  op1 = 4
  d = 4
  a = 4
  b = 4

RRX:
  op2 = 4
  d = 4
  a = 4
  b = 4
  dis = 16

op1:
  "add":0
  "sub":1
  "mul":2
  "div":3
  "cmplt":4
  "cmpeq":5
  "cmpgt":6
  "inv":7
  "and":8
  "or":9
  "xor":a
  "shiftl":b
  "shiftr":c
  "trap":d

d | a | b : "R(num)":num
