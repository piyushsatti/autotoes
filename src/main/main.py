import os
from dotenv import load_dotenv
from typing import Final
from discord import Intents, Client, Message

# Loads the env vars
load_dotenv()

class MyClient(Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: Message):
        if message.author == client.user:
            return

        print(f'Message from {message.author}: {message.content}')

if __name__ == "__main__":
    
    # ENC Vars
    DISCORD_TOKEN: Final[str] = os.getenv("DISCORD_API_KEY")

    # Bot Setup
    intents = Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)

    client.run(DISCORD_TOKEN)
