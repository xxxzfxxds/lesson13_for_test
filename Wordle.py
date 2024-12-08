import random

words_list = ["груша", "вишня", "банан", "слива", "арбуз", ]

secret = random.choice(words_list)


print(secret)

while True:
    yor_word = input("Ведите слово из 5 букв: ")
    if len(yor_word)!=5:
        print("Слово должно состоять из 5 букв!")
    else:
        break

yor_word_spisok = []
secret_spisok = []

for c in yor_word:
    yor_word_spisok.append(c)

for i in secret:
    secret_spisok.append(i)

if yor_word_spisok[0] == secret_spisok[0]:
    print(yor_word_spisok[0].upper())
    if yor_word_spisok[1] == secret_spisok[1]:
        print(yor_word_spisok[1].upper())
        if yor_word_spisok[2] == secret_spisok[2]:
            print(yor_word_spisok[2].upper())
            if yor_word_spisok[3] == secret_spisok[3]:
                print(yor_word_spisok[3].upper())
                if yor_word_spisok[4] == secret_spisok[4]:
                    print(yor_word_spisok[4].upper())
                    if 0==1:
                        print(1)
                    else:
                        breakpoint()
else:
    print("_")
if yor_word_spisok[1] == secret_spisok[1]:
    print(yor_word_spisok[1].upper())
    if yor_word_spisok[2] == secret_spisok[2]:
        print(yor_word_spisok[2].upper())
        if yor_word_spisok[3] == secret_spisok[3]:
            print(yor_word_spisok[3].upper())
            if yor_word_spisok[4] == secret_spisok[4]:
                print(yor_word_spisok[4].upper())
                if 0 == 1:
                    print(1)
                else:
                    breakpoint()
else:
    print("_")
if yor_word_spisok[2] == secret_spisok[2]:
    print(yor_word_spisok[2].upper())
    if yor_word_spisok[3] == secret_spisok[3]:
        print(yor_word_spisok[3].upper())
        if yor_word_spisok[4] == secret_spisok[4]:
            print(yor_word_spisok[4].upper())
            if 0 == 1:
                print(1)
            else:
                breakpoint()
else:
    print("_")
if yor_word_spisok[3] == secret_spisok[3]:
    print(yor_word_spisok[3].upper())
    if yor_word_spisok[4] == secret_spisok[4]:
        print(yor_word_spisok[4].upper())
        if 0 == 1:
            print(1)
        else:
            breakpoint()
else:
    print("_")
if yor_word_spisok[4] == secret_spisok[4]:
    print(yor_word_spisok[4].upper())
else:
    print("_")
