import datetime

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot, CommandOnCooldown
from discord import app_commands

from main import bot
from Utils.embeds import photo_embed, improper_format, message_too_long
from Utils.request import get_photo, get_dated_photo
from Utils.date_parsing import search

CHANNEL_ID = 982534397309894707


time_info = datetime.time(hour=4, minute=00, second=0, tzinfo=datetime.timezone.utc)
channel = bot.get_channel(CHANNEL_ID)


class AutoPhotoManager(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: Bot = bot
        self.channel = self.bot.get_channel(CHANNEL_ID)
        super().__init__()
        self.auto_photo.start()


    #TODO Fix cooldown system idk why tf it's broken
    @app_commands.command(name="photo", description="give datedphoto...")
   # @commands.cooldown(1, 60.0, commands.BucketType.user)
    async def photo(
        self, interaction: discord.Interaction, year: str, month: str, day: str
    ) -> None:
        """Command for dated photos

        params:
        -------
        interaction : discord.Interaction

        year : str

        month : str

        day : str

        """

        compiled_date = f"{year}-{month}-{day}"
        if search(year, month, day):
            dated_info = get_dated_photo(f"{year}-{month}-{day}")
            print(dated_info)

            if dated_info == "Limit":
                embed = message_too_long()

            elif dated_info != None:
                embed = photo_embed(dated_info)

            else:
                embed = improper_format(compiled_date)

        else:
            embed = improper_format(compiled_date)

        await interaction.response.send_message(embed=embed)

    @tasks.loop(time=time_info)
    async def auto_photo(self) -> None:
        """Task loop which handles message send

        return None
        """
        embed = photo_embed(get_photo())
        try:
            await self.channel.send(embed=embed)

        except Exception as e:
            await self.channel.send(content=str(e))


async def setup(bot: commands.Bot):
    await bot.add_cog(AutoPhotoManager(bot))
