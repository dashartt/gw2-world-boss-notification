from discord.ext import tasks

import discord


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.users_notification = list()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
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


    # @tasks.loop(seconds=1)  # task runs every 60 seconds
    # async def my_background_task(self):
    #     channel = self.get_channel(1234567)  # channel ID goes here
    #     self.counter += 1
    #     await channel.send(self.counter)


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = MyClient(intents=intents)

client.run('MTAzNTA1NzYwNjczOTM2MTg1Mw.G805BH.rKedyrpBC791KjIKdMqcOWJeMAJxShccwVZGS4')