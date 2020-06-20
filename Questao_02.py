def em_equilibrio(a, b, c, d):
    if a == b + c + d and d == b + c and b == c:
        return True
    else:
        return False


print(em_equilibrio(500, 125, 125, 250))
