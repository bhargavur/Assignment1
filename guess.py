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
    sD = stringDatabase.StringDatabase()
    word = sD.get_word()
    print(word)

    def update_string(string, idx, replace_with):
        return string[:idx] + replace_with + string[idx + 1:]

    bad_guesses = 0
    letter_request_counter = 0
    missed_letters = 0
    score = 0.0
    status = 'Success'
    while True:
        user_input = input('g = guess, t = tell me, l for a letter, and q to quit')
        if user_input == 'g':
            user_word = input('Enter your guess:')
            if user_word == word:
                print('true')
            else:
                print('false')
        elif user_input == 't':
            status = 'Gave up'
            print('The secret word is', word)
            break
        elif user_input == 'l':
            letter_request_counter = letter_request_counter + 1
            letter = input('Enter a letter:')
            occurrences = word.count(letter)
            print('You found ', occurrences, ' letters')
            if occurrences == 0:
                bad_guesses = bad_guesses + 1
                score = score * 0.9
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
                j = 0
                while j < 4:
                    if for_counting_blanks[j] == '-':
                        score = score + game.game.get_value(current_string[j])
                        print(current_string[j], game.game.get_value(current_string[j]))
                    j += 1
                game_obj = game.game(game_number, word, status, bad_guesses, missed_letters, score)
                print(game_obj.score, game_obj.status, game_obj. missed_letters)
                break
            else:
                continue
        elif user_input == 'q':
            status = 'Gave up'
            global quit_flag
            quit_flag = 1
            break
        else:
            print('Wrong input. Please enter the appropriate option.')
            continue
    if letter_request_counter != 0:
        score = score / letter_request_counter
    game_object = game.game(game_number, word, status, bad_guesses, missed_letters,  score)
    global list_of_game_objects
    list_of_game_objects.append(game_object)


while quit_flag == 0:
    play()
if quit_flag == 1:
    print('The game ended')
for obj in list_of_game_objects:
    print(obj.game_number, obj.word, obj.status, obj.bad_guesses, obj.missed_letters, obj.score)