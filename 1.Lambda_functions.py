odd_or_even = lambda x : "Even" if x % 2 == 0 else "Odd"

input_number = int(input("Enter a number:"))
result = odd_or_even(input_number)

print(f"The number {input_number} is {result}")
