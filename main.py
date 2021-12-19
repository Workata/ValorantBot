"""
  TODO add docstring
  TODO (if needed) only specific user/users can add new maps/agents etc

  message.author -> Member
  member.name -> The user’s username.

  Clear DB:
  from replit import db
  del db["competitives"]

"""

import discord
import os
import crud
import errors
import messages
from prompt import PROMPT
from keep_alive import keep_alive
from timer import Timer
from utils import get_time_dif


TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

async def remind_about_competitive(message, content):
  await message.channel.send(content)

# on message actions here!
@client.event
async def on_message(message):

  msg = message.content # get messgae content

  # ! dont analyze bot messages
  if message.author == client.user:
    return 

  
  # [MAPS]
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

  # [AGENTS]
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

    agent_to_delete = msg_split[1]
    feedback = crud.delete_agent(agent_to_delete)
    await message.channel.send(feedback)

  # [COMPETITIVES]
  # create competitive game time (hh:mm) person_1 person_2 etc
  if message.content.startswith(f'{PROMPT}create_competitive'):
    msg_split = msg.split()
    game_time = msg_split[1]
    feedback = crud.create_competitive(game_time)
    await message.channel.send(feedback)

  # join competitive game
  if message.content.startswith(f'{PROMPT}join_competitive'):
    """
      COMMAND: join_competitive <game_id> <agent>
    """
    # command format validation
    msg_split = msg.split()
    if len(msg_split) != 3:
      await message.channel.send(errors.ERROR_MSG_JOIN_COMPETITIVE_FORMAT)
      return

    user_username = message.author.name
    user_id = message.author.id
    msg_split = msg.split()
    game_id = msg_split[1]
    agent = msg_split[2]

    if agent not in crud.get_agents():
      await message.channel.send(errors.ERROR_MSG_WRONG_AGENT)
      return
      
    feedback = crud.join_competitive(user_username, user_id, game_id, agent)
    await message.channel.send(feedback)

  # show all competitives games
  if message.content.startswith(f'{PROMPT}show_competitives'):
    feedback = crud.show_competitives()
    await message.channel.send(feedback)

  # set reminder for competitive
  if message.content.startswith(f'{PROMPT}remind_competitive'):
    """
      COMMAND: remind_competitive <game_id> <minutes_before>
    """
    msg_split = msg.split()
    game_id = msg_split[1]
    minutes_before = msg_split[2]
    user_ids = crud.get_players_ids_in_competitive(game_id)
    competitive_time = crud.get_competitive_time(game_id)

    msg_content = ""
    for user_id in user_ids:
      msg_content += f"<@{user_id}> "
    msg_content += f" competitive game is about to start ({competitive_time})!"

    time_dif = get_time_dif(competitive_time)
    trigger_time = time_dif - int(minutes_before)
    if trigger_time <= 0:
      await message.channel.send("This doesn't make any sense!")
      return

    # Create async timer that will trigger reminder after 'X' seconds
    Timer(trigger_time*60, remind_about_competitive, message, msg_content) 

    await message.channel.send(
      f"Reminder will trigger {minutes_before} minutes before {competitive_time}.")

  
  # [OTHERS]
  # get info
  if message.content.startswith(f'{PROMPT}info'):
    await message.channel.send(messages.INFO_MSG)

  # get help
  if message.content.startswith(f'{PROMPT}help'):
    await message.channel.send(messages.HELP_MSG)


keep_alive()
client.run(TOKEN)
