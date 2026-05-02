def month_to_season(month):
    if 12 >= month <= 2:
        return "Зима"
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    return "Такого нет"
month = int(input("Введите номер месяца: "))
print(month_to_season(month))
