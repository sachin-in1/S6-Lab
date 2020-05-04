ORG 00000H
MOV A,#18H
MOV R3,A
MOV B,#09H
MOV R4,B
MUL AB
MOV R0,A ;Product is in R0 and R1 (Higher order byte)
MOV R1,B
MOV A,R3
MOV B,R4
DIV AB
MOV R2,A ;Quotient is in R2
END