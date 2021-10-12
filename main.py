import asyncio
import sys
import time
import nest_asyncio

from function import init, function_send_message, add_contact, random_sleep
from generator_number import generator_number_of_seconds_between_round
from myconfig import *

sys.setrecursionlimit(10000)
nest_asyncio.apply()


async def main():
    if bool_add_contact == True:
        for session in api_list:
            client = await init(session['api_id'], session['api_hash'], session['username'])
            await add_contact(session['username'], client)
            await client.disconnect()

    for i in range(0, 10):
        for session in api_list:
            client = await init(session['api_id'], session['api_hash'], session['username'])
            async with client:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(function_send_message(client, session['username']))
                await client.disconnect()
        random_sleep(generator_number_of_seconds_between_round())


if __name__ == '__main__':
    asyncio.run(main())
