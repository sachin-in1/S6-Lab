MOV R0,#01H
MOV R6,#05H
LOOP: MOV A ,@R0
CJNE A,#42H,DOWN
MOV A , R0
MOV R7, A
SJMP STOP
DOWN: INC R0
DJNZ R6 ,LOOP
STOP: SJMP STOP