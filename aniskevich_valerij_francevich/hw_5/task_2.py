# Напишите программу, которая перебирает последовательность от 1 до 100 Для чисел
# кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5
# печатать "Buzz". Для чисел которые кратны 3 и 5 надо печатать "FuzzBuzz". Иначе
# печатать число

for i in range(1, 101):
    if i % 15 == 0:
        print("FuzzBuzz")
        continue
    if i % 5 == 0:
        print("Buzz")
        continue
    if i % 3 == 0:
        print("Fuzz")
        continue
    print(i)