grammar = '''

?start  : program
program : "Hello" "World!"

%import common.WS
%ignore WS

'''
