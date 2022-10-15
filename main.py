size_a = int(input ('press enter size_a: '))
size_b = int(input ('press enter size_b: '))
size_c = int(input ('press enter size_c: '))

if 0 in (size_a, size_b, size_c):
    print('there are no such triangles.')
else:
    perimeter = size_a + size_b + size_c
    print('Perimetr: ', perimeter)
    if perimeter > 20:
        print('Max size is:', max(size_a, size_b, size_c))
    elif perimeter < 10:
        print('Min size is:', min(size_a, size_b, size_c))

