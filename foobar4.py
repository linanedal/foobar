def solution(M, F):

    if '^' in M:
        M = int(M.split('^')[0])**int(M.split('^')[1])
    if '^' in F:
        F = int(F.split('^')[0])**int(F.split('^')[1])

    M = int(M)
    F = int(F)
    pair = [M, F]

    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    check = gcd(M, F)
    if check != 1:
        return 'impossible'

    if M == 0 or F == 0:
        return 'impossible'

    count = 0
    while M != 1 and F != 1:
        if M == 1 or F == 1:
            break
        if M > F:
            mul = int(M/F)
            M = M - (F*mul)
            count += mul
        elif M < F:
            mul = int(F/M)
            F = F - (M*mul)
            count += mul

    if M == 1 and F != 1:
        return str(count + (F-1))
    if F == 1 and M != 1:
        return str(count + (M-1))
    if F == 1 and M == 1:
        return str(count)


solution('4', '7')
solution('2', '1')
solution('33', '19')
solution('27', '33')
solution('10','23')
solution('1','1')
solution('10000000000000000000000000000000000000000000000001', '1000000000000000000000000000000005')

# solution('10^50', '10^50')
