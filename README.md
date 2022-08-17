# D&D-Dice-Rolling-Bot

## Description:
A simple discord bot that accepts a command of !dice and any combination of throw amounts and dice types
For example:
- !dice 4D12 >>> This will roll a 12 sided die 2 times and sum the results
- !dice 2D14:4D17 >>> This will roll a 14 sided die 2 times and a 17 sided die 4 times and sum the results
- !dice 2D14:4D17:+4 >>> This will roll a 14 sided die 2 times and a 17 sided die 4 times and sum the results, then + 4 to the summed result, you can use the "+, -, *, /" operators

![My Remote Image](https://i.imgur.com/oq9uLK0.png)

## Instructions:
- You will need to create a '.env' file in the root folder and add a variable called DISCORD_TOKEN = 'your bot token goes here'

## Required Modules:
- pip install -U discord.py
- pip install python-dotenv