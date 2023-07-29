def getSum(a: int, b: int) -> int:
    # below solution does not work with negative numbers (it works in different languages though like c++)
    # TODO have to find out why it does not work in python
    while b != 0:
        temp = (a & b) << 1
        a = a ^ b
        b = temp

    return a


if __name__ == "__main__":
    a, b = 2, 3
    # a, b = -2, 19
    print("Input:", f"a: {a}", f"b: {b}")
    res = getSum(a=a, b=b)
    print("Output:", res)
