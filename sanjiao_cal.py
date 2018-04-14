"""
包含两个定理，注意三角函数使用的是弧度，radians()转化
"""
from math import cos, sqrt, sin, asin, degrees, radians

# 余弦定理，求第三边，已知a,b边，夹角C
def bian(a, b, C):
    C = radians(C)
    m = a**2 + b**2 -2*a*b*cos(C)
    m = sqrt(m)
    return m

# 正弦定理， 求一个角，已知a边，角A,求b边所对角B 
def jiao(a, b, A):
    A = radians(A)
    sinB= b * sin(A) / a
    B = asin(sinB)
    B = degrees(B)
    return B

AB = sqrt(6)
BC = 5-sqrt(3)
CD = 6
C = 120
ABC = 135
BD = bian(BC,CD,C)

print('BD = %s '% BD)

CBD = jiao(BD, CD, C)

print('jiaoCBD= %s ' % CBD)

ABD = ABC - CBD

AD = bian(AB, BD, ABD)

print('AD = %s' %AD)



