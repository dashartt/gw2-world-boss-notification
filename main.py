from discord.ext import tasks
from time_handler.main import get_time, addition_n_minutes
from data.main import load_world_boss_data
from message.main import message_world_boss_alert
import discord
import os
from dotenv import load_dotenv

ALERT_N_MINUTES_BEFORE_WORLD_BOSS_SPAWN = 10
CHECK_BOSS_WORLD_EVERY_N_MINUTES = 1
EMPTY_LIST = 0


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.users_notification = list()

    async def on_ready(self):
        print(f'[on] GW2 Bot')        
        self.activate_alert.start()

    async def on_message(self, message):        
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$start'):
            user = message.author

            if not user in self.users_notification:
                self.users_notification.append(user)
                embed_card=discord.Embed(title = '[on] World Boss notification!', color=0x29bd00)                
                embed_card.set_footer(text="You will get the alerts")
                await user.send(embed= embed_card)                
        
        if message.content.startswith('$stop'):
            user = message.author

            if user in self.users_notification:
                self.users_notification.remove(user)                
                embed_card=discord.Embed(title = '[off] World Boss notification!',color=0xc00c0c)                
                embed_card.set_footer(text="You will not receive the alerts")
                await user.send(embed=embed_card)

    @tasks.loop(minutes=CHECK_BOSS_WORLD_EVERY_N_MINUTES)      
    async def activate_alert(self):        
        world_boss_time = addition_n_minutes(get_time(), ALERT_N_MINUTES_BEFORE_WORLD_BOSS_SPAWN)
        world_boss_data = load_world_boss_data()
        
        try:
            avaliable_world_boss = world_boss_data[world_boss_time]
                    
            if len(self.users_notification) != EMPTY_LIST:
                for member in self.users_notification:                              
                    for world_boss in avaliable_world_boss:
                        embed_card = discord.Embed(title=world_boss['name'])                                                 
                        embed_card.set_thumbnail(url='https://media.discordapp.net/attachments/933408739480961086/1035643643840712704/NO8hnUi.jpg?width=960&height=540')
                        embed_card.add_field(name='Starts at', value=world_boss['start_time'], inline=False)
                        embed_card.add_field(name='Waypoint link', value=world_boss['waypoint_link'], inline=False)
                        embed_card.add_field(name='Zone', value=world_boss['zone'], inline=False)
                        embed_card.add_field(name='Area', value=world_boss['area'], inline=False)        
                        # embed_card.set_image(url="https://media.discordapp.net/attachments/933408739480961086/1035643643840712704/NO8hnUi.jpg?width=960&height=540")                        

                        await member.send(embed=embed_card)                        
        except Exception:
            pass
                

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = MyClient(intents=intents)

client.run(os.environ['BOT_TOKEN'])