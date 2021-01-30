def is_square(n):
    if n < 0:
        return False
    
    n_sqrt = n ** 0.5
    
    if n_sqrt.is_integer():
        return True
    else:
        return False