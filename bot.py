import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands

import gspread
'''from oauth2client.service_account import ServiceAccountCredentials'''
from google.oauth2.service_account import Credentials
import asyncio
import json
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()  


# Discord bot setup
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')
'''
intents = discord.Intents.default()  # Creates a default set of intents.
intents.message_content = True  # Enables the message content intent.

client = discord.Client(intents=intents)
'''
# Google Sheets setup
scope = ['https://www.googleapis.com/auth/spreadsheets',
               'https://www.googleapis.com/auth/drive']


'''creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

GOOGLE_CREDENTIALS_PATH = os.getenv('GOOGLE_CREDENTIALS_PATH')

if not GOOGLE_CREDENTIALS_PATH:
    raise ValueError("GOOGLE_CREDENTIALS_PATH is not set or is empty.")
    
print(f"GOOGLE_CREDENTIALS_PATH: {GOOGLE_CREDENTIALS_PATH}")

print(GOOGLE_CREDENTIALS_PATH, scope)
print(" ");
'''
print(os.getenv('GOOGLE_CREDENTIALS_PATH'));
current_directory = os.getcwd()+"\credentials.json";
print(current_directory)

try:
    credentials = Credentials.from_service_account_file(
        current_directory, scopes=scope
    )
except Exception as e:
    print(f"Failed to load credentials:>>>>>>>>> {e}")
    raise

spreadsheet_name = "OnboardingDoc"

client_gs = gspread.authorize(credentials)

'''
spreadsheet_list = client_gs.openall()

print(len(spreadsheet_list))

for sheet in spreadsheet_list:
        print(sheet.title)
        print(">>")
'''
sheetDet = client_gs.open("OnboardingDoc").sheet1
print(sheetDet.title)

'''
responses = sheetDet.get_all_records()
for response in responses:
    uname = response['Name']
    user_id = response['Email'] 
    address = response['Address']
    phoneno = response['Phone number']
    comments = response['Comments']
    print(uname)
    print(user_id)
    print(address)
    print(phoneno)
    print(comments)
'''
    
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "!", intents=intents)

try:
   print("====")
   print(bot.user)
   print("====")
except Exception as e:
    print(f"Failed to get bot user:>>>>>>>>> {e}")
    raise

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel is not None:
        responses = sheetDet.get_all_records()
        for response in responses:
            uname = response['Name']
            user_id = response['Email'] 
            address = response['Address']
            phoneno = response['Phone number']
            comments = response['Comments']
            isCompleted = response['post complete']
            print(uname)
            print(user_id)
            print(address)
            print(phoneno)
            print(comments)
            
            if(isCompleted == 'Y' or isCompleted == 'y'):
                print("completed")
            else:
                print("Not completed")
                
           # await channel.send(f"User {user_id} has filled the form.")
            
        for guild in bot.guilds:
            for member in guild.members:
                print(member)
                
           #await channel.send("Hello, this is a test message!")
    else:
        print("Channel not found.")

@bot.event
async def on_disconnect():
    print('Bot disconnected!')
    
@bot.event
async def on_resumed():
    print('Bot reconnected!')

'''
async def check_form_responses():
    print("in check_form_responses")
    await bot.wait_until_ready()
    try:
        channel = bot.get_channel(DISCORD_CHANNEL_ID)  # Replace with your channel ID
    except Exception as e:
        print(f"Failed to connect channel:>>>>>>>>> {e}")
        raise
        
   
    print(bot.is_closed())
    while not bot.is_closed():
        responses = sheetDet.get_all_records()
        for response in responses:
            uname = response['Name']
            user_id = response['Email'] 
            address = response['Address']
            phoneno = response['Phone number']
            comments = response['Comments']
            print(uname)
            print(user_id)
            print(address)
            print(phoneno)
            print(comments)
            # Adjust based on your form field
            # Check if the user has already been notified (to avoid spamming)
            # You can add logic here to track notified users
            await channel.send(f"User {user_id} has filled the form.")
        await asyncio.sleep(3600)  # Check every hour

bot.loop.create_task(check_form_responses())
'''
bot.run(DISCORD_TOKEN)

