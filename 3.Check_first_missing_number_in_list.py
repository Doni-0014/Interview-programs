def num(nums):
    expected = 1  # Start with 1, the first positive number

    for num in nums:
        if num == expected:
            expected += 1  # Increment expected if the number is found

    return expected  # Return the first missing number after checking the list


number_list = num([1, 2, 4])
print(number_list)
