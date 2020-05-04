ORG 0000H
CLR C
MOV A,#013H;lower byte
SUBB A,#003H;lower byte
MOV R1,A
MOV A,#055H ;Higher byte
SUBB A,#010H ;Higher byte
MOV R0,A ;lower byte of result in R1 higher byte in R0
END