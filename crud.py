from replit import db

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
  if "competitives" in db.keys():
    current_competitives = db["competitives"]
    current_competitives.append({"time": time_string, "players": 
    {}})
  else:
    db["competitives"] = [{"time": time_string, "players": {}}]

  return f"New game has been created! Start at {time_string}."

def join_competitive(user_username, user_id, game_time, agent):
  if "competitives" not in db.keys():
    return "There are no competitives created yet!"
  
  for competitive in db["competitives"]:
    if competitive["time"] == game_time:
      players = competitive["players"]
      if len(players.keys()) >= 5:
        return f"There are no free slots for competitive at {game_time}!"
      else:
        players[user_id] = (user_username, agent)
        competitive["players"] = players
        return f"You ({user_username}) have been added to the competitive as {agent}!"

def get_players_string(players):
  if not players: # empty dict
    return "There are no players in this competitive yet."

  players_str = ""
  for user_id in players:
    player = players[user_id]
    username = player[0]
    agent = player[1]
    players_str += f"{username} ({agent}), "
  players_str = players_str[:-2]
  return players_str

# TODO show current competitives
def show_competitives():
  if "competitives" not in db.keys():
    return "There are no competitives created yet!"

  feedback = ""
  iterator = 1
  for competitive in db["competitives"]:
    time_string = competitive["time"]
    players_string = get_players_string(competitive["players"])
    feedback += f"{iterator}. {time_string}  {players_string}\n"
    iterator += 1
  return feedback



