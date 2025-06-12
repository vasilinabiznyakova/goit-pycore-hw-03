import random

def get_numbers_ticket(min, max, quantity):
    unique_numbers = []
    # validation
    if min < 1 or max > 1000 or quantity >= (max - min + 1):
        return unique_numbers
    else:
        numbers_list = range(min, max + 1)
        print(numbers_list)
        unique_numbers = random.sample(numbers_list, quantity)

        return sorted(unique_numbers)


result = get_numbers_ticket(2, 100, 10)
print(result)