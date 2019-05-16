import stringDatabase
import game

list_of_game_objects = []
game_number = 0
quit_flag = 0


def play():
    global game_number
    game_number = game_number + 1
    print('** The great guessing game **')
    current_string = '----'
    print('Current Guess: ' + current_string)
    sd = stringDatabase.StringDatabase()
    word = sd.get_word()
    print(word)
    word='bork'
    print(word)
    bad_guesses = 0
    letter_request_counter = 0
    letter_bad_request_counter = 0
    missed_letters = 0
    score = 0.0
    status = 'Success'
    while True:
        user_input = input('g = guess, t = tell me, l for a letter, and q to quit')
        if user_input == 'g':
            bad_guesses = bad_guesses + 1
            user_word = input('Enter your guess:')
            if user_word == word:
                score = calcTotal(current_string, word)
                print('You guessed it right')
                break
            else:
                print('Your guess is wrong')
        elif user_input == 't':
            status = 'Gave up'
            score = -1 * calcPenalty(current_string)
            missed_letters = current_string.count('-')
            print('The secret word is', word)
            print(score)
            break
        elif user_input == 'l':
            letter_request_counter = letter_request_counter + 1
            letter = input('Enter a letter:')
            occurrences = word.count(letter)
            print('You found ', occurrences, ' letters')
            if occurrences == 0:
                letter_bad_request_counter = letter_bad_request_counter+1
            for_counting_blanks = current_string
            print(for_counting_blanks)
            i = 0
            while i < 4:
                if word[i] == letter:
                    current_string = update_string(current_string, i, letter)
                i = i + 1
            print(current_string)
            if current_string == word:
                print('You got it!')
                missed_letters = for_counting_blanks.count('-')
                print(for_counting_blanks)
                score = calcTotal(for_counting_blanks, current_string)
                game_obj = game.game(game_number, word, status, bad_guesses, missed_letters, score)
                print(game_obj.score, game_obj.status, game_obj. missed_letters)
                break
            else:
                continue
        elif user_input == 'q':
            current_string = 'quit'
            global quit_flag
            quit_flag = 1
            break
        else:
            print('Wrong input. Please enter the appropriate option.')
            continue
    if current_string != 'quit':
        if letter_request_counter != 0 and score >= 0:
            score = score / letter_request_counter
            score = score * (1-letter_bad_request_counter*0.1)
        game_object = game.game(game_number, word, status, bad_guesses, missed_letters,  score)
        global list_of_game_objects
        list_of_game_objects.append(game_object)


def update_string(string, idx, replace_with):
    return string[:idx] + replace_with + string[idx + 1:]


def calcPenalty(current_string):
    i = 0
    total = 0
    while i < 4:
        if current_string[i] != '-':
            total = total + game.game.get_value(current_string[i])
        i += 1
    return total


def calcTotal(for_counting_blanks, current_string):
    i = 0
    total = 0
    while i < 4:
        if for_counting_blanks[i] == '-' and current_string[i] != '-':
            total = total + game.game.get_value(current_string[i])
        i += 1
    return total


while quit_flag == 0:
    play()
if quit_flag == 1:
    print('The game ended')
print('Game     Word    Status     Bad Guesses     Missed Letters      Score')
print('-----    ------  --------   -----------     ---------------     --------')
for obj in list_of_game_objects:
    print(obj.game_number, '      ', obj.word, '  ', obj.status, '  ',
          obj.bad_guesses, '             ', obj.missed_letters, '                 ', obj.score)