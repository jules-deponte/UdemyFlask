def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError('Denominator cannot be 0')

    return numerator / denominator

grades = [2, 5]

print('Average Grades Program')

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print('There are no grades yet')
else:
    print(f'The average grade is {average}')
finally:
    print('fin!')
