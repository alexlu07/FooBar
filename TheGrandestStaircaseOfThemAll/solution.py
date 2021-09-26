def solution(n):
    result = [0 for i in range(n+1)]
    result[0] = 1
    for i in range(1, n+1):
        for j in range(n, i-1, -1):
            result[j] += result[j-i]
            # print(i, j)

    return result[n] - 1

print(solution(3))


