def find_max_number(num1, num2, num3):
    if num1 > num2 and num2 >num3:
      return num1
    if num2 > num1 and num2 > num3:
      return num2
    return num3

def find_mean(num1, num2, num3):
    n = 3
    sum_of_numbers = num1 + num2 + num3 
    mean = sum_of_numbers / n
    return mean

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    pass  # Replace 'pass' with code

