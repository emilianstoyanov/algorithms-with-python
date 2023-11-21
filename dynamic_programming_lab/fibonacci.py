def fibonacci(n):
    if n <= 2:
        return 1

    result = fibonacci(n - 1) + fibonacci(n - 2)

    return result


print(fibonacci(36))
