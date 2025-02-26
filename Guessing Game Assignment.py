import random
hidden_num = random.randint(1, 1000)
low = 1
high = 1000
count = 10
#print(hidden_num)

while True:
    try:
        guess = int(input(f"Enter your guess number from range {low}-{high}: "))
    except ValueError:
        print("\033[31mAre you sure??? Please try again!\033[0m", "\n")
        continue

    if guess < low or guess > high:
        print("\033[31mAre you sure??? Please try again!\033[0m", "\n")
        continue


    if guess < hidden_num:
        count -= 1
        low = guess + 1
        print(f"oh oh! You guess the wrong number! Remain guess chances: {count}", "\n")

    elif guess > hidden_num:
        count -= 1
        high = guess - 1
        print(f"oh oh! You guess the wrong number! Remain guess chances: {count}", "\n")

    else:
        print(f"Yeah!!! The number is \033[36m{hidden_num}\033[0m. You guess \033[36m{11-count}\033[0m time(s).")
        break


    if count == 0:
        print("\033[31mYou Loose!!!!! \033[0m" f"The number is \033[31m{hidden_num}\033[0m.")
        break

