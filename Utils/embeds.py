import discord
from discord import Embed
from typing import Type



def failed_embed_photo(error):
    embed_photo = (
        (discord.Embed(title="Error While Searching", color=discord.Color.red()))
        .add_field(name="Error Info", value=f"{error}")
        .set_footer(text="Fucky Wucky")
    )
    return embed_photo


def photo_embed(photo_info: tuple):

    try:
        #TODO Try to fix this BS Rey made
        #TODO 1024 Character Limit
        # descriptions_text : list = [""]
        # photo, title, explanation = photo_info
        # words_list : list = explanation.split(" ")
        # current_desc = 0

        # for word in words_list:
        #     if len(descriptions_text[current_desc]) + len(word) + 1 > 1024:
        #         current_desc += 1 

        #     descriptions_text[current_desc] = f"{descriptions_text[current_desc]}{word} "

        photo, title, explanation = photo_info 
        embed_photo = (
            discord.Embed(
                title="Daily Nasa Photo",
                description=f"**Name:** {title}",
                color=discord.Color.red(),
            )
            .add_field(name="Description of Photo", value=f"{explanation}", inline=True)
            .set_image(url=f"{photo}")
            .set_footer(
                text=f'{"Thanks to the APOD NASA API for image and description."}'
            )
        )
    except Exception as e:
        print(e)
        return failed_embed_photo(e)
    return embed_photo


def improper_format(date) -> Embed:
    embed_photo = (
        discord.Embed(title="Improper Date Input", color=discord.Color.red())
        .add_field(name="Value Given", value=date)
        .add_field(
            name="Proper Date Input",
            value="Date format must be **YYYY-MM-DD** and mustn't be before **1995-06-16**",
            inline=False,
        )
    )

    return embed_photo


def message_too_long():
    embed_photo = (
        discord.Embed(title="Char Limit Reached", color=discord.Color.red())
        .add_field(name="Info", value="API return statement is too long for discord..." )
        .set_footer(text="It's a work in progress")
        .set_thumbnail(url="https://img.freepik.com/premium-photo/crying-emoji-with-tears-eyes_764664-144.jpg?w=2000")
        
        
    )
    return embed_photo