def counter(ii, nums):
    c = 0
    if ii > 0:
        c = counter(ii - 1, nums)
    if nums[ii] > 0:
        return c + nums[ii]
    else:
        return c


numbers = [1, 3, 5, 7, 9]
count = counter(len(numbers) - 1, numbers)
print(count)
