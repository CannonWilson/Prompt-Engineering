import random
import math
import copy

from data import AGE_DICT_GLOBAL, AGE_DICT_UNIFORM, AGE_DICT_US, \
    SEX_DICT_GLOBAL, SEX_DICT_UNIFORM, SEX_DICT_US, \
    RACE_DICT_US, RACE_DICT_GLOBAL, RACE_DICT_UNIFORM 

CHOSEN_AGE_DICT = AGE_DICT_GLOBAL
CHOSEN_SEX_DICT = SEX_DICT_UNIFORM
CHOSEN_RACE_DICT = RACE_DICT_GLOBAL

def random_weighted_key(input_dict):
    # Copy the input dict
    # Loop over the copy dict, replace vals with the summed vals up to that key
    # Pick a random value in the range of [0, sum)
    # Loop over the copy dict again, find the key where sum is in range
    #   [val for previous key, val for current key]
    modded_dict = copy.deepcopy(input_dict)
    sum = 0
    for key, val in list(modded_dict.items()):
        sum += val
        modded_dict[key] = sum

    random_num = random.uniform(0, sum)
    
    prev_value = 0
    for key, val in list(modded_dict.items()):
        if prev_value <= random_num <= val:
            return key
        prev_value = val
    return None


def generate_age_mod():
    random_key = random_weighted_key(CHOSEN_AGE_DICT)
    # random_key will be an age-range as a string like '5-14'
    min_age = int(random_key.split('-')[0])
    max_age = int(random_key.split('-')[-1])
    float_age = random.uniform(min_age, max_age)
    if float_age < 1:
        random_age = math.floor(float_age * 12)
        return f'{random_age} month old'
    else:
        random_age = round(float_age)
        return f'{random_age} year old'


def generate_sex_mod():
    random_sex = random_weighted_key(CHOSEN_SEX_DICT)
    return random_sex

def generate_race_mod():
    random_race = random_weighted_key(CHOSEN_RACE_DICT)
    return random_race

# Split on newlines to get list of lines
# Split on spaces to get list of lines with nested list of words for each line
# (Option 1) Add the diversity info in front of the word with curly braces
# (Option 2) Add the diversity info as a new sentence at the end of the current line
# Print out the diversified sentence

print("Please type or paste your desired input below. Wrap the words you want to diversify in {curly braces}. Hit enter and then Ctrl-D or Ctrl-Z (Windows) to save it.")
input_lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    input_lines.append(line)

# Maps words that were wrapped in curly braces into dicts containing line index and word index
diversify_dict = {}

for line_idx in range(len(input_lines)):
    words_list = input_lines[line_idx].split(" ")
    for word_idx, word in enumerate(words_list):
        if '{' in word:
            found_word = None
            for next_idx, next_word in enumerate(words_list[word_idx: -1]):
                if '}' in next_word:
                    found_word = next_word
            if found_word is None: 
                raise Exception('Could not find the closing curly brace on this line.')
            end_idx = words_list.index(found_word)
            found_phrase = " ".join(words_list[word_idx:end_idx+1])
            no_braces_phrase = found_phrase.replace("{", "").replace("}", "")
            new_dict = {
                no_braces_phrase: {
                    'line_idx': line_idx,
                    'word_idx': word_idx
                }
            }
            diversify_dict.update(new_dict)

    input_lines[line_idx] = words_list

# Loop through the words we found to modify and add modifications
for phrase in diversify_dict:
    age_mod = generate_age_mod()
    sex_mod = generate_sex_mod()
    race_mod = generate_race_mod()

    modded_str = f'{age_mod} {race_mod} {sex_mod} {phrase}'
    line_idx = diversify_dict[phrase]['line_idx']
    phrase_idx = diversify_dict[phrase]['word_idx']
    phrase_end_idx = phrase_idx + len(phrase.split(' '))

    input_lines[line_idx][phrase_idx:phrase_end_idx] = [modded_str]

# Flatten the input_lines list of lists to be one string
output_str = '\n'.join([" ".join(line) for line in input_lines])

print('output: ', output_str)

"""
The {police officer} is riding a motorcycle.
The {firefigher} is putting out a fire.
The {surgeon} is performing surgery.
The {construction worker} is building a building.
The {engineer} is looking at drawings.
The {priest} is preaching to a congregation.
The {soldier} is holding a rifle.
The {trucker} is inside a truck.
The {miner} is swinging a pickaxe.
The {nurse} is helping a patient.
The {secretary} is writing on a piece of paper.
The {teacher} is teaching a class.
The {hairstylist} is cutting someone's hair.
The {therapist} is talking to a client.
The {counselor} is sitting at a desk.
The {receptionist} is answering a phone.
The {designer} is drawing.
The {librarian} is reading a book.
The {rapper} is rapping into a microphone.
The {basketball player} is shooting a basketball.
The {farmer} is farming a plot of land.
The {veterinarian} is treating a sick dog.
The {pilot} is flying a plane.
The {CEO} is leading a meeting.
The {judge} is talking to a jury.
The {professor} is discussing with a colleague.
The {grocery store cashier} is checking out a customer.
The {retail sales associate} is helping a customer.
The {babysitter} is feeding a baby.
The {tutor} is instructing a student.
"""