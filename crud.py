from replit import db
from utils import generate_id

# MAPS

def add_map(map_name: str):
  if "maps" in db.keys():
    current_maps = db["maps"]
    current_maps.append(map_name)
    db["maps"] = current_maps
  else:   # no maps in the db
    db["maps"] = [map_name] # create a list with a first map
  return f"New map '{map_name}' has been added to the database!"
  
def get_maps():
  if "maps" in db.keys():
    current_maps = db["maps"]
    return ', '.join(current_maps)
  else:   # no maps in the db
    return "There are no maps in the database!"

def delete_map(map_name: str):
  if "maps" not in db.keys():
    return "There are no maps declared!"
  else:
    current_maps = db["maps"]
    if map_name not in current_maps:
      return "This map is not listed within current maps!"
    current_maps.remove(map_name)
    return f"Map '{map_name}' has been successfully deleted!"

# AGENTS

def add_agent(agent_name: str):
  if "agents" in db.keys():
    current_agents = db["agents"]
    current_agents.append(agent_name)
    db["agents"] = current_agents
  else:   # no maps in the db
    db["agents"] = [agent_name] # create a list with a first map
  return f"New agent '{agent_name}' has been added to the database!"

def get_agents():
  if "agents" in db.keys():
    current_agents = db["agents"]
    return ', '.join(current_agents)
  else:   # no agents in the db
    return "There are no agents in the database!"

def delete_agent(agent_name: str):
  if "agents" not in db.keys():
    return "There are no agents declared!"
  else:
    current_agents = db["agents"]
    if agent_name not in current_agents:
      return "This agent is not listed within current agents!"
    current_agents.remove(agent_name)
    return f"Agent '{agent_name}' has been successfully deleted!"

# COMPETITIVES

def create_competitive(time_string: str):
  """
    time_string -> hh:mm
  """
  game_id = generate_id()
  if "competitives" in db.keys():
    current_competitives = db["competitives"]
    current_competitives.append({"id": game_id,"time": time_string, "players": {}})
  else:
    db["competitives"] = [{"id": game_id, "time": time_string, "players": {}}]

  return f"New game ({game_id}) has been created! Start at {time_string}."

def join_competitive(user_username: str, user_id: str, game_id: str, agent: str):
  if "competitives" not in db.keys():
    return "There are no competitives created yet!"
  
  for competitive in db["competitives"]:
    if competitive["id"] == game_id:
      players = competitive["players"]
      if len(players.keys()) >= 5:
        return f"There are no free slots for competitive '{game_id}'!"
      else:
        players[user_id] = (user_username, agent)
        competitive["players"] = players
        return f"You ({user_username}) have been added to the competitive as {agent}!"
  # no games with this ID
  return f"There are no competitives with id equall to '{game_id}'!"

def get_players_string(players):
  """
    Get players using formatted string: <username> (<agent>)...
  """
  if not players: # empty dict
    return "None"

  players_str = ""
  for user_id in players:
    player = players[user_id]
    username = player[0]
    agent = player[1]
    players_str += f"{username} ({agent}), "
  players_str = players_str[:-2]
  return players_str

# show current competitives
def show_competitives():
  if "competitives" not in db.keys():
    return "There are no competitives created yet!"

  feedback = ""
  for competitive in db["competitives"]:
    game_id = competitive["id"]
    time_string = competitive["time"]
    players_string = get_players_string(competitive["players"])
    feedback += f"ID: {game_id} | TIME: {time_string} | TEAM: {players_string}\n"
  return feedback


def get_players_ids_in_competitive(game_id):
  if "competitives" not in db.keys():
    return []

  user_ids = []
  for competitive in db["competitives"]:
    if game_id == competitive["id"]:
      for user_id in competitive["players"]:
        user_ids.append(user_id)
      break
  return user_ids

def get_competitive_time(game_id):
  if "competitives" not in db.keys():
    return "None"

  competitive_time = "None"
  for competitive in db["competitives"]:
    if game_id == competitive["id"]:
      competitive_time = competitive["time"]
      break
  return competitive_time


