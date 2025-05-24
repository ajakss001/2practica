def combinationsum2(candidates, target):
    candidates.sort()
    results = []

    def backtrack(start, path, current_sum):
        if current_sum == target:
            results.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if current_sum + candidates[i] > target:
                break
            backtrack(i + 1, path + [candidates[i]], current_sum + candidates[i])

    backtrack(0, [], 0)
    return results

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationsum2(candidates, target))