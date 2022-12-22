n, m = [int(num) for num in input().split()]
n_set = set()
m_set = set()

for i in range(1, n + m + 1):
    number = int(input())

    if i <= n:
        n_set.add(number)
    else:
        m_set.add(number)

unique_nums = [num for num in n_set if num in m_set]
print(*unique_nums, sep="\n")