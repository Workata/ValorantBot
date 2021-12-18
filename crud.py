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