import uuid
import datetime
import pytz

def generate_id():
  """
    Generate short id for games.
    https://stackoverflow.com/questions/13484726/safe-enough-8-character-short-unique-random-string
  """
  return str(uuid.uuid4())[:8]

def get_time_dif(time_string):
  """
    time_string -> hh:mm
    Returns time difference between current time and given time.

    Ref
    1)
    https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python

    2)
    https://stackoverflow.com/questions/23642676/python-set-datetime-hour-to-be-a-specific-time
  """
  seconds_in_day = 24 * 60 * 60
  # tz = pytz.timezone('Poland')

  split_time = time_string.split(":")
  hours = int(split_time[0])
  minutes = int(split_time[1])

  # +1 hour cause timezones
  today = datetime.datetime.now() + datetime.timedelta(hours=1, minutes=0) 
  t = datetime.time(hour= hours, minute= minutes)
  combined_time = datetime.datetime.combine(today, t)
  difference = combined_time - today
  # it will return something like: (0, 8) # 0 minutes, 8 seconds
  difference_tuple = divmod(difference.days * seconds_in_day + difference.seconds, 60)
  return difference_tuple[0]


