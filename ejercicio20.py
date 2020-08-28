def año_bisiesto(n):
    if n % 4 == 0 and n % 100 != 0:
        return True
    elif n % 400 == 0:
        return True
    else:
        return False


