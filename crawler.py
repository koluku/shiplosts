# Modules
import requests
from pymongo import MongoClient

# User modules
import settings
import notification

def connect_db(server = settings.MONGODB_SERVER, port = settings.MONGODB_PORT):
  client = MongoClient(server, port)
  database = client[settings.MONGODB_DATABASE]
  collection = database[settings.MONGODB_COLLECTION]
  return collection

def main():
  # MongoDB Collection
  co = connect_db()

  r = requests.get(settings.ZKILLBOARD_API_URL)
  data = r.json()

  for item in data:
    data_exist = co.find_one({'killID': item['killID']})

    if not data_exist:
      co.insert_one(item)

      if notification.is_target(item):
        notification.post_to_discord(item)

if __name__ == '__main__':
  main()
