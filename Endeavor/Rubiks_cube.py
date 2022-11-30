import numpy as np
import copy as cp

# 创建六个面，放在faces列表里，顺序为上（0），下（1），左（2），右（3），前（4），后（5）
faces = [np.zeros((3, 3))]

for i in range(1, 6):
    faces.append(np.ones((3, 3)) + faces[i - 1])

t = np.array([[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0]])

# 该面顺时针旋转 90 度
def clockwise(face):
    face = face.transpose().dot(t)
    return face

# 该面逆时针旋转 90 度
def antiClockwise(face):
    face = face.dot(t).transpose()
    return face


def U(FACES):
    FACES[0] = clockwise(FACES[0])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = FACES_new[4], FACES_new[2], FACES_new[5], FACES_new[3]
    FACES[4][0], FACES[2][0], FACES[5][0], FACES[3][0] = d[0], a[0], b[0], c[0]


def _U(FACES):
    FACES[0] = antiClockwise(FACES[0])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = FACES_new[4], FACES_new[2], FACES_new[5], FACES_new[3]
    FACES[4][0], FACES[2][0], FACES[5][0], FACES[3][0] = b[0], c[0], d[0], a[0]


def U2(FACES):
    for i in range(2):
        U(FACES)
    '''
    FACES[0] = clockwise(clockwise(FACES[0]))
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = FACES_new[4], FACES_new[2], FACES_new[5], FACES_new[3]
    FACES[4][0], FACES[2][0], FACES[5][0], FACES[3][0] = c[0], d[0], a[0], b[0]
    '''


def D(FACES):
    FACES[1] = clockwise(FACES[1])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = FACES_new[4], FACES_new[2], FACES_new[5], FACES_new[3]
    FACES[4][2], FACES[2][2], FACES[5][2], FACES[3][2] = b[2], c[2], d[2], a[2]


def _D(FACES):
    FACES[1] = antiClockwise(FACES[1])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = FACES_new[4], FACES_new[2], FACES_new[5], FACES_new[3]
    FACES[4][2], FACES[2][2], FACES[5][2], FACES[3][2] = d[2], a[2], b[2], c[2]


def D2(FACES):
    for i in range(2):
        D(FACES)
    '''
    FACES[1] = clockwise(clockwise(FACES[1]))
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = FACES_new[4], FACES_new[2], FACES_new[5], FACES_new[3]
    FACES[4][2], FACES[2][2], FACES[5][2], FACES[3][2] = c[2], d[2], a[2], b[2]
    '''


def L(FACES):
    FACES[2] = clockwise(FACES[2])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = clockwise(FACES_new[4]), clockwise(FACES_new[1]), antiClockwise(FACES_new[5]), clockwise(FACES_new[0])
    e, f, g, h = cp.deepcopy(a), cp.deepcopy(b), cp.deepcopy(c), cp.deepcopy(d)
    e[0], f[0], g[0], h[0] = d[0], a[0], b[0], c[0]
    FACES[4], FACES[1], FACES[5], FACES[0] = antiClockwise(e), antiClockwise(f), clockwise(g), antiClockwise(h)


def _L(FACES):
    FACES[2] = antiClockwise(FACES[2])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = clockwise(FACES_new[4]), clockwise(FACES_new[1]), antiClockwise(FACES_new[5]), clockwise(FACES_new[0])
    e, f, g, h = cp.deepcopy(a), cp.deepcopy(b), cp.deepcopy(c), cp.deepcopy(d)
    e[0], f[0], g[0], h[0] = b[0], c[0], d[0], a[0]
    FACES[4], FACES[1], FACES[5], FACES[0] = antiClockwise(e), antiClockwise(f), clockwise(g), antiClockwise(h)


def L2(FACES):
    for i in range(2):
        L(FACES)


# 上（0），下（1），左（2），右（3），前（4），后（5）
def R(FACES):
    FACES[3] = clockwise(FACES[3])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = antiClockwise(FACES_new[4]), antiClockwise(FACES_new[1]), clockwise(FACES_new[5]), antiClockwise(
        FACES_new[0])
    e, f, g, h = cp.deepcopy(a), cp.deepcopy(b), cp.deepcopy(c), cp.deepcopy(d)
    g[0], f[0], e[0], h[0] = d[0], c[0], b[0], a[0]
    FACES[4], FACES[1], FACES[5], FACES[0] = clockwise(e), clockwise(f), antiClockwise(g), clockwise(h)


def _R(FACES):
    FACES[3] = antiClockwise(FACES[3])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = antiClockwise(FACES_new[4]), antiClockwise(FACES_new[1]), clockwise(FACES_new[5]), antiClockwise(
        FACES_new[0])
    e, f, g, h = cp.deepcopy(a), cp.deepcopy(b), cp.deepcopy(c), cp.deepcopy(d)
    f[0], g[0], h[0], e[0] = a[0], b[0], c[0], d[0]
    FACES[4], FACES[1], FACES[5], FACES[0] = clockwise(e), clockwise(f), antiClockwise(g), clockwise(h)


