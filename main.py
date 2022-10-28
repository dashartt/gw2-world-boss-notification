from discord.ext import tasks
from time_handler.main import get_time, addition_n_minutes
from data.main import load_world_boss_data
from message.main import message_world_boss_alert
import discord


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
                await user.send('[on] World Boss notification!', mention_author=True)
        
        if message.content.startswith('$stop'):
            user = message.author

            if user in self.users_notification:
                self.users_notification.remove(user)                
                await user.send('[off] World Boss notification!', mention_author=True)

    @tasks.loop(minutes=CHECK_BOSS_WORLD_EVERY_N_MINUTES)  
    async def activate_alert(self):        
        world_boss_time = addition_n_minutes(get_time(), ALERT_N_MINUTES_BEFORE_WORLD_BOSS_SPAWN)
        world_boss_data = load_world_boss_data()
        
        try:
            avaliable_world_boss = world_boss_data[world_boss_time]
            message_alert = message_world_boss_alert(avaliable_world_boss)

            if len(self.users_notification) != EMPTY_LIST:
                for member in self.users_notification:                                
                    await member.send(message_alert)  
        except Exception:
            pass
 

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = MyClient(intents=intents)

client.run('MTAzNTA1NzYwNjczOTM2MTg1Mw.G805BH.rKedyrpBC791KjIKdMqcOWJeMAJxShccwVZGS4')