import discord
import asyncio
import requests
import json

client = discord.Client()
user = 'aXtKefZwLdTB2m6r'
key = 'yILcPtnpbLGlgAgXWYmRAVM0g59Xc1Lo'

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | '+str(len(client.servers))+' servers')
    await client.change_presence(game=discord.Game(name='chat with me!'))

@client.event
async def on_message(message):
       if not message.author.bot and (message.server == None or client.user in message.channel):

        await client.send_typing(message.channel)
        txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
        if r['status'] == 'success':
            await client.send_message(message.channel, r['response'] )

print('Starting...')
requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})
client.run('NDYxMTc0NDM3NjI3MTY2NzMx.DhPd5A.gG4Sexah48-Ztwkr0YlzlBxXB7M')
