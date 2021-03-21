import random


def win_list(opinion_list, user_choose_now):
    index = opinion_list.index(user_choose_now)
    temp = opinion_list[index + 1:] + opinion_list[:index]
    half = len(opinion_list) // 2
    win = temp[half:]
    return win


def lose_list(opinion_list, user_choose_now):
    index = opinion_list.index(user_choose_now)
    temp = opinion_list[index + 1:] + opinion_list[:index]
    half = len(opinion_list) // 2
    lose = temp[:half]
    return lose


def winning_list(opinion_list, user_choose_now):
    winning_opinion = []
    first_index = opinion_list.index(user_choose_now) + 1
    for i in range(len(opinion_list) // 2):
        winning_opinion.append(opinion_list[(first_index + i) % len(opinion_list)])
    return winning_opinion


def loosing_list(opinion_list, user_choose_now):
    loosing_opinion = []
    first_index = opinion_list.index(user_choose_now) - 1
    for i in range(len(opinion_list) // 2):
        loosing_opinion.append(opinion_list[(first_index - i) % len(opinion_list)])
    return loosing_opinion


file = open("rating.txt", 'r')
all_score = file.readlines()
file.close()
user_name = input("Enter your name: ").strip()
user_score = 0
for score_line in all_score:
    name, score = score_line.split(' ')
    if name == user_name:
        user_score = int(score)
        break
print(f"Hello, {user_name}")
options_list = input()
options_list = options_list.split(',')
if not options_list or len(options_list) == 1:
    options_list = ["rock", "paper", "scissors"]
print("Okay, let's start")
while 1:
    user_choose = input().strip()
    exit_command = "!exit"
    score_command = "!rating"
    if user_choose in options_list:
        random.seed()
        computer_choose = random.randrange(0, 5)
        if computer_choose == 1:
            # print(win_list(options_list, user_choose))
            print(f"Sorry, but the computer chose {random.choice(lose_list(options_list, user_choose))}")
        elif computer_choose == 2:
            user_score += 50
            print(f"There is a draw {user_choose}")
        else:
            user_score += 100
            # print(lose_list(options_list, user_choose))
            print(f"Well done. The computer chose {random.choice(win_list(options_list, user_choose))} and failed")

    elif user_choose == exit_command:
        print("Bye!")
        break
    elif user_choose == score_command:
        print(f"Your rating: {user_score}")
    else:
        print("Invalid input")
