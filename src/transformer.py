from lark import Transformer


class _IntegerTransformer(Transformer):
    def hex_integer(self, v):
        return int(v[0][2:], base=16)

    def oct_integer(self, v):
        return int(v[0][2:], base=8)

    def bin_integer(self, v):
        return int(v[0][2:], base=2)

    def dec_integer(self, v):
        return int(v[0][2:] if v[0][1:2] == 'd' else v[0], base=10)


class _MathTransformer(Transformer):
    def math_expr(self, v):
        return v[0]

    def add(self, v):
        return v[0] + v[1]

    def sub(self, v):
        return v[0] - v[1]

    def mul(self, v):
        return v[0] * v[1]

    def div(self, v):
        return v[0] // v[1]

    def modulo(self, v):
        return v[0] % v[1]

    def power(self, v):
        return v[0] ** v[1]

    def unary_pos(self, v):
        return +v[0]

    def unary_neg(self, v):
        return -v[0]

    def logical_not(self, v):
        return not v[0]

    def bitwise_not(self, v):
        return ~v[0]

    def bitwise_left_shift(self, v):
        return v[0] << v[1]

    def bitwise_right_shift(self, v):
        return v[0] >> v[1]

    def more_than(self, v):
        return v[0] > v[1]

    def less_than(self, v):
        return v[0] < v[1]

    def more_than_or_equal(self, v):
        return v[0] >= v[1]

    def less_than_or_equal(self, v):
        return v[0] <= v[1]

    def equal_to(self, v):
        return v[0] == v[1]

    def not_equal_to(self, v):
        return v[0] != v[1]

    def bitwise_and(self, v):
        return v[0] & v[1]

    def bitwise_xor(self, v):
        return v[0] ^ v[1]

    def bitwise_or(self, v):
        return v[0] | v[1]

    def logical_and(self, v):
        return v[0] and v[1]

    def logical_or(self, v):
        return v[0] or v[1]

    def ternary(self, v):
        return v[1] if v[0] else v[2]


class ObjAsTransformer(_IntegerTransformer, _MathTransformer):
    pass
