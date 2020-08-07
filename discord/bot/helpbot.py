import discord
import datetime, os
import asyncio
from discord.ext import commands
import nacl


client = discord.Client()
# app = commands.Bot(command_prefix="$")

# Bot アクセストークン
token = "mytoken"
channel_id = "mychannel"
voicechannel_id = "mychannel"
server_id = "mychannel"

dtime = datetime.datetime.now()
TODAY = dtime.today()
text_path = r'myfolder' + '{0:%Y%m%d}.txt'.format(TODAY)

@client.event
# 起動時に動作チェック
async def on_ready():
    print("ログインしました")
    print(client.user.name)
    print(client.user.id)
    print(dtime)
    print("===========")
    await boot_bot()

#Bot起動したら挨拶
async def boot_bot():
    channel = client.get_channel(channel_id)
    await channel.send('おはよう！')

#ボイスチャンネルにメンバーの入室・退室の通知
@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == server_id and (before.channel != after.channel):
        text_cannel = client.get_channel(channel_id)
        if before.channel is None:
            msg = f'{member.name} が {after.channel.name} に参加しました。'
            await text_cannel.send(msg)
        elif after.channel is None:
            msg = f'{member.name} が {before.channel.name} に参加しました。'
            await text_cannel.send(msg)


@client.event
async def on_message(message):
    today = datetime.datetime.now()

    # Botに対して返事しない
    if message.author.bot:
        return None

    # 時間をメモする
    if message.content.startswith('！めも') or message.content.startswith('！メモ'):
        if os.path.isfile(text_path):
            file = open(text_path, "a", encoding='utf-8')
            file.write(str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日 " + str(today.hour) + "時" + str(today.minute) + "分" + str(today.second) + "秒" + '\n')
            file.close()
            print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + " memo save!")
        else:
            file = open(text_path, "w", encoding='utf-8')
            file.write(str(today.year) + "年" + str(today.month) + "月" + str(today.day) + "日 " + str(today.hour) + "時" + str(today.minute) + "分" + str(today.second) + "秒" + '\n')
            file.close()
            print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + " memo save!")
        await message.channel.send('メモ完了！')

    # メモした時間をチャットチャンネルに流す
    if message.content.startswith('！おしえて'):
        if os.path.isfile(text_path):
            file = open(text_path, "r", encoding='utf-8')
            text_read = file.readlines()
            for read in text_read:
                await message.channel.send(read)
            file.close()
            print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + " memo output!")

    # メモの内容を消す
    if message.content.startswith('！けして'):
        if os.path.isfile(text_path):
            file = open(text_path, "w", encoding='utf-8')
            file.close()
            print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + " memo delete!")
        else:
            pass
        await message.channel.send('初期化した！')

    # メンバーがボイスチャンネルで使うとBotがボイスチャンネルに入ってくる
    if message.content.startswith('！はいって'):
        channel = message.author.voice.channel
        print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + "connect voice channel!")
        vc = await channel.connect()

    # Botがボイスチャンネルから出る
    elif message.content.startswith('！でて'):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + "disconnect voice channel!")
                await vc.disconnect()

    # テキストチャンネルのチャット履歴をクリアする
    if message.content.startswith('！くりあ') or message.content.startswith('！クリア'):
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('チャットクリア完了！')
        else:
            await message.channel.send('チャットクリア失敗')

    # サイコロを回す
    if message.content.startswith('！さいころ') or message.content.startswith('！サイコロ'):
        random_num = random.randrange(1, 7)
        print(random_num)

        if random_num == 1:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':one:'))
        if random_num == 2:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':two:'))
        if random_num == 3:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':three:'))
        if random_num == 4:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':fore:'))
        if random_num == 5:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':five:'))
        if random_num == 6:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':six:'))

    if message.content.startswith('！にゅーす') or message.content.startswith('！ニュース'):
        url = 'https://news.yahoo.co.jp/topics/top-picks'
        html = request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        embed = discord.Embed(
            title = '最新ニュース',
            description = 'YAHOOニュースのトピックス（主要）',
            color = discord.Color.orange()
        )
        # news_data1 = soup.find('div', class_='newsFeed')
        # news_data2 = news_data1.find('ul', class_='newsFeed_item')
        news_data = soup.find_all('li', class_='newsFeed_item')
        for data in news_data:
            news_url = data.find('a', class_='newsFeed_item_link')
            if news_url:
                news_href = news_url.get('href')
                news_title = data.find('div', class_='newsFeed_item_title')
                news_time = data.find('time', class_='newsFeed_item_date')
            else:
                pass

            embed.add_field(name=news_time.text, value='[%s](<%s>)' % (news_title.text, news_href), inline=False)
        print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + " Realtime news list")
        await message.channel.send(embed=embed)


    # ヘルプコマンドを表示する
    if message.content.startswith('！ヘルプ'):
        embed = discord.Embed(
            title = 'ヘルプコマンド',
            description = '各コマンドなのでチャットで書いたら返してくる',
            color = discord.Color.blue()
        )

        embed.set_footer(text = str(dtime.year) + "年" + str(dtime.month) + "月" + str(dtime.day) + "日 " + str(dtime.hour) + "時" + str(dtime.minute) + "分" + str(dtime.second) + "秒")
        embed.add_field(name='！めも', value="日付と時間をテキストファイルにメモする", inline=False)
        embed.add_field(name='！`けして`', value="当日のテキストファイル中身を削除する", inline=False)
        embed.add_field(name='！おしえて', value="本日メモした内容をチャットに流す", inline=False)
        embed.add_field(name='！はいって', value="ボイスチャンネルにBotを参加させる", inline=False)
        embed.add_field(name='！でて', value="ボイスチャンネルにいるBotが出ていく", inline=False)
        embed.add_field(name='！くりあ', value="テキストチャンネルのチャット履歴を削除する", inline=False)
        embed.add_field(name='！さいころ', value="1から6までの数字がランダムに出る", inline=False)
        embed.add_field(name='！にゅーす', value="最新ニュースを表示する", inline=False)

        print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + " help view")
        await message.channel.send(embed=embed)


# Botの起動とDiscordサーバーへの接続
client.run(token)
