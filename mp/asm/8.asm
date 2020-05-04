ORG 0000H
MOV R0, #030H ;Start address of array
MOV R7,#04H ;number of elements
MOV A,@R0 ;smallest stored in R1
MOV R1,A
MOV B,@R0
MOV R2,B ;largest stored in R2
INC R0
Find:DJNZ R7,next
JMP END
next:CLR C
MOV A,R1
SUBB A,@R0
JNC small ;a is small
JMP check
small:MOV A,@R0 
MOV R1,A
check:CLR C
MOV A,R2
SUBB A,@R0
JC large
JMP finish
large:MOV A,@R0
MOV R2,A
finish:INC R0
JMP find ;smallest in R1 ,largest in R2
END: END