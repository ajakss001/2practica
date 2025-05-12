def find_combinations(nums, target):
    nums.sort()
    combinations = []

    def find(start, current, remaining):
        if remaining == 0:
            combinations.append(current.copy())
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > remaining:
                break
            current.append(nums[i])
            find(i + 1, current, remaining - nums[i])
            current.pop()

    find(0, [], target)
    return combinations

print(find_combinations([2, 5, 2, 1, 2], 5))
print(find_combinations([10, 1, 2, 7, 6, 1, 5], 8))
