from prompt import PROMPT

HELP_MSG = f""" Available commands:
[MAPS]
{PROMPT}add_map <map_name> - adds new map to the database
{PROMPT}delete_map <map_name> - deletes map from the database
{PROMPT}get_maps - shows current maps in the database

[OTHERS]
{PROMPT}info - shows more details about this bot
{PROMPT}help - shows this message
"""

INFO_MSG = f""" Author: Workata
Soruce code: <insert_link_to_github_here>
License: MIT
"""