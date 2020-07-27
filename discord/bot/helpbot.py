import discord
import datetime, os
import asyncio
from discord.ext import commands
import nacl


client = discord.Client()
# app = commands.Bot(command_prefix="$")

# Bot アクセストークン
token = "NzI5NTc0OTI4MDY3NTkyMTky.XwK71g.lintONVPMZvgZY8mOyH2eTLIfus"
channel_id = 729573049292029975
voicechannel_id = 729573049292029976

dtime = datetime.datetime.now()
TODAY = dtime.today()
text_path = r'C:\Users\nicet\PycharmProjects\DC\memo_' + '{0:%Y%m%d}.txt'.format(TODAY)

@client.event
# 起動時に動作チェック
async def on_ready():
    print("ログインしました")
    print(client.user.name)
    print(client.user.id)
    print(dtime)
    print("===========")
    await boot_bot()

async def boot_bot():
    channel = client.get_channel(channel_id)
    await channel.send('おはよう！')

@client.event
async def on_message(message):
    today = datetime.datetime.now()

    if message.author.bot:
        return None

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

    if message.content.startswith('！おしえて'):
        if os.path.isfile(text_path):
            file = open(text_path, "r", encoding='utf-8')
            text_read = file.readlines()
            for read in text_read:
                await message.channel.send(read)
            file.close()
            print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + " memo output!")

    if message.content.startswith('！けして'):
        if os.path.isfile(text_path):
            file = open(text_path, "w", encoding='utf-8')
            file.close()
            print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + " memo delete!")
        else:
            pass
        await message.channel.send('初期化した！')

    if message.content.startswith('！はいって'):
        channel = message.author.voice.channel
        global vc

        print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + "connect voice channel!")
        vc = await discord.VoiceChannel.connect(channel)
        await message.channel.send('入った！')

        # if not discord.VoiceChannel.connect(channel):
        #     print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + "connect voice channel!")
        #     vc = await discord.VoiceChannel.connect(channel)
        # else:
        #     await message.channel.send('既に入ってます。')

    # if message.content.startswith('！でて'):
    #     channel = message.author.voice.channel
    #     if not discord.VoiceClient.is_connected(channel):
    #         print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + "disconnect voice channel!")
    #     vc = discord.VoiceChannel.connect(message.author.voice.channel)
    #     await vc.disconnect()


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

        print('{0:%Y-%m-%d %H:%M:%S}'.format(today) + " help view")
        await message.channel.send(embed=embed)

# @commands.command(name='！はいって', invoke_without_subcommand=True)
# async def join(ctx):
# #     if ctx.author.voice and ctx.author.voice.channel:
#     channel = ctx.author.voice.channel
#     discord.VoiceClient.move_to(voicechannel_id)
#     await channel.connect()
#         await channel.connect()
#     else:
#         await ctx.send("なし")
#
#
# @app.command(name="退室")
# async def leave(ctx):
#     await client.voice_clients[0].disconnect()

# Botの起動とDiscordサーバーへの接続
client.run(token)
