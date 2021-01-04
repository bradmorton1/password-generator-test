import random

LOWERCASE_CHARS = tuple(map(chr, range(ord('a'), ord('z')+1)))
UPPERCASE_CHARS = tuple(map(chr, range(ord('A'), ord('Z')+1)))
DIGITS = tuple(map(str, range(0, 10)))
SPECIALS = ('!', '@', '#', '$', '%', '^', '&', '*')

SEQUENCE = (LOWERCASE_CHARS,
            UPPERCASE_CHARS,
            DIGITS,
            SPECIALS,
            )

def generate_random_password(total, sequences):
    r = generate_random_number_for_each_sequence(total, len(sequences))

    password = []
    for (population, k) in zip(sequences, r):
        n = 0
        while n < k:
            position = random.randint(0, len(population)-1)
            password += population[position]
            n += 1
    random.shuffle(password)
    
    while is_repeating(password):
        random.shuffle(password)
        
    return ''.join(password)

def generate_random_number_for_each_sequence(total, sequence_number):
    """ Generate random sequence with numbers (greater than 0).
        The number of items equals to 'sequence_number' and
        the total number of items equals to 'total'
    """
    current_total = 0
    r = []
    for n in range(sequence_number-1, 0, -1):
        current = random.randint(1, total - current_total - n)
        current_total += current
        r.append(current)
    r.append(total - sum(r))
    random.shuffle(r)

    return r

def is_repeating(password):
    """ Check if there is any 2 characters repeating consecutively."""
    #TODO

    return False

if __name__ == '__main__':
    print(generate_random_password(random.randint(6, 30), SEQUENCE))