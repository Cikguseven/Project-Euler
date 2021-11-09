import time

start = time.time()

import os

current_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\Additional files\\54_poker.txt', current_path)

poker_file = open(new_path, 'r')

raw_games = poker_file.read().splitlines()

p1_hands = []

p1_scores = [0 for i in range(1000)]

p2_hands = []

p2_scores = [0 for i in range(1000)]

p1_wins = p2_wins = 0

poker_games = []

value_replacement_dict = {84: '10', 74: '11', 81: '12', 75: '13', 65: '14'}

for lines in raw_games:
    formatted_lines = lines.translate(value_replacement_dict)
    poker_games.append(formatted_lines.split())

for rounds in poker_games:
    p1_hands.append(rounds[:5])
    p2_hands.append(rounds[5:])


def duplicate_checker(hand):
    list_of_values = []
    for cards in hand:
        if cards[0] == '1':
            list_of_values.append(int(cards[:2]))
        else:
            list_of_values.append(int(cards[0]))
    unique_values = set()
    duplicated_values = []
    for value in sorted(list_of_values):
        if value in unique_values:
            duplicated_values.append(value)
        else:
            unique_values.add(value)
    # High card
    if not duplicated_values:
        return int(zero_adder(max(unique_values))
                   + zero_adder(sorted(unique_values)[2]))
    non_duplicated_values = [
        value for value in list_of_values if value not in duplicated_values]
    # One pair
    if len(duplicated_values) == 1:
        return int('1' + zero_adder(duplicated_values[0])
                   + zero_adder(sorted(non_duplicated_values)[-1]))
    elif len(duplicated_values) == 2:
        # Two pair
        if duplicated_values[0] != duplicated_values[1]:
            return int('2' + zero_adder(sorted(duplicated_values)[1])
                       + zero_adder(sorted(duplicated_values)[0]))
        # Three of a kind
        else:
            return int('3' + zero_adder(duplicated_values[0])
                       + zero_adder(sorted(non_duplicated_values)[1]))
    # Full house
    elif sorted(duplicated_values)[0] != sorted(duplicated_values)[2]:
        return int('6' + zero_adder(sorted(list_of_values)[2]) + '00')
    # Four of a kind
    else:
        return int('7' + zero_adder(duplicated_values[0]) + '00')


def flush_checker(hand):
    suits = ''
    for cards in hand:
        suits += cards[-1]
    if len(set(suits)) == 1:
        return True


def highest_card(hand):
    list_of_values = []
    for cards in hand:
        if cards[0] == '1':
            list_of_values.append(int(cards[:2]))
        else:
            list_of_values.append(int(cards[0]))
    return zero_adder(max(list_of_values))


def straight_checker(hand):
    list_of_values = []
    for cards in hand:
        if cards[0] == '1':
            list_of_values.append(int(cards[:2]))
        else:
            list_of_values.append(int(cards[0]))
    return sorted(list_of_values) == list(range(min(list_of_values), max(
        list_of_values)+1))


def zero_adder(value):
    if value // 10 == 0:
        return '0' + str(value)
    else:
        return str(value)


for index, hand in enumerate(p1_hands):
    if flush_checker(hand):
        p1_scores[index] = int('5' + highest_card(hand) + '00')
    elif straight_checker(hand):
        p1_scores[index] = int(
            '4' + highest_card(hand) + '00')
    else:
        p1_scores[index] = duplicate_checker(hand)

for index, hand in enumerate(p2_hands):
    if flush_checker(hand):
        p2_scores[index] = int('5' + highest_card(hand) + '00')
    elif straight_checker(hand):
        p2_scores[index] = int(
            '4' + highest_card(hand) + '00')
    else:
        p2_scores[index] = duplicate_checker(hand)

for p1_score, p2_score in zip(p1_scores, p2_scores):
    if p1_score > p2_score:
        p1_wins += 1
    else:
        p2_wins += 1

print(p1_wins)

end = time.time()

# Executes in 0.0170 seconds
print(end - start)
