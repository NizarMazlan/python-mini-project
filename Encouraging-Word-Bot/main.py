import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

#our token from an env file
my_secret = os.environ['TOKEN']

#create instance of a client, connection to discord
client = discord.Client()

#sad list
sad_words = ["sad" ,"depressed", "unhappy", "angry", "miserable", "depressing", "frustrated", "crying", "lost", "stressed", "not okay"]

#list of encouraging message
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person"
]

#new key in the database, check if responding is in the database
if "responding" not in db.keys():
  db["responding"] = True

#add helper function, return a quote from an API, return a quote
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']
  return(quote)


#update/add encouraging_message
def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]


#delete encouraging message
def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    #save into the database
    db["encouragements"] = encouragements


#use client.event to register an event
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


#if it senses a message in a discord server
@client.event
async def on_message(message):

  msg = message.content

  #check if the message is from ourselves, if the message if from bot
  if message.author == client.user:
    return 

  #see if the message starts with a command that have been sent to our discord bot
  if msg.startswith('$yoo'):
    await message.channel.send('Yo ssup')

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    option = starter_encouragements
    if "encouragements" in db.keys():
      option = option + list(db["encouragements"])

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(option))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ", 1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message is added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = list(db["encouragements"])
    await message.channel.send(encouragements)

  if msg.startswith("$commands"):
    await message.channel.send("$yoo - Saying hye to the bot\n$list - list out the encouraging words\n$new - add encouraging words\n$del - delete an encouraging word\n$inspire - send a quote\n$responding - to turn on and off the bot with true or false")

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]
  
    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

#keeping the bot alive using a web server
keep_alive()
#run the bot
client.run(my_secret)

