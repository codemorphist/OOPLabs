from equation import *
from math import sqrt

def compare(eq: Equation, 
            coefs: list[int|float], 
            sol: list[int|float]) -> bool:
    e = eq(*coefs).solve()
    e.sort()
    sol.sort()
    return e == sol


def test_linear():
    assert compare(Equation, [0, 0], REAL)
    assert compare(Equation, [1, 1], [-1])
    assert compare(Equation, [0, 1], [])
    assert compare(Equation, [-2, 2], [1])
    assert compare(Equation, [-3, 1], [1/3])


def test_quadratic():
    assert compare(QuadraticEquation, [0, 0, 0], REAL)
    assert compare(QuadraticEquation, [0, 0, 1], [])
    assert compare(QuadraticEquation, [0, 3, -2], [2/3])
    assert compare(QuadraticEquation, [1, 1, 1], [])
    assert compare(QuadraticEquation, [1, 4, 1], [-2-sqrt(3), sqrt(3)-2])
    # assert compare(QuadraticEquation, [6, -4, -11], [1/3+sqrt(35/2)/3,
                                                     # 1/3-sqrt(35/2)/3])
    assert compare(QuadraticEquation, [7, -70, 168], [4, 6])


def test_biquadratic():
    assert compare(BiQuadraticEquation, [0, 0, 0], REAL)
    assert compare(BiQuadraticEquation, [0, 0, 1], [])
    # assert compare(BiQuadraticEquation, [0, 3, -2], [sqrt(2/3), -sqrt(2/3)])
    assert compare(BiQuadraticEquation, [1, 1, 1], [])
    assert compare(BiQuadraticEquation, [1, 4, 1], [])
    # assert compare(BiQuadraticEquation, [6, -4, -11], [sqrt(1/3+sqrt(35/2)/3),
                                                     # -sqrt(1/3+sqrt(35/2)/3)])
    assert compare(BiQuadraticEquation, [7, -70, 168], [-2, 2, -sqrt(6), sqrt(6)])



