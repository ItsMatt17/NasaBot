import os
import platform

from discord import app_commands
import discord
import discord.ext
from discord.ext.commands import Bot, CommandOnCooldown
import asyncio
import logging
from config import DISCORD_AUTH

from Utils.embeds import failed_embed_photo


class NasaBot(Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.synced = False

    async def on_ready(self) -> None:
        """
        Send some start-up messages on Bot Ready State
        :return: None
        """

        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="The Stars"
            )
        )

        print("-------------------")
        print(f"Logged in as {self.user.name}")
        print(f"Discord.py API version: {discord.__version__}")
        print(f"Python version: {platform.python_version()}")
        print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
        print("Go for launch!")
        print("-------------------")
        logging.info("Good to go")

        
        # for filename in os.listdir("./cogs"):
        #     if filename.endswith(".py"):
        #         print(
        #             f"[COG] Loaded bot extension", f"/{filename.replace('.', '/')}.py"
        #         )
        #     await bot.load_extension(f"cogs.{filename[:-3]}") # literally no idea why this didn't work, but whatever

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                print(
                    f"[COG] Loaded bot extension", f"/{filename.replace('.', '/')}.py"
                )
                await bot.load_extension(f"cogs.{filename[:-3]}")
    
    async def on_application_command_error(self, context, exception):
        """
        Whenever there is a command error, it'll be handled here
        :param context: Context of the request
        :param exception: The error that was raised
        :return: None
        """

        # If the command cooldown is reached
        if isinstance(exception, CommandOnCooldown):
            return await context.respond(
                ephemeral=True,
                embed=failed_embed_photo(f"You are on cooldown! Try again in `{round(exception.retry_after, 1):,}` seconds.")
            )

        raise exception
    

intents = discord.Intents.all()
bot: NasaBot = NasaBot(
    command_prefix="!",
    intents=intents,
)


@bot.tree.command(
    name="sync",
    description="Sync tree commands ",
    guild=discord.Object(id=982514587742142545),
)
async def sync(interaction: discord.Interaction):
    if interaction.user.id == 188779992585469952:  # My ID
        synced = await bot.tree.sync()
        await interaction.response.send_message(f"Synced {len(synced)} synced commands")
        print(f"Synced {len(synced)} synced commands")

    else:
        await interaction.response.send_message(
            "You must be the owner to use this command!"
        )


if __name__ == "__main__":
    bot.run(DISCORD_AUTH)
