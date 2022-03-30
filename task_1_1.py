# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
duration = int(input('Введите размер отрезка времени в секундах: '))
#Дни
duration_days = duration // (3600 * 24)
#Часы
duration_hour = (duration % (3600 * 24)) // 3600
#Минуты
duration_min = ((duration % (3600 * 24)) % 3600) // 60
#Секунды
duration_sec = duration % 60
#решение задания
if (duration_days or duration_hour or duration_min) == 0:
    print(f'В введённом отрезке времени: {duration_sec} сек.')
elif (duration_days or duration_hour) == 0:
    print(f'В введённом отрезке времени: {duration_min} мин., {duration_sec} сек.')
elif duration_days == 0:
    print(f'В введённом отрезке времени: {duration_hour} ч., {duration_min} мин., {duration_sec} сек.')
else:
    print(f'В введённом отрезке времени: {duration_days} д., {duration_hour} ч., {duration_min} мин., {duration_sec} сек.')