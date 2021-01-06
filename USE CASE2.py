# comprehensions

list_even = [ x for x in range(20) if x % 2 == 0]
print(list_even)
list_odd = [ x for x in range(20) if x % 2 != 0]
print(list_odd)
list_square = [ x*x for x in range(20)]
print(list_square)
list_cube = [ x*x*x for x in range(20)]
print(list_cube)