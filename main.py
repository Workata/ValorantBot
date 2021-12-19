"""
  TODO add docstring
  TODO (if needed) only specific user/users can add new maps/agents etc

  message.author -> Member
  member.name -> The user’s username.

  My user id: 501082895805448204
"""

import discord
import os
import crud
import errors
import messages
from prompt import PROMPT
from keep_alive import keep_alive
# import schedule
# import time
# from threading import Timer
from timer import Timer


TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


# ref: https://schedule.readthedocs.io/en/stable/examples.html#run-a-job-once
# async def remind_about_competitive(message):
#   # Do some work that only needs to happen once...
#   user_id = '501082895805448204'
#   await message.channel.send(f"<@{user_id}> competitive game is about to start!")
#   # cancel job
#   return schedule.CancelJob

async def remind_about_competitive(message):
  # Do some work that only needs to happen once...
  user_id = '501082895805448204'
  await message.channel.send(f"<@{user_id}> competitive game is about to start!")

# on message actions here!
@client.event
async def on_message(message):

  msg = message.content # get messgae content

  # ! dont analyze bot messages
  if message.author == client.user:
    return 

  
  # MAPS ACTIONS
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

  # AGENTS ACTIONS
  # add new valorant agent to the database
  if message.content.startswith(f'{PROMPT}add_agent'):
    # command format validation
    msg_split = msg.split()
    if len(msg_split) != 2:
      await message.channel.send(errors.ERROR_MSG_ADD_AGENT_FORMAT)
      return

    agent_to_add = msg_split[1]
    feedback = crud.add_agent(agent_to_add)
    await message.channel.send(feedback)

  # get current valorant agents
  if message.content.startswith(f'{PROMPT}get_agents'):
    # command format validation
    msg_split = msg.split()
    if len(msg_split) != 1:
      await message.channel.send(errors.ERROR_MSG_GET_AGENTS_FORMAT)
      return

    feedback = crud.get_agents()
    await message.channel.send(feedback)

  # delete valorant agent from the database
  if message.content.startswith(f'{PROMPT}delete_agent'):
    # command format validation
    msg_split = msg.split()
    if len(msg_split) != 2:
      await message.channel.send(errors.ERROR_MSG_DELETE_AGENT_FORMAT)
      return

    agent_to_delete = msg.split()[1]
    feedback = crud.delete_agent(agent_to_delete)
    await message.channel.send(feedback)

  
  # create competitive game time (hh:mm) person_1 person_2 etc
  if message.content.startswith(f'{PROMPT}create_competitive'):
    msg_split = msg.split()
    game_time = msg_split[1]
    feedback = crud.create_competitive(game_time)
    await message.channel.send(feedback)

  if message.content.startswith(f'{PROMPT}join_competitive'):
    user_username = message.author.name
    user_id = message.author.id
    msg_split = msg.split()
    game_time = msg_split[1]
    agent = msg_split[2]
    feedback = crud.join_competitive(user_username, user_id, game_time, agent)
    await message.channel.send(feedback)

  if message.content.startswith(f'{PROMPT}show_competitives'):
    feedback = crud.show_competitives()
    await message.channel.send(feedback)


  if message.content.startswith(f'{PROMPT}ping'):
    user_id = '501082895805448204'
    msg_split = msg.split()
    game_time = msg_split[1]
    # schedule.every().day.at(game_time).do(remind_about_competitive, message = message)
    await message.channel.send(f"Ok, will ping at {game_time}")

    # t = Timer(30.0, remind_about_competitive, args = [message])
    # t.start()
    timer = Timer(15, remind_about_competitive, message)

    # check scheduled jobs
    # while True:
    #   schedule.run_pending()
    #   time.sleep(1)
  

  # get info
  if message.content.startswith(f'{PROMPT}info'):
    await message.channel.send(messages.INFO_MSG)

  # get help
  if message.content.startswith(f'{PROMPT}help'):
    await message.channel.send(messages.HELP_MSG)


keep_alive()
client.run(TOKEN)
