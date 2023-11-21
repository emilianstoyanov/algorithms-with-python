first_word = input()
second_word = input()

rows = len(first_word) + 1
cols = len(second_word) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first_word[row - 1] == second_word[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(dp[rows - 1][cols - 1])

row = rows - 1
col = cols - 1
result = []

while row > 0 and col > 0:
    if first_word[row - 1] == second_word[col - 1]:
        result.append(first_word[row - 1])
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(list(reversed(result)))
