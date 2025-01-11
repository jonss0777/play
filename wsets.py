

t = set()


t.add('4')
t.add('56')

print('t: ',t)

y = {'4', '56', '57'}

print('y: ', y)

print('t.issubset()',t.issubset(y) )

print('t.pop()', t.pop())
print('t: ', t)

print('y.issuperset(): ', y.issuperset(t))

t.union({'4', '56'})
print('t.union(): ',t.union(y))

print('t, y', t,y )
print('t.symmetric_difference():', t.symmetric_difference(y))
