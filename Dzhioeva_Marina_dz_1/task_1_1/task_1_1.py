while(1):
    duration = int(input('Введите количество секунд: '))

    second = duration % 60
    minute = duration // 60

    hour = minute // 60
    minute = minute % 60

    day = hour // 24
    hour = hour % 24

    print(day, "дней", hour, "часов", minute, "минут", second, "секунд")