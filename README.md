# Send messages automatically on telegram
If you want to add users into your group, you need Telegram's accounts with some __authority__.  
This program allows you to passively increase it.  

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)  ![badge-telegram-program](https://github.com/pierre-vignoles/telegram_send_messages/blob/master/img/telegram-program.svg)

## Description
All of your accounts will send messages to each other. All of these specifications are made randomly to mimic organic use :
* The content of the messages
* The number of messages per account
* The time between each messages
* The recipient of the messages 

## To start
* You need multiple telegram's accounts.
* You need the api_id and the api_hash of your accounts. To do that, you have to create an api key here for each account : [Create your api key here](https://my.telegram.org/auth?to=apps)
* Install requirements - `pip install -r requirements.txt`

## Change settings
Some variables must be configured in order to make this program work in the file `myconfig.py`.  
* `api_list` : Enter the `api_id` and `api_hash` for each account
* `bool_add_contact` : Allows you to add each account as friend. If it's the first use of this program, set it to `True`.
* The others parameters is the minimum and maximum that you want for each case.

## Launch 
Execute the following command in a terminal : `python main.py`

## Heroku
You can add this program on HEROKU to let it work without interruption for free. The file `Procfile` is there for that.
