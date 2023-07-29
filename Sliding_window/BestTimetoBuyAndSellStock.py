def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    last_min = prices[0]
    res = 0

    for n in prices[1:]:
        last_min = min(last_min, n)
        res = max(res, n - last_min)

    return res


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Input:", prices)
    res = maxProfit(prices=prices)
    print("Output:", res)
