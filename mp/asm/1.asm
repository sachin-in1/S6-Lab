ORG 0000H
CLR C
MOV A,#03aH;lower byte of first
ADD A,#011H ;lower byte of second
MOV R1,A
MOV A,#012H ;upper byte of first
ADDC A,#010H ;upper byte of second
MOV R0,A; lower byte of result in R1 upper byte in R0
END