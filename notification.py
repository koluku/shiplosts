# Modules
import requests
from datetime import datetime, timedelta

# User Modules
import settings

def is_target(item):
  corpID = item['victim']['corporationID']
  allyID = item['victim']['allianceID']
  ssID = item['solarSystemID']
  if corpID in settings.CORPORATION_ID or allyID in settings.ALLIANCE_ID and ssID in settings.SOLARSYSTEM_ID:
    return True
  else:
    return False

def post_to_discord(item, webhook = settings.DISCORD_WEBHOOK_URL):
  eve_time = item['killTime']
  jp_time = datetime.strptime(eve_time, '%Y-%m-%d %H:%M:%S') + timedelta(hours=9)
  character = item['victim']['characterName']
  url = f'https://zkillboard.com/kill/{item["killID"]}'
  comment = f'犠牲者: {character} 日本時間: {jp_time} {url}'
  requests.post(webhook, data = json.dumps({'content': comment}), headers = {'Content-Type': 'application/json'})
