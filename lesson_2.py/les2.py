rate = input("Поставьте оценку от 1 до 5:")
rate = int(rate)

# проверить
if (rate < 1):
    rate = 1


if (rate > 5):
    rate = 5

print(rate)

feedback = ''

if rate == 1:
    feedback = input("что делать: ")
elif rate == 2:
    feedback = input("здесь что не так: ")
elif rate == 3:
    feedback = input("тут что: ")
elif rate == 4:
    feedback = input("здесь: ")
else:
    feedback = input("почему так: ")
print(feedback)