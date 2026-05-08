n = int(input("Введите число: "))
def fizz_buzz(n):
     for i in range(1, n + 1):
      if i % 3 == 0:
       print(f"{i} Fizz")
     if i % 5 == 0:
      print(f"{i} Buzz")
     if i % 3 == 0 and i % 5 == 0:
         print(f"{i} fizzBuzz")
     else:
       print(i)
fizz_buzz(n)
