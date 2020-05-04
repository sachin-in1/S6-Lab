mov a , r0
mov b,#0ah
div ab
mov b,#06h
mul ab
add a , r0
mov r1 , a
stop: sjmp stop