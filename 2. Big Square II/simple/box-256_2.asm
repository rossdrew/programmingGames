01F2 Cycles

//Setup outer square
[00] mov 11, @80 
[04] mov 38, @C0
[08] pix @80, 1

//Setup inner square
[0C] jne 21, @80, @24
[10] mov 22, @80
[14] mov 48, @C0
[18] mov 00, @81
[1C] mov 0B, @44

//Main draw loop
[20] jmp @08
[24] add @80, *C0, @80
[28] add @81, 1, @81
[2C] jgr @34, @81, -14
[30] mov @C0, 1, @C0
[34] add @C0, 01, @C0
[38] jmp @C8
[3C]
[40]
[44] 00D
[48] 001 010 -01 -10
