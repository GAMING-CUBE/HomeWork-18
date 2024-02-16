import random

sequence = "Yellow Pink Green Red Black White"

items = sequence.split()
random.shuffle(items)
shuffled_sequence = ' '.join(items)
print(shuffled_sequence)
