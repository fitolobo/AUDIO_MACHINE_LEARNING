def sum(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    if n<= 0:
        return 0
    return n + sum(n-1)

sum(3)