from Point import Point
from Triangle import Triangle


def read_f_f(path_tf):
    with open(path_tf, 'r') as file:
        lst = file.readlines()
    lst = [[float(n) for n in x.split()] for x in lst]
    return lst


def gen_triangles(coords):
    a = Point(coords[0], coords[1])
    b = Point(coords[2], coords[3])
    c = Point(coords[4], coords[5])
    return Triangle(a, b, c)


def in_one_quarter(t_l):
    if t_l.a.x * t_l.b.x > 0 and \
            t_l.b.x * t_l.c.x > 0 and \
            t_l.a.x * t_l.c.x > 0 and \
            t_l.a.y * t_l.b.y > 0 and \
            t_l.b.y * t_l.c.y > 0 and \
            t_l.a.y * t_l.c.y > 0:
        return t_l


path = input('path to input file > ')
list_coords = read_f_f(path)

triangles = [gen_triangles(c) for c in list_coords]

result = [t for t in triangles if in_one_quarter(t)]

for obj in result:
    print(obj)