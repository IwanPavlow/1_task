
#Чтение с файла
def read_f(file):
    numbers = []
    with open(file, 'r') as file:
        for line in file:
            numbers += [int(num) for num in line.split()]
    return numbers
#Запись в файл
def write_f(file, list):
    with open(file, 'w') as f:
        for item in list:
            f.write(str(item) + ' ')

def sort_most_frequent(nums):
    # Создаем словарь для подсчета количества повторений чисел
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Находим максимальное количество повторений
    max_count = max(count_dict.values())

    # Фильтруем числа, которые встречаются максимальное число раз
    filtered_nums = [num for num in count_dict if count_dict[num] == max_count]

    # Сортируем полученный список по возрастанию
    sorted_nums = sorted(filtered_nums)

    return sorted_nums

numbers = read_f("f2.txt")
sorted_numbers = sort_most_frequent(numbers)

print(sorted_numbers)

write_f("res1.txt", sorted_numbers)
