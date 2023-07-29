List = list


def maxArea(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    max_water_contain = 0

    while l < r:
        breadth = min(height[l], height[r])
        length = r - l
        cur_water_contain = length * breadth
        max_water_contain = max(cur_water_contain, max_water_contain)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_water_contain


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Input:", height)
    res = maxArea(height=height)
    print("Output:", res)
