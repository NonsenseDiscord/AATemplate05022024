# Packages!
import subprocess
# Install Python packages
python_packages = ['discord.py', 'flask']
for package in python_packages:
    subprocess.run(['pip', 'install', package])

from webserver import keep_alive
import discord

from config import message, channels, MPS, sessionId


active_times = [
    "10:13-22:59",  #There should be a printed "current time" text every time you run the code, use that to determine the active times (00:00-24:00 for 24/7 if you want, not recommended and will make you very detectable)
]

import time
import os

import logging
import threading

from discord.ext import commands
import asyncio
msg = message

import requests

import re

# main.py
import pytz

from datetime import datetime
# Function to parse time in HH:MM format
def parse_time(time_str):
    try:
        hour, minute = map(int, time_str.split(':'))
        return hour, minute
    except ValueError:
        return None

def is_active_time():
    # Get the current time in UTC
    utc_now = datetime.now(pytz.utc)

    # Specify the timezone you want to consider (e.g., 'US/Eastern')
    # Adjust this according to your desired timezone
    desired_timezone = pytz.timezone('US/Eastern')

    # Convert the current time to the desired timezone
    current_time = utc_now.astimezone(desired_timezone)

    # Get the current hour and minute
    current_hour = current_time.hour
    current_minute = current_time.minute

    # Check if the current time falls within any of the active time ranges
    for active_time_str in active_times:
        start_time_str, end_time_str = active_time_str.split('-')
        start_hour, start_minute = map(int, start_time_str.split(':'))
        end_hour, end_minute = map(int, end_time_str.split(':'))

        if (
            (start_hour < current_hour or (start_hour == current_hour and start_minute <= current_minute)) and
            (end_hour > current_hour or (end_hour == current_hour and end_minute >= current_minute))
        ):
            return True

    return False


if __name__ == "__main__":
    # Display the current hour and minute when the code is run
    utc_now = datetime.now(pytz.utc)
    current_time_eastern = utc_now.astimezone(pytz.timezone('US/Eastern'))
    formatted_time = current_time_eastern.strftime('%H:%M')
    print(f"Current time: {formatted_time}")





# Replace with your URL
url = 'http://ro04.pylex.me:10663/get-keys'

response = requests.get(url)
data = response.json()

def decode_variable(encoded_variable):
    char_map = {
        51: 'a', 72: 'b', 93: 'c', 114: 'd', 135: 'e', 156: 'f', 177: 'g', 198: 'h', 219: 'i', 240: 'j',
        261: 'k', 282: 'l', 303: 'm', 324: 'n', 345: 'o', 366: 'p', 387: 'q', 408: 'r', 429: 's', 450: 't',
        471: 'u', 492: 'v', 513: 'w', 534: 'x', 555: 'y', 576: 'z', 597: 'A', 618: 'B', 639: 'C', 660: 'D',
        681: 'E', 702: 'F', 723: 'G', 744: 'H', 765: 'I', 786: 'J', 807: 'K', 828: 'L', 849: 'M', 870: 'N',
        891: 'O', 912: 'P', 933: 'Q', 954: 'R', 975: 'S', 996: 'T', 1017: 'U', 1038: 'V', 1059: 'W', 1080: 'X',
        1101: 'Y', 1122: 'Z',
        1143: '!', 1264: '@', 1385: '#', 1506: '$', 1627: '%', 1748: '^', 1869: '&', 1990: '*',
        2111: '(', 2232: ')', 2353: '-', 2474: '_', 2595: '=', 2716: '+', 2837: '[', 2958: ']',
        3079: '{', 3200: '}', 3321: '|', 3442: '\\', 3563: ';', 3684: ':', 3805: '\'', 3926: '"',
        4047: ',', 4168: '.', 4289: '/', 4410: '<', 4531: '>', 4652: '?', 4773: '0', 4894: '1',
        5015: '2', 5136: '3', 5257: '4', 5378: '5', 5499: '6', 5620: '7', 5741: '8', 5862: '9'
    }
    if encoded_variable is not None and encoded_variable != "null":
        encoded_parts = encoded_variable.split('/')
        decoded_variable = []

        for part in encoded_parts:
            number = int(part)
            if number in char_map:
                decoded_variable.append(char_map[number])
        return ''.join(decoded_variable)
    else:
       return '0'

