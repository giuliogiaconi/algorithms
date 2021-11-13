def karatsuba_prod(x, y):
    """A Python implementation of the efficient Karatsuba multiplication recursive algorithm

    Args:
        x (int): first factor
        y (int): second factor

    Returns:
        int: the product between x and y
    """

    # recursive step
    if x > 10 and y > 10:

        print(f"recursive step: x: {x}; y: {y}")
        lenx = len(str(x))
        leny = len(str(y))
        half = int(max(lenx, leny) / 2)
        splitx = lenx - half
        splity = leny - half
        x1 = int(str(x)[:splitx])
        y1 = int(str(y)[:splity])
        x2 = int(str(x)[splitx:])
        y2 = int(str(y)[splity:])
        # print(f'x1: {x1}; x2: {x2}; y1: {y1}; y2: {y2}')
        x1y1 = karatsuba_prod(x1, y1)
        # print(f'karatsuba product: {x1}*{y1}={x1y1}')
        x2y2 = karatsuba_prod(x2, y2)
        # print(f'karatsuba product: {x2}*{y2}={x2y2}')
        mix = karatsuba_prod(x1 + x2, y1 + y2) - x1y1 - x2y2
        # print(f'karatsuba product ({x1+x2}*{y1+y2}) - {x1y1} - {x2y2} = {mix}')
        prod = x1y1 * (10 ** (half * 2)) + (10 ** (half)) * mix + x2y2

        return prod

    # base case
    if x <= 10 or y <= 10:

        print(f"base case: x: {x}; y: {y}")
        return x * y
