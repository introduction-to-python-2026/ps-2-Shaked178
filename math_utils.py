def find_max_number(num1, num2, num3):
    if num1 >= num2 and num2 >= num3:
      return num1
    if num2 >= num1 and num2 >= num3:
      return num2
    return num3

def find_mean(num1, num2, num3):
    n = 3
    sum_of_numbers = num1 + num2 + num3 
    mean = sum_of_numbers / n
    return mean

def find_mean_std(num1, num2, num3):
    n = 3
    mean = find_mean(num1, num2, num3)
    sum_of_squares = (num1 - mean) **2 + (num2 - mean) **2 + (num3 - mean) **2
    std = (sum_of_squares / n) **0.5
    return mean, std

