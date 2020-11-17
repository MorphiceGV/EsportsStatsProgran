#import discord package

import discord
from discord.ext import commands

#client
##client = discord.Client()
client = commands.Bot(command_prefix='--')

#setting up commands
@client.command(name='version')

#context passed into function
#context has info on how version commmand was called

async def version(context):

    myEmbed = discord.Embed(title="Current Version", desciption="Bot Version 1.0", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released", value="November 11th, 2020", inline=False)
    myEmbed.set_footer(text="Sample Footer")
    myEmbed.set_author(name="Morphice")
    await context.message.channel.send(embed=myEmbed)

"""@client.command(name='users')
async def team(ctx):
    VC = discord.utils.get(ctx.client.channels, id =759785533022273541)
    int(VC.members) # each user is a member object
    for user in VC.members:
        #
        print(user.name)
    await ctx.send(user.name)

    ###version 2
 ##   vc = ctx.client.get_channel(759785533022273541)
##    await ctx.send("\n".join([str(i) for i in vc.members]))
"""

#do actions depending on event
@client.event
async def on_ready():
    #Do things
    #retrive channel that you want to access and save to a variable

    #general_channel = client.get_channel(759785533022273540)

    #await general_channel.send('@Morphice#4243 launch client')
    bot_spam_channel = client.get_channel(777346631825358872)
    #user_morphice = client.get_user(426096379727839232)
    await bot_spam_channel.send('start the site')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Minecraft'))
@client.event
async def on_message(message):

    if message.content == '!version':
        bot_spam_channel = client.get_channel(777346631825358872)

        myEmbed = discord.Embed(title ="Current Version", desciption="Bot Version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline= False)
        myEmbed.add_field(name="Date Released", value="November 11th, 2020", inline = False)
        myEmbed.set_footer(text="Sample Footer")
        myEmbed.set_author(name="Morphice")
        await bot_spam_channel.send(embed=myEmbed)

    if message.content =='!dm':

        await message.author.send('Test dm')

    await client.process_commands(message)

@client.event
async def on_disconnect():
    bot_spam_channel = client.get_channel(777346631825358872)
    await bot_spam_channel.send('Goodbye!')


#Run client on server
client.run('Nzc3MzQxMzk4MjQ3NjY5Nzgy.X7CBlw.nCD2dzm_hguyulDDVxkT_WOFODU')

