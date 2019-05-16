class game:
    def __init__(self, game_number, word, ststus, bad_guesses, missed_letters, score):
        self.game_number = game_number
        self.word = word
        self.status = ststus
        self.bad_guesses = bad_guesses
        self.missed_letters = missed_letters
        self.score = score

    @classmethod
    def get_value(cls, letter):
        if letter == 'a':
            return 8.17
        elif letter == 'b':
            return 1.49
        elif letter == 'c':
            return 2.78
        elif letter == 'd':
            return 4.25
        elif letter == 'e':
            return 12.70
        elif letter == 'f':
            return 2.23
        elif letter == 'g':
            return 2.02
        elif letter == 'h':
            return 6.09
        elif letter == 'i':
            return 6.97
        elif letter == 'j':
            return 0.15
        elif letter == 'k':
            return 0.77
        elif letter == 'l':
            return 4.03
        elif letter == 'm':
            return 2.41
        elif letter == 'n':
            return 6.75
        elif letter == 'o':
            return 7.51
        elif letter == 'p':
            return 1.93
        elif letter == 'q':
            return 0.10
        elif letter == 'r':
            return 5.99
        elif letter == 's':
            return 6.33
        elif letter == 't':
            return 9.06
        elif letter == 'u':
            return 2.76
        elif letter == 'v':
            return 0.98
        elif letter == 'w':
            return 2.36
        elif letter == 'x':
            return 0.15
        elif letter == 'y':
            return 1.97
        elif letter == 'z':
            return 0.07
        else:
            return 0.0