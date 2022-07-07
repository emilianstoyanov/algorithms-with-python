def nested_loops(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=" ")
        return
    for num in range(1, len(arr) + 1):
        arr[idx] = num
        nested_loops(idx + 1, arr)


n = int(input())
arr = [None] * n
nested_loops(0, arr)

"""
input:
2

output:
1 1
1 2
2 1
2 2

"""