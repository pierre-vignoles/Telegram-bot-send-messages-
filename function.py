import time
from random import randint, choice
from telethon.client.telegramclient import TelegramClient
from telethon.tl.functions.contacts import AddContactRequest

from generator_number import *
from myconfig import api_list


async def init(api_id: int, api_hash: str, username: str) -> TelegramClient:
    client = TelegramClient('sessions/{}'.format(str(api_id)), api_id, api_hash)
    await client.connect()
    print("\nSESSION : {}".format(username))
    return client


async def add_contact(username: str, client: TelegramClient):
    for user in api_list:
        if user['username'] == username:
            continue
        else:
            entity = await client.get_entity(user['username'])
            await client(AddContactRequest(
                id=entity.username,
                first_name=entity.first_name,
                last_name="None",
                phone=entity.phone
            ))
    print("Every contacts added")


def random_choice_username(username: str) -> str:
    random_username = choice(api_list)['username']
    if random_username == username:
        random_username = random_choice_username(username)
    return random_username


def random_sleep(function):
    number_of_seconds = function
    print("Sleep : {} seconds".format(number_of_seconds))
    time.sleep(number_of_seconds)


async def function_send_message(client: TelegramClient, username: str):
    list_words = ['apple', 'banana', 'cherry', 'dates', 'etc', 'have', 'I', 'You', 'good', 'morning', 'what',
                  'This', 'is', 'a', 'string', 'with', 'words', 'whirl', 'evacs', 'congestin', 'Arawak', 'drypoint',
                  'mutton-chop', 'organoborane', 'meticas', 'expatiate', 'rehearse', 'unblamableness', 'misplacement',
                  'coresidence', 'retroact', 'lipstick', 'brows', 'halobacterium', 'wagati', 'javelot', 'Osakan',
                  'bestowal', 'illuminati', 'encyclopedia', 'lilies', 'namedrop', 'fagot', 'incompetent', 'snell',
                  'internuncios', 'penetralium', 'hedge-warbler', 'spokes', 'woolsorter', 'absorbancy', 'anglophilia',
                  'magistrates', 'ring-brooch', 'knitting-sheath', 'crumple', 'Columella', 'schmoozer', 'oleographer',
                  'red-tapery', 'boils', 'mouselook', 'pibrochs', "bvd's", 'cajuput', 'interlanguage', 'tatle',
                  'druggist', 'argumentations', 'bryozoon', 'fratricides', 'progestins', 'wallcoverings', 'seedcase',
                  'hadrosaurs', 'dimities', 'persuade', 'thickhead', 'darger', 'carquenet', 'slayer', 'fire-chamber',
                  'teatime', 'bepotastine', 'occiputs', 'letters', 'undividedness', 'dabchick', 'sarcasm',
                  'stake-driver', 'zyzzyvas', 'rayat', 'tummer', 'amethopterin', 'interposition', 'infame', 'collation',
                  'boychildren', 'throne', 'decolonization', 'culchies', 'tranquilisers', 'tragédienne', 'research',
                  'clairvoyance', 'mobilize', 'pleading-place', 'leftenants', 'foresignify', 'Attis', 'attired',
                  'blood-stain', 'try-cock', 'frote', 'prolines', 'peachy', 'fire-roll', 'think', 'know', 'look', 'the',
                  'when', 'because', 'yes', 'no']

    sentence = []
    list_sentence = []
    random_number_message = generator_number_message_per_user()
    random_username = random_choice_username(username)
    for message in range(0, random_number_message):
        random_number_word = generator_number_words_by_message()
        for word in range(0, random_number_word):
            sentence.append(choice(list_words))
        list_sentence.append(" ".join(sentence))
        sentence = []
    entity = await client.get_entity(random_username)
    for message in range(0, random_number_message):
        await client.send_message(entity=entity, message=list_sentence[message])
        print("1 message sent to {}".format(random_username))
        random_sleep(generator_number_of_seconds_between_each_message_of_the_same_person())

    print("Total of {} messages sent to {}".format(random_number_message, random_username))

    random_sleep(generator_number_of_seconds_between_each_message())


