import random
import string


def generate_random_password(total):
    password = create_random_string(total)

    while is_repeating(password):
        password = create_random_string(total)

    return "".join(password)


def create_random_string(
    total, chars=string.ascii_letters + string.digits + string.punctuation
):
    # TODO

    return "not randomised yet"


def is_repeating(password):
    """ Check if there is any 2 characters repeating consecutively."""
    # TODO

    return False


if __name__ == "__main__":
    print(generate_random_password(random.randint(6, 30)))
