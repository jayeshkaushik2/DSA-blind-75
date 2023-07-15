List = list


def threeSum(nums: List[int]) -> List[List[int]]:
    # time comp O(n.log(n) + n * n) space comp O(n*n)
    triplets = []
    n = len(nums)
    nums.sort()

    for i in range(n - 2):
        if i < 0 and nums[i] == nums[i - 1]:
            continue
        target = 0 - nums[i]
        l = i + 1
        r = n - 1

        while l < r:
            cur_sum = nums[l] + nums[r]

            if cur_sum == target:
                temp = [nums[i], nums[l], nums[r]]
                if temp not in triplets:
                    triplets.append([nums[i], nums[l], nums[r]])
                left = nums[l]

                # remove all duplicates from the left side
                while l < r and nums[l] == left:
                    l += 1

                right = nums[r]
                # remove all duplicates from the right side
                while l < r and nums[r] == right:
                    r -= 1

            elif cur_sum < target:
                l += 1
            else:
                r -= 1

    return triplets


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print("Input:", nums)
    res = threeSum(nums=nums)
    print("Output:", res)
