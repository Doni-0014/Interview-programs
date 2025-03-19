def is_armstrong_number(number):
    num_string = str(number)
    num_length = len(num_string)

    sum_of_digits = 0

    for digit in num_string:
        sum_of_digits += int(digit) ** num_length

    return sum_of_digits == number

user_input = int(input("Enter a number: "))

if is_armstrong_number(user_input):
    print(f"The number {user_input} is an armstrong number")

else:
    print(f"The number {user_input} is not an armstrong number")


#Convert the user_input integer to string
#Then find the length of that string to find the total numbers
#Initialize the sum_of_digits to 0
#Then iterate over the loop to find the sum of the squares of the numbers
#Return true if number is equal to the sum of the digits
