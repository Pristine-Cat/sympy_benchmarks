from sympy import Symbol, Matrix
from sympy import S, simplify

x = Symbol('x')

A = Matrix(8, 8, [x+1]*64)
B = Matrix(8, 8, ([1+x, 1-x]*4 + [1-x, 1+x]*4)*4)
C = Matrix(8, 8, [x+i for i in range (64)])
D = Matrix(S('''[
            [             -3/4,       45/32 - 37*I/16,         1/4 + I/2,      -129/64 - 9*I/64,      1/4 - 5*I/16,      65/128 + 87*I/64,         -9/32 - I/16,      183/256 - 97*I/128],
            [-149/64 + 49*I/32, -177/128 - 1369*I/128,  125/64 + 87*I/64, -2063/256 + 541*I/128,  85/256 - 33*I/16,  805/128 + 2415*I/512, -219/128 + 115*I/256, 6301/4096 - 6609*I/1024],
            [          1/2 - I,         9/4 + 55*I/16,              -3/4,       45/32 - 37*I/16,         1/4 + I/2,      -129/64 - 9*I/64,         1/4 - 5*I/16,        65/128 + 87*I/64],
            [   -5/8 - 39*I/16,   2473/256 + 137*I/64, -149/64 + 49*I/32, -177/128 - 1369*I/128,  125/64 + 87*I/64, -2063/256 + 541*I/128,     85/256 - 33*I/16,    805/128 + 2415*I/512],
            [            1 + I,         -19/4 + 5*I/4,           1/2 - I,         9/4 + 55*I/16,              -3/4,       45/32 - 37*I/16,            1/4 + I/2,        -129/64 - 9*I/64],
            [         21/8 + I,    -537/64 + 143*I/16,    -5/8 - 39*I/16,   2473/256 + 137*I/64, -149/64 + 49*I/32, -177/128 - 1369*I/128,     125/64 + 87*I/64,   -2063/256 + 541*I/128],
            [               -2,         17/4 - 13*I/2,             1 + I,         -19/4 + 5*I/4,           1/2 - I,         9/4 + 55*I/16,                 -3/4,         45/32 - 37*I/16],
            [     1/4 + 13*I/4,    -825/64 - 147*I/32,          21/8 + I,    -537/64 + 143*I/16,    -5/8 - 39*I/16,   2473/256 + 137*I/64,    -149/64 + 49*I/32,   -177/128 - 1369*I/128]]'''))

# Smaller test matrices if the big ones run too long.

# A = Matrix(4, 4, [x+1]*16)
# B = Matrix(4, 4, ([1+x, 1-x]*2 + [1-x, 1+x]*2)*2)
# C = Matrix(4, 4, [x+i for i in range (16)])
# D = Matrix(S('''[
#             [             -3/4,       45/32 - 37*I/16,         1/4 + I/2,      -129/64 - 9*I/64],
#             [-149/64 + 49*I/32, -177/128 - 1369*I/128,  125/64 + 87*I/64, -2063/256 + 541*I/128],
#             [          1/2 - I,         9/4 + 55*I/16,              -3/4,       45/32 - 37*I/16],
#             [   -5/8 - 39*I/16,   2473/256 + 137*I/64, -149/64 + 49*I/32, -177/128 - 1369*I/128]]'''))


class TimeMatrixPowerA04:
    def time_PowA04(self): A**4
    def time_PowA04MulSimp(self): A.pow(4, mulsimp=True)
    def time_PowA04Simplify(self): simplify(A**4)

class TimeMatrixPowerA07:
    def time_PowA07(self): A**7
    def time_PowA07MulSimp(self): A.pow(7, mulsimp=True)
    def time_PowA07Simplify(self): simplify(A**7)

class TimeMatrixPowerA13:
    def time_PowA13(self): A**13
    def time_PowA13MulSimp(self): A.pow(13, mulsimp=True)
    def time_PowA13Simplify(self): simplify(A**13)

class TimeMatrixPowerA16:
    def time_PowA16(self): A**16
    def time_PowA16MulSimp(self): A.pow(16, mulsimp=True)
    def time_PowA16Simplify(self): simplify(A**16)


class TimeMatrixPowerB04:
    def time_PowB04(self): B**4
    def time_PowB04MulSimp(self): B.pow(4, mulsimp=True)
    def time_PowB04Simplify(self): simplify(B**4)

class TimeMatrixPowerB07:
    def time_PowB07(self): B**7
    def time_PowB07MulSimp(self): B.pow(7, mulsimp=True)
    def time_PowB07Simplify(self): simplify(B**7)

class TimeMatrixPowerB13:
    def time_PowB13(self): B**13
    def time_PowB13MulSimp(self): B.pow(13, mulsimp=True)
    def time_PowB13Simplify(self): simplify(B**13)

class TimeMatrixPowerB16:
    def time_PowB16(self): B**16
    def time_PowB16MulSimp(self): B.pow(16, mulsimp=True)
    def time_PowB16Simplify(self): simplify(B**16)


class TimeMatrixPowerC04:
    def time_PowC04(self): C**4
    def time_PowC04MulSimp(self): C.pow(4, mulsimp=True)
    def time_PowC04Simplify(self): simplify(C**4)

class TimeMatrixPowerC07:
    def time_PowC07(self): C**7
    def time_PowC07MulSimp(self): C.pow(7, mulsimp=True)
    def time_PowC07Simplify(self): simplify(C**7)

class TimeMatrixPowerC13:
    def time_PowC13(self): C**13
    def time_PowC13MulSimp(self): C.pow(13, mulsimp=True)
    def time_PowC13Simplify(self): simplify(C**13)

class TimeMatrixPowerC16:
    def time_PowC16(self): C**16
    def time_PowC16MulSimp(self): C.pow(16, mulsimp=True)
    def time_PowC16Simplify(self): simplify(C**16)


class TimeMatrixPowerD04:
    def time_PowD04(self): D**4
    def time_PowD04MulSimp(self): D.pow(4, mulsimp=True)
    def time_PowD04Simplify(self): simplify(D**4)

class TimeMatrixPowerD07:
    def time_PowD07(self): D**7
    def time_PowD07MulSimp(self): D.pow(7, mulsimp=True)
    def time_PowD07Simplify(self): simplify(D**7)

class TimeMatrixPowerD13:
    def time_PowD13(self): D**13
    def time_PowD13MulSimp(self): D.pow(13, mulsimp=True)
    def time_PowD13Simplify(self): simplify(D**13)

class TimeMatrixPowerD16:
    def time_PowD16(self): D**16
    def time_PowD16MulSimp(self): D.pow(16, mulsimp=True)
    def time_PowD16Simplify(self): simplify(D**16)
