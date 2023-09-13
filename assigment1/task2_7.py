word = input("Enter a word: ")
number = int(input("Enter a number: "))

for char in word:
    for _ in range(number):
        print(char * number)
