grammar = '''

?start  : program
program : (directive | instruction NEWLINE)*

directive : "Hello" "World" "!"

?instruction : addi | andi | slli | slti | sltiu | xori | srli | srai 
             | ori | lui | auipc | add | sub | sll | slt | sltu | xor 
             | srl | sra | or | and | jal | jalr | beq | bne | blt | bge 
             | bltu | bgeu | lb | lh | lw | lbu | lhu | sb | sh | sw 
             | fence | fence_i | ecall | ebreak

reg         : /x([1-2][0-9]|3[0-1]|[0-9])|zero|ra|[sgt]p|t[0-6]|a[0-7]|s1[01]|s[0-9]|this/
?integer    : BIN_INTEGER -> bin_integer 
            | OCT_INTEGER -> oct_integer 
            | HEX_INTEGER -> hex_integer 
            | DEC_INTEGER -> dec_integer

math_expr       : ternary
?ternary        : logical_or
                | logical_or "?" ternary ":" ternary -> ternary
?logical_or     : logical_and
                | logical_or "||" logical_and -> logical_or
?logical_and    : bitwise_or
                | logical_and "&&" bitwise_or -> logical_and
?bitwise_or     : bitwise_xor
                | bitwise_or "|" bitwise_xor -> bitwise_or
?bitwise_xor    : bitwise_and
                | bitwise_xor "^" bitwise_and -> bitwise_xor
?bitwise_and    : equal
                | bitwise_and "&" equal -> bitwise_and
?equal          : more_less
                | equal "==" more_less -> equal_to
                | equal "!=" more_less -> not_equal_to
?more_less      : bitwise_shift
                | more_less ">"  bitwise_shift -> more_than
                | more_less "<"  bitwise_shift -> less_than
                | more_less ">=" bitwise_shift -> more_than_or_equal
                | more_less "<=" bitwise_shift -> less_than_or_equal
?bitwise_shift  : sum
                | bitwise_shift "<<" sum -> bitwise_left_shift
                | bitwise_shift ">>" sum -> bitwise_right_shift
?sum            : product
                | sum "+" product -> add
                | sum "-" product -> sub
?product        : power
                | product "*" power -> mul
                | product "/" power -> div
                | product "%" power -> modulo
?power          : unary
                | unary "**" power -> power
?unary          : atomic
                | "+"      unary -> unary_pos
                | "-"      unary -> unary_neg
                | "!"      unary -> logical_not
                | "~"      unary -> bitwise_not
                | "sizeof" unary -> sizeof
?atomic         : integer
                | "(" ternary ")"

DEC_INTEGER    : /(0[Dd])?[0-9_]+/
HEX_INTEGER.10 : /0[Xx][0-9a-fA-F_]+/
OCT_INTEGER.10 : /0[Oo][0-7_]+/
BIN_INTEGER.10 : /0[Bb][01_]+/

// I-type инструкции
addi	: "addi" reg "," reg "," math_expr
andi	: "andi" reg "," reg "," math_expr
slli	: "slli" reg "," reg "," math_expr
slti	: "slti" reg "," reg "," math_expr
sltiu	: "sltiu" reg "," reg "," math_expr
xori	: "xori" reg "," reg "," math_expr
srli	: "srli" reg "," reg "," math_expr
srai	: "srai" reg "," reg "," math_expr
ori	    : "ori" reg "," reg "," math_expr

// U-type инструкции
lui		: "lui" reg "," math_expr
auipc	: "auipc" reg "," math_expr

// R-type инструкции
add		: "add" reg "," reg "," reg
sub		: "sub" reg "," reg "," reg
sll		: "sll" reg "," reg "," reg
slt		: "slt" reg "," reg "," reg
sltu	: "sltu" reg "," reg "," reg
xor		: "xor" reg "," reg "," reg
srl		: "srl" reg "," reg "," reg
sra		: "sra" reg "," reg "," reg
or	    : "or" reg "," reg "," reg
and		: "and" reg "," reg "," reg

// J-type инструкции
jal		: "jal" reg "," math_expr
jalr	: "jalr" reg "," reg "," math_expr

// B-type инструкции
beq		: "beq" reg "," reg "," math_expr
bne		: "bne" reg "," reg "," math_expr
blt		: "blt" reg "," reg "," math_expr
bge		: "bge" reg "," reg "," math_expr
bltu	: "bltu" reg "," reg "," math_expr
bgeu	: "bgeu" reg "," reg "," math_expr

// S-type инструкции (load/store)
lb	    : "lb" reg "," math_expr "(" reg ")"
lh	    : "lh" reg "," math_expr "(" reg ")"
lw	    : "lw" reg "," math_expr "(" reg ")"
lbu		: "lbu" reg "," math_expr "(" reg ")"
lhu		: "lhu" reg "," math_expr "(" reg ")"
sb	    : "sb" reg "," math_expr "(" reg ")"
sh	    : "sh" reg "," math_expr "(" reg ")"
sw	    : "sw" reg "," math_expr "(" reg ")"

// Special instructions
fence	: "fence"
fence_i	: "fence.i"
ecall	: "ecall"
ebreak	: "ebreak"

%import common.WS
%import common.C_COMMENT
%import common.NEWLINE
%ignore WS
%ignore C_COMMENT
%ignore /;.*/

'''
