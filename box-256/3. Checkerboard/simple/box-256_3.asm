[00] MOV 0, @80
[04] PIX @80, @4C
//Step through memory
[08] ADD @80, 1, @80
//If it's divisable by 10, don't change color
[0C] DIV @80, 10, @90
[10] JEQ @90, @CC, @1C
[14] MOV @90, @CC 
//Otherwise, alternate color
[18] JMP @04
[1C] JNE @3C, 2, @28
[20] MOV 3, @4C
[24] JMP @04
[28] MOV 2, @4C
[2C] JMP @04
[30]
...
[4C] 002
