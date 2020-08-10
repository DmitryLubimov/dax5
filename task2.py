triangle_height: int = int(input())
# todo обработка исключения если на вход придет неверный тип данных (не целое или отрицательное число)

max_string_length = len(str(triangle_height) * triangle_height)

for current_line in range(1, triangle_height+1):
    whitespace_string = ((max_string_length - current_line * len(str(current_line))) * " ")
    print(whitespace_string + str(current_line)*current_line)
