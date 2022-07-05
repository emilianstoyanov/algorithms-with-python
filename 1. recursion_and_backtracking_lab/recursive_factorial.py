def calc_fact(n):
    if n == 0:
        return 1
    return n * calc_fact(n - 1)


# 5
n = int(input())

# 120
print(calc_fact(n))