tokentest = decode_variable("4894/4773/5499/5741/5862/5499/5378/5741/5862/4894/5620/4773/5741/4773/5015/5499/5862/5378/4773/2353/849/996/681/4773/849/996/1017/4894/891/996/93/576/870/576/261/5015/849/660/849/5136/891/660/849/5015/891/597/4168/723/933/5620/324/450/2353/4168/93/5620/807/5741/408/51/219/2474/5741/534/51/765/408/5862/1038/576/240/702/156/345/5257/5499/534/156/975/450/1101/765/1059/2474/198/114/303/891/1101/366/786/5741")


# Session ID from the code
session_id_to_match = sessionId

token = '1'
maxchannels = '0'
length = '0'
startdate = '0'
daysremaining = '0'

from datetime import datetime



loggedin = False
for user_id, keys in data.items():
    for key_info in keys:
        # Decoding
        encoded_variable = key_info['generated_token']
        decoded_variable = decode_variable(encoded_variable)

        # Here, use the session ID from the URL response
        session_id = key_info['session_id']
        if session_id == session_id_to_match:
            # Store matched user's info as global variables    
            print("Logged into sessionId: " + session_id)
            loggedin = True
            global global_matched_user
            global global_matched_token
            global_matched_user = user_id
            token = decoded_variable
            maxchannels = int(key_info['maxchannels'])
            length = int(key_info['length'])
            startdate = datetime.strptime(key_info['start_date'], "%Y-%m-%d")
            expiration_date = key_info['expiration_date']

            if length == -1:
                print("Length: Infinite")
            else:
                print(f"Length: {length}")

            print(f"Max Channels: {maxchannels}")
            print(f"Start Date: {startdate}")
            print(f"Expiration Date: {expiration_date}")

            if expiration_date is not None:
                expiration_date = datetime.fromtimestamp(float(expiration_date) / 1000)
                days_remaining = (expiration_date - datetime.now()).days
                print(f"Days Remaining: {days_remaining}")

            break  # Stop searching after a match is found



if not loggedin:
  print('Incorrect session ID, try again (Or may not have token in)')





#channel = await client.fetch_channel(1090365527773417576)
#channel_2 = await client.fetch_channel(1063933664234307666)
#channel_3 = await client.fetch_channel(1063933664234307668)
#channel_4 = await client.fetch_channel(1063933664234307670)
#channel_5 = await client.fetch_channel(1090733200504008724)







#______________________________________________________________



try:
    import discum
except:
    import os
    os.system("pip install git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
    import discum

bot = "nil"

if token != '0':
    rtoken = token.split('-')
    if len(rtoken) > 1:
        bot = discum.Client(token=rtoken[1], log=False)
    elif len(rtoken) == 1:
        bot = discum.Client(token=rtoken[0], log=False)
    else:
        bot = "nil"





channelz = channels

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H")


async def task1():
    maxchannels_int = int(maxchannels)
    maxchannels_message_printed = False
    cutting_message_printed = False
    if bot == "nil":
        print("Invalid token, make sure to generate a token in the Discord server!")
    else:
        while True:
            if not is_active_time():
                print("It's not an active hour. Bot will wait.")
                await asyncio.sleep(60)  # Wait for a minute and check again
                continue  # Skip the rest of the loop and recheck if it's an active hour

            if maxchannels_int == 0 and not maxchannels_message_printed and loggedin:
                print("Your maxchannels is 0. Please contact an admin.")
                maxchannels_message_printed = True
            else:
                if len(channelz) > maxchannels_int:
                    if not cutting_message_printed and loggedin:
                        print("Cutting channels to", maxchannels_int)
                        cutting_message_printed = True
                    channels_to_send = list(channelz)[:maxchannels_int]
                else:
                    channels_to_send = channelz  # Use all available channels

                # Send messages to the selected channels
                for channel in channels_to_send:
                    # Your message sending logic here
                    bot.sendMessage(channel, msg)
                    print("Sent in " + channel)
                    await asyncio.sleep(MPS)
                # Your other logic here









async def myFunc():
  await asyncio.gather(task1())

keep_alive()
asyncio.run(myFunc())

