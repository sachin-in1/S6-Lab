ORG 0000H
MOV B,R0;number whose factorial should be found
MOV R1,B
MOV A,#01H
DO:MUL AB;
DEC R1
MOV B,R1
CJNE R1,#01,DO
END