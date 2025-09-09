grammar = '''

?start  : program
program : (directive | instruction)*

directive : "Hello" "World" "!"

?instruction : addi | andi | slli | slti | sltiu | xori | srli | srai 
             | ori | lui | auipc | add | sub | sll | slt | sltu | xor 
             | srl | sra | or | and | jal | jalr | beq | bne | blt | bge 
             | bltu | bgeu | lb | lh | lw | lbu | lhu | sb | sh | sw 
             | fence | fence_i | ecall | ebreak

REG : /x([1-2][0-9]|3[0-1]|[0-9])|zero|ra|[sgt]p|t[0-6]|a[0-7]|s1[01]|s[0-9]|this/
IMM : /0x[0-9a-fA-F]+|0o[0-7]+|[0-9]+/

// I-type инструкции
addi	: "addi" REG "," REG "," IMM
andi	: "andi" REG "," REG "," IMM
slli	: "slli" REG "," REG "," IMM
slti	: "slti" REG "," REG "," IMM
sltiu	: "sltiu" REG "," REG "," IMM
xori	: "xori" REG "," REG "," IMM
srli	: "srli" REG "," REG "," IMM
srai	: "srai" REG "," REG "," IMM
ori	    : "ori" REG "," REG "," IMM

// U-type инструкции
lui		: "lui" REG "," IMM
auipc	: "auipc" REG "," IMM

// R-type инструкции
add		: "add" REG "," REG "," REG
sub		: "sub" REG "," REG "," REG
sll		: "sll" REG "," REG "," REG
slt		: "slt" REG "," REG "," REG
sltu	: "sltu" REG "," REG "," REG
xor		: "xor" REG "," REG "," REG
srl		: "srl" REG "," REG "," REG
sra		: "sra" REG "," REG "," REG
or	    : "or" REG "," REG "," REG
and		: "and" REG "," REG "," REG

// J-type инструкции
jal		: "jal" REG "," IMM
jalr	: "jalr" REG "," REG "," IMM

// B-type инструкции
beq		: "beq" REG "," REG "," IMM
bne		: "bne" REG "," REG "," IMM
blt		: "blt" REG "," REG "," IMM
bge		: "bge" REG "," REG "," IMM
bltu	: "bltu" REG "," REG "," IMM
bgeu	: "bgeu" REG "," REG "," IMM

// S-type инструкции (load/store)
lb	    : "lb" REG "," IMM "(" REG ")"
lh	    : "lh" REG "," IMM "(" REG ")"
lw	    : "lw" REG "," IMM "(" REG ")"
lbu		: "lbu" REG "," IMM "(" REG ")"
lhu		: "lhu" REG "," IMM "(" REG ")"
sb	    : "sb" REG "," IMM "(" REG ")"
sh	    : "sh" REG "," IMM "(" REG ")"
sw	    : "sw" REG "," IMM "(" REG ")"

// Special instructions
fence	: "fence"
fence_i	: "fence.i"
ecall	: "ecall"
ebreak	: "ebreak"

%import common.WS
%import common.C_COMMENT
%ignore WS
%ignore C_COMMENT
%ignore /;.*/

'''
