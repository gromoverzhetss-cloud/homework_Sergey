def is_year_leap(age):
    return True if age % 4 == 0 else False
nam = int(input("Год:"))
result = is_year_leap(nam)
print(f"Год {nam}: {result}")
