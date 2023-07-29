List = list


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print("Input:", nums)
    res = productExceptSelf(nums=nums)
    print("Output:", res)
