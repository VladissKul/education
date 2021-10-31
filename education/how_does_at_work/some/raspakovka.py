a, b, *c = [1, 2, 3, True, 'hell', 'mood']
print(a, b, c)
a, *b, c = [1, 2, 3, True, 'hell', 'mood']
print(a, b, c)
a, *b, c = [1, 2]
print(a, b, c)

s = [4, 10]
print(list(range(*s)))  # *s распаковывает список

a = [1, 2, 3, 4]
print(*a)
