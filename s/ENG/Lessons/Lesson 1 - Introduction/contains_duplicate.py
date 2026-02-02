def contains_duplicate(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False


result = contains_duplicate([1, 2, 3, 1])
print(result)