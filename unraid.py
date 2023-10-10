import discord;
import datetime;
import asyncio
import docker
import discord
from discord.ext import tasks

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)


Server_ID = #server id bot will be in

docker_client = docker.from_env()



@tasks.loop(seconds = 10) 
async def myLoop():
    await client.change_presence(activity=discord.Game(name="Checking Containers"))
  
    Server_ID = #server id bot will be in
    server = client.get_guild(Server_ID)
    channel = discord.utils.get(server.channels, id=#channel id)
    await channel.purge()
    containers = docker_client.containers.list(all=True)
    x = datetime.datetime.now()
    embedVar = discord.Embed(title="UNRAID DOCKER BOT", description="Made by Joey", color=0x00ff00)

    embedVar.add_field(name="The Following Containers are Installed as of",value=f"{x}", inline=False)

    for container in containers:
        if "sonarr" in container.name and container.status == "running" :
            embedVar.add_field(name="Sonarr",value=f" {container.status} 🟢", inline=False)
        elif "sonarr" in container.name and container.status != "running" :
            embedVar.add_field(name="Sonarr",value=f"{container.status} 🔴", inline=False)
        if "radarr" in container.name and container.status == "running" :
            embedVar.add_field(name="Radarr",value=f" {container.status} 🟢", inline=False)
        elif "radarr" in container.name and container.status != "running" :
            embedVar.add_field(name="Radarr",value=f"{container.status} 🔴", inline=False)
        if "qbit" in container.name and container.status == "running" :
            embedVar.add_field(name="Qbitorent",value=f" {container.status} 🟢", inline=False)
        elif "qbit" in container.name and container.status != "running" :
            embedVar.add_field(name="Qbitorent",value=f"{container.status} 🔴", inline=False)
        if "immich" in container.name and container.status == "running" :
            embedVar.add_field(name="Immich",value=f" {container.status} 🟢", inline=False)
        elif "immich" in container.name and container.status != "running" :
            embedVar.add_field(name="Immich",value=f"{container.status} 🔴", inline=False)
        if "plex" in container.name and container.status == "running" :
            embedVar.add_field(name="Plex",value=f" {container.status} 🟢", inline=False)
        elif "plex" in container.name and container.status != "running" :
            embedVar.add_field(name="Plex",value=f"{container.status} 🔴", inline=False)
    
    await channel.send(embed=embedVar)
    
    await client.change_presence(activity=discord.Game(name="Done Checking Containers"))
    await asyncio.sleep(60) # task runs every 60 seconds


  

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    print('Bot is now running and will perform an action every 60 seconds.')
    myLoop.start()


                    
client.run('token')