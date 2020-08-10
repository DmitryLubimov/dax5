sec = int(input())
# todo обработка исключения если на вход придет неверный тип данных (не целое или отрицательное число)

hours_count = 0
minutes_count = 0
seconds_count = 0

if sec < 60:
    seconds_count = sec
elif sec < 3600:
    minutes_count = sec // 60
    seconds_count = sec % 60
elif sec >= 3600:
    hours_count = sec // 3600
    minutes_count = sec % 3600 // 60
    if minutes_count < 1:
        seconds_count = sec % 3600
    else:
        seconds_count = (sec % 3600) % 60


def hours_count_str(hours):
    """на вход подаем Int количество часов, на выходе получаем строку для печати"""
    if hours == 0:
        hours_str = ""
    elif 11 <= hours <= 19:
        hours_str = str(hours) + " часов "
    elif int(str(hours)[-1]) == 0:
        hours_str = str(hours) + " часов "
    elif int(str(hours)[-1]) == 1:
        hours_str = str(hours) + " час "
    elif 2 <= int(str(hours)[-1]) <= 4:
        hours_str = str(hours) + " часа "
    elif 5 <= int(str(hours)[-1]) <= 9:
        hours_str = str(hours) + " часов "
    else:
        hours_str = ""
    return hours_str


def minutes_count_str(minutes):
    """на вход подаем Int количество минут, на выходе получаем строку для печати"""
    if minutes == 0:
        minutes_str = ""
    elif 11 <= minutes <= 19:
        minutes_str = str(minutes) + " минут "
    elif int(str(minutes)[-1]) == 0:
        minutes_str = str(minutes) + " минут "
    elif int(str(minutes)[-1]) == 1:
        minutes_str = str(minutes) + " минута "
    elif 2 <= int(str(minutes)[-1]) <= 4:
        minutes_str = str(minutes) + " минуты "
    elif 5 <= int(str(minutes)[-1]) <= 9:
        minutes_str = str(minutes) + " минут "
    else:
        minutes_str = ""
    return minutes_str


def seconds_count_str(seconds):
    """на вход подаем Int количество секунд, на выходе получаем строку для печати"""
    if seconds == 0:
        seconds_str = ""
    elif 11 <= seconds <= 19:
        seconds_str = str(seconds) + " секунд "
    elif int(str(seconds)[-1]) == 0:
        seconds_str = str(seconds) + " секунд "
    elif int(str(seconds)[-1]) == 1:
        seconds_str = str(seconds) + " секунда "
    elif 2 <= int(str(seconds)[-1]) <= 4:
        seconds_str = str(seconds) + " секунды "
    elif 5 <= int(str(seconds)[-1]) <= 9:
        seconds_str = str(seconds) + " секунд "
    else:
        seconds_str = ""
    return seconds_str


print(hours_count_str(hours_count), minutes_count_str(minutes_count), seconds_count_str(seconds_count), sep='')
