objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
print(len(set([id(i) for i in objects])))
