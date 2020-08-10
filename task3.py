n = int(input())
# todo обработка исключения если на вход придет неверный тип данных (не целое или отрицательное число)
input_string = input()
string_list = list(input_string.split())
integer_list = []

for i in range(0, len(string_list)):  # переводим список строк в список int - не ясно из задания надо-ли
    integer_list.append(int(string_list[i]))

max_count = 1
max_count_num = integer_list[0]

for current_element in range(0, len(integer_list)):
    if integer_list.count(integer_list[current_element]) > max_count:
        max_count = integer_list.count(integer_list[current_element])
        max_count_num = integer_list[current_element]
print(max_count_num)
