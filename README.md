# zKillreporter

[zKillboard](https://zkillboard.com/)から任意の情報をDiscordのWebhookで流すツール。

汎用性高いコード書こうと思ったけどめんどくさいからまた今度で。

## Requirements

- Python 3.6 over
- pip 9.0.1 over
- MongoDB 3.4.9 over

## Instllation

```
clone git@github.com:koluku/zkillreporter.git
cd zkillreporter
pip install -r requirements.txt
```

その後に`settings.sample.py`をsettings.pyに名前を変更し、ファイルを開いて必要事項を記入してください。

```
sudo service mongod start
python get-started.py
```

## Usage

手動実行

```
sudo service mongod start
python crawler.py
```

おすすめとしてはCronに`job.sh`を1時間おきに実行するようにするといいです。

```
echo '* */1 * * * sh zkillreporter/job.sh' > cron.conf
```

## LICENSE

- [MIT LICENSE](LICENSE)

## Author

- koluku
