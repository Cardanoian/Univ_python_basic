def markStars(n):
    if n == 0:
        return '*'
    last_star = markStars(n - 1)
    result = []
    for i in range(3):
        tmp = ''
        for j in range(len(last_star)):
            if i != 1:
                tmp = last_star[j] * 3
            else:
                tmp = last_star[j] + ' ' * (3 ** (n - 1)) + last_star[j]
            result.append(tmp)
    return result


def printStars(stars):
    for i in stars:
        print(i)
