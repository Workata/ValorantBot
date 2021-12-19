from prompt import PROMPT

HELP_MSG = f""" Available commands:
[MAPS]
{PROMPT}add_map <map_name> - adds new map to the database
{PROMPT}delete_map <map_name> - deletes map from the database
{PROMPT}get_maps - shows current maps in the database

[AGENTS]
{PROMPT}add_agent <agent_name> - adds new agent to the database
{PROMPT}delete_agent <agent_name> - deletes agent from the database
{PROMPT}get_agents - shows current agents in the database

[COMPETITIVES]
{PROMPT}create_competitive <game_time> - craete new competitive game at given time
{PROMPT}join_competitive <game_id> <agent_name> - join specific game with selected agent (type 'fill' if not selected)
{PROMPT}remind_competitive <game_id> <minutes_before> - set a reminder 'X' minutes before competitive will take place
{PROMPT}delete_competitive <game_id> - delete competitive

[CUSTOMS]
Work in progress

[OTHERS]
{PROMPT}info - shows more details about this bot
{PROMPT}help - shows this message
"""

INFO_MSG = f""" Author: Workata
Soruce code: https://github.com/Workata/ValorantBot
Version: 0.69.420
License: MIT
"""