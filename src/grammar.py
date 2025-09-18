grammar = r'''

?start  : scope
scope   : (directive | instruction | label_def)*

?directive  : "section" NAME \
            -> section
            | "namespace" NAME "{" scope "}" \
            -> namespace
            | "using" NAME ("::" NAME)* ("::" STAR)? \
            -> using

reg      : /x([1-2][0-9]|3[0-1]|[0-9])|zero|ra|[sgt]p|t[0-6]|a[0-7]|s1[0-1]|s[0-9]|this/
?integer : BIN_INTEGER -> bin_integer
         | OCT_INTEGER -> oct_integer
         | HEX_INTEGER -> hex_integer
         | DEC_INTEGER -> dec_integer

label_def    : _dotted_name ":"
label_val    : _dotted_name
_dotted_name : NAME ("." NAME)*

?math_expr      : ternary
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
                | label_val

DEC_INTEGER    : /(0[Dd])?[0-9_]+/
HEX_INTEGER.10 : /0[Xx][0-9a-fA-F_]+/
OCT_INTEGER.10 : /0[Oo][0-7_]+/
BIN_INTEGER.10 : /0[Bb][01_]+/

// ОСНОВНОЕ ПРАВИЛО для всех инструкций с сохранением типа
instruction : r_type_instr
            | i_type_instr
            | s_type_instr
            | b_type_instr
            | u_type_instr
            | j_type_instr
            | special_instr

// R-TYPE ИНСТРУКЦИИ (арифметика регистр-регистр) [10]
!r_type_instr : "add"  rrr_args
              | "sub"  rrr_args
              | "sll"  rrr_args
              | "slt"  rrr_args
              | "sltu" rrr_args
              | "xor"  rrr_args
              | "srl"  rrr_args
              | "sra"  rrr_args
              | "or"   rrr_args
              | "and"  rrr_args

// I-TYPE ИНСТРУКЦИИ (арифметика с непосредственным значением) [15]
!i_type_instr : "addi"  rri_args
              | "slti"  rri_args
              | "sltiu" rri_args
              | "xori"  rri_args
              | "ori"   rri_args
              | "andi"  rri_args
              | "slli"  rri_args
              | "srli"  rri_args
              | "srai"  rri_args
              | "lb"    mem_args
              | "lh"    mem_args
              | "lw"    mem_args
              | "lbu"   mem_args
              | "lhu"   mem_args
              | "jalr"  mem_args

// S-TYPE ИНСТРУКЦИИ (сохранение в память) [3]
!s_type_instr : "sb" mem_args
              | "sh" mem_args
              | "sw" mem_args

// B-TYPE ИНСТРУКЦИИ (условные переходы) [6]
!b_type_instr : "beq"  rri_args
              | "bne"  rri_args
              | "blt"  rri_args
              | "bge"  rri_args
              | "bltu" rri_args
              | "bgeu" rri_args

// U-TYPE ИНСТРУКЦИИ (загрузка верхних бит) [2]
!u_type_instr : "lui"    ri_args
              | "auipc"  ri_args

// J-TYPE ИНСТРУКЦИИ (безусловные переходы) [1]
!j_type_instr : "jal"    ri_args

// Instructions with special arguments [4]
!special_instr  : FENCE   fence_args
                | FENCE_I
                | "ecall"
                | "ebreak"

// ФОРМАТЫ АРГУМЕНТОВ (детализированные)
rrr_args      : reg "," reg "," reg
rri_args      : reg "," reg "," math_expr
mem_args      : reg "," math_expr "(" reg ")"
ri_args       : reg "," math_expr
fence_args    : /[iorw]+/ "," /[iorw]+/

FENCE       : "fence"
FENCE_I.10  : "fence.i"
NAME        : /[A-Za-z_@][A-Za-z_@0-9]+/
STAR        : "*"

%import common.WS
%import common.C_COMMENT
%import common.NEWLINE
%ignore WS
%ignore C_COMMENT
%ignore /;.*/

'''
