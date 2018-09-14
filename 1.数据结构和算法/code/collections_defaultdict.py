from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].extend([1, 2, 3])
print(d, '\n')  # defaultdict(<class 'list'>, {'a': [1], 'b': [1, 2, 3]})

d = {}
nums = [
    (1, 0, 1), (5, 1, 5), (2, 2, 2), (4, 3, 4), (3, 4, 3), (2, 5, 6)
]
for priority, index, value in nums:
    d.setdefault(priority, {})[index] = value
print(d, '\n')    # {1: {0: 1}, 5: {1: 5}, 2: {2: 2, 5: 6}, 4: {3: 4}, 3: {4: 3}}

d = {}
nums = [
    (1, 0, 1), (5, 1, 5), (2, 2, 2), (4, 3, 4), (3, 4, 3), (2, 4, 6), (1, 2, 7), (2, 0, 8)
]
for priority, index, value in nums:
    temp = d.setdefault(index, defaultdict(list))
    # print(temp)
    temp[priority].append(value)
print(d)

"""
{
    0: defaultdict(<class 'list'>, {1: [1], 2: [8]}),
    1: defaultdict(<class 'list'>, {5: [5]}),
    2: defaultdict(<class 'list'>, {2: [2], 1: [7]}),
    3: defaultdict(<class 'list'>, {4: [4]}),
    4: defaultdict(<class 'list'>, {3: [3], 2: [6]})
}
"""
