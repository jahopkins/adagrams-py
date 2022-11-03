import random

def draw_letters():
    # create data structure to store letters

    letter_distribution = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

    # select a random letter 

    ten_rand_letters = []

    while len(ten_rand_letters) < 10:
        random_letter =random.choice(list(letter_distribution.keys()))

        if ten_rand_letters.count(random_letter) < letter_distribution[random_letter]:
            ten_rand_letters.append(random_letter)
    return ten_rand_letters
        



    #return array of 10 letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass