def swap(aa, bb):
    print('2: id(aa)', id(aa), 'id(bb)', id(bb))
    return bb, aa

a = 3
b = 5
print('1: id(a)', id(a), 'id(b)', id(b))
a,b = swap(a,b)
print('3: id(a)', id(a), 'id(b)', id(b))
print('a =',a, 'b =',b)

