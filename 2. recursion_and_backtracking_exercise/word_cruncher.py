def find_all_solution(idx, target, words_by_idx, words_count, used_words):
    if idx >= len(target):
        print(" ".join(used_words))
        return
    if idx not in words_by_idx:
        return
    for word in words_by_idx[idx]:
        if words_count[word] == 0:
            continue
        used_words.append(word)
        words_count[word] -= 1

        find_all_solution(idx + len(word), target, words_by_idx, words_count, used_words)

        used_words.pop()
        words_count[word] += 1


words = input().split(", ")
target = input()

words_by_idx = {}
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1

    try:
        idx = 0
        while True:
            idx = target.index(word, idx)

            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(word)
            idx += len(word)
    except ValueError:
        pass

find_all_solution(0, target, words_by_idx, words_count, [])

"""
input:
Word, cruncher, cr, h, unch, c, r, un, ch, er
Wordcruncher

output:
Word cruncher
Word cr unch er
Word cr un c h er
Word cr un ch er
Word c r unch er
Word c r un ch er
"""
