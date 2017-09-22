# Modules
import requests

# User modules
import crawler
import settings

def main():
  # MongoDB Collection
  co = crawler.connect_db()

  r = requests.get(settings.ZKILLBOARD_API_URL)
  data = r.json()

  for item in data:
    data_exist = co.find_one({'killID': item['killID']})

    if not data_exist:
      co.insert_one(item)

if __name__ == '__main__':
  main()
