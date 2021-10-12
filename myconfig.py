from typing import List, Dict, Union

api_list: List[Dict[str, Union[str, int]]] = [
    {'api_id': 'enter_api_id', 'api_hash': 'enter_api_hash', 'username': 'enter_username'},
    {'api_id': 'enter_api_id', 'api_hash': 'enter_api_hash', 'username': 'enter_username'}
]

bool_add_contact: bool = False

min_number_of_seconds_between_each_message: int = 100
max_number_of_seconds_between_each_message: int = 1000

min_number_of_seconds_between_round: int = 500
max_number_of_seconds_between_round: int = 5000

min_number_of_seconds_between_each_message_of_the_same_person: int = 3
max_number_of_seconds_between_each_message_of_the_same_person: int = 30

min_number_message_per_user: int = 1
max_number_message_per_user: int = 5

min_number_words_by_message: int = 1
max_number_words_by_message: int = 10




