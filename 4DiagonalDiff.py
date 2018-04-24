def diagonalDifference(a):
    sum = 0
    sumneg = 0
    i = 0
    while i < len(a):
        if i == 0:
            sum = sum + a[i][-1]
        sum = sum + a[i][i]
        print(a[i][i])
        sumneg = sumneg + a[-i][i]
        print(a[i][-i])
        i = i+1
    return abs(sum+sumneg)

if __name__ == '__main__':

    n = [[11,2,4],[4,5,6],[10,8,-12]]

    #n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))
    print(a)
    result = diagonalDifference(a)
    print(result)