def R2(FACES):
    for i in range(2):
        R(FACES)


def F(FACES):
    FACES[4] = clockwise(FACES[4])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = clockwise(clockwise(FACES_new[0])), FACES_new[1], antiClockwise(FACES_new[2]), clockwise(FACES_new[3])
    e, f, g, h = cp.deepcopy(a), cp.deepcopy(b), cp.deepcopy(c), cp.deepcopy(d)
    e[0], g[0], f[0], h[0] = c[0], b[0], d[0], a[0]
    FACES[0], FACES[1], FACES[2], FACES[3] = clockwise(clockwise(e)), f, clockwise(g), antiClockwise(h)


def _F(FACES):
    FACES[4] = antiClockwise(FACES[4])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = clockwise(clockwise(FACES_new[0])), FACES_new[1], antiClockwise(FACES_new[2]), clockwise(FACES_new[3])
    e, f, g, h = cp.deepcopy(a), cp.deepcopy(b), cp.deepcopy(c), cp.deepcopy(d)
    g[0], f[0], h[0], e[0] = a[0], c[0], b[0], d[0]
    FACES[0], FACES[1], FACES[2], FACES[3] = clockwise(clockwise(e)), f, clockwise(g), antiClockwise(h)


def F2(FACES):
    for _ in range(2):
        F(FACES)


# 上（0），下（1），左（2），右（3），前（4），后（5）
def B(FACES):
    FACES[5] = clockwise(FACES[5])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = FACES_new[0], clockwise(clockwise(FACES_new[1])), clockwise(FACES_new[2]), antiClockwise(FACES_new[3])
    e, f, g, h = cp.deepcopy(a), cp.deepcopy(b), cp.deepcopy(c), cp.deepcopy(d)
    g[0], f[0], h[0], e[0] = a[0], c[0], b[0], d[0]
    FACES[0], FACES[1], FACES[2], FACES[3] = e, clockwise(clockwise(f)), antiClockwise(g), clockwise(h)


def _B(FACES):
    FACES[5] = antiClockwise(FACES[5])
    FACES_new = cp.deepcopy(FACES)
    a, b, c, d = FACES_new[0], clockwise(clockwise(FACES_new[1])), clockwise(FACES_new[2]), antiClockwise(FACES_new[3])
    e, f, g, h = cp.deepcopy(a), cp.deepcopy(b), cp.deepcopy(c), cp.deepcopy(d)
    e[0], g[0], f[0], h[0] = c[0], b[0], d[0], a[0]
    FACES[0], FACES[1], FACES[2], FACES[3] = e, clockwise(clockwise(f)), antiClockwise(g), clockwise(h)


def B2(FACES):
    for i in range(2):
        B(FACES)


'''
                          |************|
                          |*U1**U2**U3*|
                          |************|
                          |*U4**U5**U6*|
                          |************|
                          |*U7**U8**U9*|
                          |************|
              ************|************|************|************|
              *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*|
              ************|************|************|************|
              *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*|
              ************|************|************|************|
              *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*|
              ************|************|************|************|
                          |************|
                          |*D1**D2**D3*|
                          |************|
                          |*D4**D5**D6*|
                          |************|
                          |*D7**D8**D9*|
                          |************|
'''


def toString(FACES):
    print()
    for i in range(3):
        print("     ", int(FACES[0][i][0]), int(FACES[0][i][1]), int(FACES[0][i][2]))
    for i in range(3):
        print(int(FACES[2][i][0]), int(FACES[2][i][1]), int(FACES[2][i][2]), end=" ")
        print(int(FACES[4][i][0]), int(FACES[4][i][1]), int(FACES[4][i][2]), end=" ")
        print(int(FACES[3][i][0]), int(FACES[3][i][1]), int(FACES[3][i][2]), end=" ")
        print(int(FACES[5][i][0]), int(FACES[5][i][1]), int(FACES[5][i][2]))
    for i in range(3):
        print("     ", int(FACES[1][i][0]), int(FACES[1][i][1]), int(FACES[1][i][2]))
    print()


def moves(FACES, lst):
    for x in lst:
        if x == 'U':
            U(faces)
        elif x == 'u':
            _U(faces)
        elif x == 'D':
            D(faces)
        elif x == 'd':
            _D(faces)
        elif x == 'L':
            L(faces)
        elif x == 'l':
            _L(faces)
        elif x == 'R':
            R(faces)
        elif x == 'r':
            _R(faces)
        elif x == 'F':
            F(faces)
        elif x == 'f':
            _F(faces)
        elif x == 'B':
            B(faces)
        elif x == 'b':
            _B(faces)


# UBLDFRULFDRULBGBVFDRLLBFLLDSSDBVDJFRUDLRFBDLFBbdj
lst = input("请输入步骤:")
moves(faces, lst)
print("执行后的魔方为")
toString(faces)
reverse = ''.join(map(chr, map(lambda x: ord(x) ^ 32, lst)))[::-1]
moves(faces, reverse)
print("魔方恢复步骤：", reverse)
toString(faces)

