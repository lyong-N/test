# For Loop with Range

# for number in range(1, 20): # Note the last number is not printed [1-19]
#     print(number)

'''
if you want to print let say after every 3 numbers, use the below function
'''
# for number in range(1, 20, 3): # printing 1, 4, 7, 11 etc
#     print(number)


'''
Adding all the values b/w 1 and 100
'''

# total = 0
# for number in range (1, 101):
#     total += number
# print(total) # 5050


'''
Exercise 3 - Adding Even Numbers
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even 
number would be 2 and the last one is 100:i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
Important, there should only be 1 print statement in your console output. 
It should just print the final total and not every step of the calculation.
'''
# total = 0
# for even in range (2, 101, 2):
#     total += even
# print(total)
#
# # OR
#
# net = 0
# for number in range (1, 101):
#     if number %2 == 0:
#         net += number
# print(net)


'''
Exercise 4 - FizzBuzz

Instructions
You are going to write a program that automatically prints the solution to the FizzBuzz game.
Your program should print each number from 1 to 100 in turn.
When the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
