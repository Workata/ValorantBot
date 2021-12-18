"""
  TODO add docstring
  TODO (if needed) only specific user/users can add new maps/agents etc
"""

import discord
import os
import crud
import errors
import messages
from prompt import PROMPT

TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

# on message actions here!
@client.event
async def on_message(message):

  msg = message.content # get messgae content

  # ! dont analyze bot messages
  if message.author == client.user:
    return 
  
  # add new valorant map to the database
  if message.content.startswith(f'{PROMPT}add_map'):
    # command format validation
    msg_split = msg.split()
    if len(msg_split) != 2:
      await message.channel.send(errors.ERROR_MSG_ADD_MAP_FORMAT)
      return

    map_to_add = msg_split[1]
    feedback = crud.add_map(map_to_add)
    await message.channel.send(feedback)

  # get current valorant maps
  if message.content.startswith(f'{PROMPT}get_maps'):
    # command format validation
    msg_split = msg.split()
    if len(msg_split) != 1:
      await message.channel.send(errors.ERROR_MSG_GET_MAPS_FORMAT)
      return

    feedback = crud.get_maps()
    await message.channel.send(feedback)

  # delete valorant map from the database
  if message.content.startswith(f'{PROMPT}delete_map'):
    # command format validation
    msg_split = msg.split()
    if len(msg_split) != 2:
      await message.channel.send(errors.ERROR_MSG_DELETE_MAP_FORMAT)
      return

    map_to_delete = msg.split()[1]
    feedback = crud.delete_map(map_to_delete)
    await message.channel.send(feedback)

  # get info
  if message.content.startswith(f'{PROMPT}info'):
    await message.channel.send(messages.INFO_MSG)

  # get help
  if message.content.startswith(f'{PROMPT}help'):
    await message.channel.send(messages.HELP_MSG)

client.run(TOKEN)

