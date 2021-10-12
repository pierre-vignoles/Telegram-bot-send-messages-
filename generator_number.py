from random import randint

from myconfig import min_number_of_seconds_between_each_message, max_number_of_seconds_between_each_message, \
    min_number_of_seconds_between_round, max_number_of_seconds_between_round, \
    min_number_of_seconds_between_each_message_of_the_same_person, \
    max_number_of_seconds_between_each_message_of_the_same_person, min_number_message_per_user, \
    max_number_message_per_user, min_number_words_by_message, max_number_words_by_message


def generator_number_of_seconds_between_each_message() -> int:
    number_of_seconds_between_each_message = randint(min_number_of_seconds_between_each_message,
                                                     max_number_of_seconds_between_each_message)
    return number_of_seconds_between_each_message


def generator_number_of_seconds_between_round() -> int:
    number_of_seconds_between_round = randint(min_number_of_seconds_between_round, max_number_of_seconds_between_round)
    return number_of_seconds_between_round


def generator_number_of_seconds_between_each_message_of_the_same_person() -> int:
    number_of_seconds_between_each_message_of_the_same_person: int = randint(
        min_number_of_seconds_between_each_message_of_the_same_person,
        max_number_of_seconds_between_each_message_of_the_same_person)
    return number_of_seconds_between_each_message_of_the_same_person


def generator_number_message_per_user() -> int:
    number_message_per_user = randint(min_number_message_per_user, max_number_message_per_user)
    return number_message_per_user


def generator_number_words_by_message() -> int:
    number_words_by_message = randint(min_number_words_by_message, max_number_words_by_message)
    return number_words_by_message
