# Школа Python / Домашнее задание 1

ex1_question_array = ["Какая версия языка сейчас актуальна?", "Какая кодировка используется в строках?",
                      "Какой оператор сравнения нужно использовать для работы с None и bool?",
                      "Сколько значений есть у bool?", "Что будет есть случайно умножить None на число?",
                      "Чему равно len('abc')?", "Какой цикл чаще используется?",
                      "Можно ли назвать свою переменную False?", "Что будет результатом выражение 3 == 3.0?",
                      "Как форматировать строку?"]  # инициализируем список вопросов

ex1_answer_array = ["Python3", "UTF8", "is", 2, "Ошибка", 3,
                    "for", "Нет", "True", ".format"]  # инициализируем список ответов

ex1_user_input_array = []

ex1_correct_answers_count = 0  # инициализируем переменную для подсчета верных ответов

for i in range(0, len(ex1_question_array)):  # перебираем массив вопросов и выполняем необходимые действия
    ex1_user_input_array.append(input(ex1_question_array[i]))  # добавляем введенный ответ в список введенных ответов
    # преобразуем сравниваемые значения в строку все символы которой в нижнем регистре
    if str(ex1_answer_array[i]).lower() == str(ex1_user_input_array[i]).lower():
        print('Ответ "{}" верен'.format(ex1_user_input_array[i]))
        ex1_correct_answers_count += 1
    else:
        print('Неверный ответ')

print('Верных ответов {} из 10'.format(str(ex1_correct_answers_count)))