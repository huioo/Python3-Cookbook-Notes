import heapq

# nlargest(n, iterable, key=None)、nsmallest(n, iterable, key=None)
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
largest_n = heapq.nlargest(3, nums)     # 最大的n个值
smallest_n = heapq.nsmallest(3, nums)   # 最小的n个值
print(largest_n, smallest_n)            # [42, 37, 23] [-4, 1, 2]
print(nums, '\n')             # [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])         # 关键字排序
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap, expensive, '\n')
"""
[{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75}] [{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]
"""

# heapify(list)、heappop(heap)组合使用，获取前n个最小的元素
heap = list(nums)
heapq.heapify(heap)     # 堆排序，小顶堆，首位元素最小
print(heap)             # [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
print(heap[0])          # -4；heap[0]永远最小，heapify之后，使用heappop，取出下一个最小的元素
print(heapq.heappop(heap), heap)    # -4 [1, 2, 2, 23, 7, 8, 18, 23, 42, 37]
print(heapq.heappop(heap), heap)    # 1 [2, 2, 8, 23, 7, 37, 18, 23, 42]
print(heapq.heappop(heap), heap)    # 2 [2, 7, 8, 23, 42, 37, 18, 23]
print(heapq.heappop(heap), heap)    # 2 [7, 23, 8, 23, 42, 37, 18]
print()

# heapify(list)、heappush(heap, item)组合使用，
heap = list([1,2,3,-6,5])
heapq.heappush(heap, -5)
print(heap)             # [-5, 2, 1, -6, 5, 3]；heappop单独使用时，会遗漏

heap = list([1,2,3,-6,5])
heapq.heapify(heap)         # heapify()之后，每次heappush之后，heap[0]总是最小
heapq.heappush(heap, -5)    # [-6, 1, -5, 2, 5, 3]
print(heap)
heapq.heappush(heap, -7)    # [-7, 1, -6, 2, 5, 3, -5]
print(heap)

# heapify(list)、heappushpop(heap, item)组合使用
print(heapq.heappushpop(heap, -8))      # -8； 等同于先 heappush 后 heappop
print(heap)                             # [-7, 1, -6, 2, 5, 3, -5]
print(heapq.heappushpop(heap, -4))      # -7
print(heap)                             # [-6, 1, -5, 2, 5, 3, -4]
print()

# heapify(list)、heapreplace(heap, item)组合使用
print(heapq.heapreplace(heap, -8))      # -6； 返回heap第一个元素，并用新元素替换，再_siftup（堆排序）操作一次
print(heap)                             # [-8, 1, -5, 2, 5, 3, -4]
print(heapq.heapreplace(heap, -3))      # -8
print(heap)                             # [-5, 1, -4, 2, 5, 3, -3]
print()

# merge(*iterables, key=None, reverse=False): 合并多个`有序`序列，并排序
print(list(
    heapq.merge([1, 2], [1, 3], [-1, 3, 4, 5, 6])
))
