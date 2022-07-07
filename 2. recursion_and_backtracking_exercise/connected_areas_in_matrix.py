def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0

    if matrix[row][col] != "-":
        return 0

    matrix[row][col] = "v"

    result = 1
    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col - 1, matrix)
    result += explore_area(row, col + 1, matrix)

    return result


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        areas.append((row, col, size))

print(f"Total areas found: {len(areas)}")
for idx, area in enumerate(sorted(areas, key=lambda a: a[2], reverse=True)):
    print(f"Area #{idx + 1} at ({area[0]}, {area[1]}), size: {area[2]}")

"""
5
10
*--*---*--
*--*---*--
*--*****--
*--*---*--
*--*---*--

Total areas found: 4
Area #1 at (0, 1), size: 10
Area #2 at (0, 8), size: 10
Area #3 at (0, 4), size: 6
Area #4 at (3, 4), size: 6

Process finished with exit code 0
"""
