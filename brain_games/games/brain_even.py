from brain_games.game_logic import welcome_user, max_rounds
from brain_games.game_logic import min_num, max_num, prompt, congrats_win
from random import randint


def brain_event():
    correct_answer = 'yes'
    incorrect_answer = 'no'
    name_user = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter_correct = 0
    while counter_correct < max_rounds:

        random_number = randint(min_num, max_num)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and answer == correct_answer:
            counter_correct += 1
            print('Correct!')
        elif random_number % 2 > 0 and answer == incorrect_answer:
            counter_correct += 1
            print('Correct')
        elif random_number % 2 == 0 and answer == incorrect_answer:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.'
                  f'\nLet\'s try again, {name_user}!')
            break
        else:
            print(f'{answer} is wrong answer ;(.'
                  f' Correct answer was {incorrect_answer}.'
                  f'\nLet\'s try again, {name_user}!')
            break

    if counter_correct == max_rounds:
        return congrats_win(name_user)
