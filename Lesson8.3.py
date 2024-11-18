def find_unique_value():
    numbers = input("Введите список чисел (например: 1, 1, 2, 2, 3): ")
    numbers = [int(x.strip()) for x in numbers.split(',')]

    unique_count = sum(1 for number in numbers if numbers.count(number) == 1)

    if unique_count == len(numbers):
        print("Все числа в списке уникальны.")
        return None

    for number in numbers:
        if numbers.count(number) == 1:
            return number

print(find_unique_value())
