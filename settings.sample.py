# zkillboard.comの一覧ページに/api/を加えることでJSON出力のAPIのURLが得られます
# 例: Goonswarm Federation https://zkillboard.com/api/alliance/1354830081/
ZKILLBOARD_API_URL = ''

# Discordのサーバー設定のページからWebhookのページに移動して通知したいチャンネルを選び、Webhook URLを取得してください
DISCORD_WEBHOOK_URL = ''

# MongoDBのサーバーのドメインとポートを指定してください
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DATABASE = 'zkillreporter'
MONGODB_COLLECTION = 'yourhome'

# 通知したい対象を記入してください。現在ではコープ名もしくはアライアンス名のどちらかかつ、ソーラーシステム名でフィルターしています
# 条件式はis_target関数を変更してください
CORPORATION_ID = []
ALLIANCE_ID = []
SOLARSYSTEM_ID = []
