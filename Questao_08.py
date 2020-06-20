def passa_pela_janela(a, b, c, h, l):
    if a <= h and b <= l or a <= l and b <= h or a <= h and c <= l or a <= l and c <= h or b <= h and c <= l or b <= l and c <= h:
        return True
    else:
        return False


print(passa_pela_janela(20,22,5,20,10))
