ORG 0000H
MOV A, R7
RLC A
JC neg
MOV B,#00H ;if positive then 0 else 1
SJMP last
neg:MOV B,#01H
last:END