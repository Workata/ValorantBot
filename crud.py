from replit import db

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

def delete_map(map_name):
  if "maps" not in db.keys():
    return "There are no maps declared!"
  else:
    current_maps = db["maps"]
    if map_name not in current_maps:
      return "This map is not listed within current maps!"
    current_maps.remove(map_name)
    return f"Map '{map_name}' has been successfully deleted!"

def add_agent():
  pass

def get_agent():
  return db.get("agents", None)

def delete_agent():
  pass