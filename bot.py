import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import random
import time
import datetime
import io
import os
import platform
import sys
import json

minutes = 0
hour = 0
bot = discord.Client()
bot_prefix= "<" 
bot = commands.Bot(command_prefix=bot_prefix)



bot.remove_command("help")
@bot.command(pass_context=True)
async def help(ctx):
   embed=discord.Embed(title="If You Need On Help Please Join Our Support Server ", url="https://discord.gg/fq3J5c5")
   embed.set_author(name='Hello Help Center - Prefix "<"', icon_url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.png?size=256")
   embed.add_field(name=" :gun: Action Commands", value="`hug` , `kiss` , `slap`" , inline=False)
   embed.add_field(name=":video_game: Game Commands", value="`rps paper` , `rps rock` , `rps scissor` " , inline=False) 
   embed.add_field(name=":information_source: Info Commands", value="`ping` , `serverinv` , `serverinfo` , `servericon` ,  `afk - back` ,  `userinfo` , `avatar` , `count`" , inline=False)
   embed.add_field(name=":joy: Fun Commands", value="`insult` , `troll` , `virus` , `8ball` , `tell` , `lovecal` , `gaycal`" , inline=False)
   embed.add_field(name="<:tankilogo:419067537007837184> Tanki Online Commands", value="`tolinks`, `battle` , `open1` , `open10` ,` play` , `tankibot` , `dropgold`", inline=False)
   embed.add_field(name=":regional_indicator_f: Fortnite Commands", value="`fortnite_drop` , `fortnite_dance`", inline=False)
   embed.add_field(name=":trophy: Moderation Commands", value="`report` , `suggest` , `warn` , `changenick` , `c_mute` , `c_unmute` ,`kick` , `ban` , `getbans` , `clear`" , inline=True)
   embed.add_field(name=":camera_with_flash: Image Commands", value="`cry` , `cat` , `meme` , `dog` , `cheer` , `party`"  , inline=True)
   embed.add_field(name=":robot: Bot Info Commands", value="`support` , `premium` , `uptime` , `info` , `askhelp` , `reqpre` " , inline=True)
   embed.set_footer(text="Requested By {} | {}".format(ctx.message.author.name,ctx.message.server.name) , icon_url=ctx.message.server.icon_url)
   await bot.say(embed=embed)



@bot.event
async def on_command(command, ctx):
    chane = bot.get_channel("451696010914299905")
    await bot.send_message(chane,"**Command** `<{}` , **Server:** `{}` | `{}` **User:** `{}` | `{}`".format(command,
            ctx.message.server.name,
            ctx.message.server.id,
            ctx.message.author.name,
            ctx.message.author.id))

@bot.event
async def on_server_join(server):
    await bot.change_presence(game=discord.Game(name="<HELP | {:,} Servers & {:,} Users ".format(len(bot.servers) , len(set(bot.get_all_members()))),type=3))
    channel = bot.get_channel("452352293275172894")
    await bot.send_message(server.owner ,":wave: Hey There ! I am **Hello** , A Discord Bot By Scanner#4797 <:Hello:446973883619213312>\n\nTo Get Started Use `<help` to View All Commands !\nMust Have a Channel Named `hello-logs` as the Log Channel\n\n**Useful Links:-**\nDiscord Bot List Vote :- https://discordbots.org/bot/445544179310002176\nSupport Server :- https://discord.gg/S6gDBqr\n\n:tada: **Enjoy ! Have Fun !**")
    await bot.send_message(channel, "**The bot has just joined a new server! :tada:**\n **Server name:** {}\n**Server Owner :**{}\n**Total members:** {:,}".format(server.name,server.owner,len(server.members)))

@bot.event
async def on_server_remove(server):
    await bot.change_presence(game=discord.Game(name="<HELP | {:,} Servers & {:,} Users ".format(len(bot.servers) , len(set(bot.get_all_members()))),type=3))
    channel = bot.get_channel("452352293275172894")
    await bot.send_message(channel, "**The bot has just left a server! :cry:**\n **Server name:** {}\n**Server Owner :**{}\n**Total members:**{:,}".format(server.name,server.owner,len(server.members)))

@bot.event
async def on_member_join(member):
    server = member.server
    if server.id == "418001869781205002":
        if not member.avatar_url:
            mem_ava = member.default_avatar_url
        else:
            mem_ava = member.avatar_url

        channel1 = bot.get_channel("418001869781205004")
        embed=discord.Embed(title="Joined", description="\n\n:tada: Welcome **{}** to **{}** , Your the **{}** User !\n\n".format(member.mention,member.server.name, len(server.members)))
        embed.set_author(name=member.name, icon_url=mem_ava)
        embed.set_thumbnail(url=server.icon_url)
        embed.set_footer(text=server.name , icon_url=server.icon_url)
        await bot.send_message(channel1, embed=embed)

    elif server.id == "458206172940337190":
        #MSI#
        channe = bot.get_channel("458213198408056834")
        server = member.server
        msg = "**:tada: Welcome to {} {} , You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        await bot.send_message(channe, msg)


    elif server.id == "446967025773051905":
        #Hello SS#
        channel1 = bot.get_channel("446972812712738816")
        server = member.server
        msg = "**<:Hello:446973883619213312> Welcome to {} {} , You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        await bot.send_message(channel1, msg)

    elif server.id == "419567438452097027":
        #Games Server (Prince)#
        channel1 = bot.get_channel("419567438972059649")
        server = member.server
        msg = "**:tada: Welcome to {} {} , You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        await bot.send_message(channel1, msg)
        x2 = bot.get_message("418004504206770176" , "461160883989774356")
        await bot.send_message(member ,  x2)

    elif server.id == "454067549374775306":
        # Blitz Server #
        channel2 = bot.get_channel("454067549374775309")
        server = member.server
        msg = "**:tada: Welcome to {} {} , You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        await bot.send_message(channel2, msg)

    elif server.id == "441893381397020673":
        #Alak
        channel2 = bot.get_channel("441895176953135105")
        server = member.server
        msg = "**:tada: Welcome to {} {} , You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        await bot.send_message(channel2,msg )

    else:
        return

@bot.event
async def on_member_remove(member):
    server = member.server
    if server.id == "419567438452097027":
        #Games Server
        channel = bot.get_channel("419567438972059649")
        msg = ":wave: ** {} Has Just Left the Server !**".format(member)
        await bot.send_message(channel, msg)
    elif server.id == "454067549374775306":
        #Blitz
        channel2 = bot.get_channel("454067549374775309")
        msg = ":wave: ** {} Has Just Left the Server !**".format(member)
        await bot.send_message(channel2, msg)
    else:
        return

print("Logging...")
@bot.event
async def on_ready():
    chan = bot.get_channel("453821473694547970")
    await bot.send_message(chan , "I Was Restarted Just Now ! :wink:")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Users: {}".format(len(set(bot.get_all_members()))))
    await bot.change_presence(game=discord.Game(name="<HELP | {:,} Servers & {:,} Users ".format(len(bot.servers) , len(set(bot.get_all_members()))),type=3))

@bot.event
async def on_command_error(error, ctx):
    await bot.change_presence(game=discord.Game(name="<HELP | {:,} Servers & {:,} Users ".format(len(bot.servers) , len(set(bot.get_all_members()))),type=3))
    if isinstance(error, commands.BadArgument):
        await bot.send_message(ctx.message.channel,"<:Fail:461924435176325120> Invalid Argument")
    elif isinstance(error, commands.CommandNotFound):
        chan =  bot.get_channel ("451695928336842753")
        await bot.send_message(chan, "{} Used Not Avalible Command On {} With Server ID {}" .format(ctx.message.author.mention , ctx.message.server.name , ctx.message.server.id))
    elif isinstance(error, commands.CheckFailure):
        await bot.send_message(ctx.message.channel, "<:Fail:461924435176325120> You Don't Have Enough  Permissions to Excute this Command ! ")
    elif isinstance(error, discord.errors.Forbidden):
        await bot.send_message(ctx.message.author , "<:Fail:461924435176325120> Missing Permissions to Excute the Command !")
    elif isinstance(error, commands.CommandOnCooldown):
        x =  await bot.send_message(ctx.message.channel, "<:Fail:461924435176325120> **Spam Alert !**\n\n{} , {}".format(ctx.message.author.mention , error))
        await asyncio.sleep(5)
        await bot.delete_message(x)
    else:
        await bot.send_message(ctx.message.author, "<:Fail:461924435176325120> Something is Wrong ! ")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot:
        return

    elif message.content.startswith('<uptime'):
        embed=discord.Embed()
        embed.add_field(name="Uptime", value=":clock10: **|** I Have Been Online For **{0}** Hour(s) and **{1}** Minute(s) !".format(hour , minutes), inline=True)
        await bot.send_message(message.channel , embed=embed)

    elif message.content.startswith('<count'):
        embed=discord.Embed(description="**Searching Messages Sent** <a:loading:438280917363195905>\n\nThis May Take Some Time !")
        mesg = await bot.send_message(message.channel, embed=embed)
        counter = 0
        async for msg in bot.logs_from(message.channel, limit=99999):
            if msg.author == message.author:
                counter += 1
        embed=discord.Embed(title="Messages Sent ",color=0x080808)
        embed.set_author(name="{}".format (message.author.name), icon_url="{}".format (message.author.avatar_url))
        embed.add_field(name="Name", value="{}".format (message.author) , inline=True)
        embed.add_field(name="Messages Sent", value="{}".format(str(counter)), inline=True)
        embed.add_field(name="Channel", value="<#{}>".format (message.channel.id), inline=True)
        embed.set_footer(text="{}".format(message.server.name) ,icon_url="{}".format(message.server.icon_url))
        await bot.edit_message(mesg, embed=embed)

    elif message.content.startswith('<rps rock'):
        await bot.send_message(message.channel, random.choice([":scissors: **|** You Choose __Rock__ , I Choose __Scissors__ , **You Win**  :tada:",
                                                                  ":newspaper: **|** You Choose __Rock__ , I Choose __Paper__ , **You Lose**  :robot:",
                                                                  ":scissors: **|** You Choose __Rock__ , I Choose __Scissors__ , **You Win**  :tada:",
                                                                  ":newspaper: **|** You Choose __Rock__ , I Choose __Paper__ , **You Lose**  :robot:",
                                                                  ":black_circle:  **|** You Choose __Rock__ , I Choose __Rock__ , **Its Tie**  :confused:" ]))

    elif message.content.startswith('<rps scissor'):
        await bot.send_message(message.channel, random.choice([":scissors: **|** You Choose __Scissors__ , I Choose __Scissors__ , **Its Tie**  :confused:",
                                                                  ":newspaper: **|** You Choose __Scissors__ , I Choose __Paper__ ,  **You Lose**  :robot:",
                                                                  ":scissors: **|** You Choose __Scissors__ , I Choose __Scissors__ ,  **Its Tie**  :confused",
                                                                  ":newspaper: **|** You Choose __Scissors__ , I Choose __Paper__ ,  **You Lose**   :robot:",
                                                                  ":black_circle:  **|** You Choose Scissors__ , I Choose __Rock__ , **You Lose**  :robot: " ]))

    elif message.content.startswith("<rps paper"):
        await bot.send_message(message.channel, random.choice([":scissors: **|** You Choose __Paper__ , I Choose __Scissors__ , **You Lose**  :robot:",
                                                                  ":newspaper: **|** You Choose __Paper__ , I Choose __Paper__ ,  **Its Tie**  :confused:",
                                                                  ":scissors: **|** You Choose __Paper__ , I Choose __Scissors___ , **You Lose**  :robot:",
                                                                  ":newspaper: **|** You Choose __Paper__ , I Choose __Paper___ ,  **Its Tie**  :confused:",
                                                                  ":black_circle:  **|** You Choose __Paper__ , I Choose __Rock__ , **You Win**  :tada:" ]))
    elif message.content.startswith ("<8ball"):
        await bot.send_message(message.channel, random.choice([":8ball: | **{},** It is Certain ".format(message.author.name),
                                                                  ":8ball: | **{},** It is Decidedly, So ?".format(message.author.name),
                                                                  ":8ball: | **{},** Without a doubt ".format(message.author.name),
                                                                  ":8ball: | **{},** Yes, definitely  ".format(message.author.name),
                                                                  ":8ball: | **{},** You may rely on it ".format(message.author.name),
                                                                  ":8ball: | **{},** As I see it, yes  ".format(message.author.name),
                                                                  ":8ball: | **{},** Most likely  ".format(message.author.name),
                                                                  ":8ball: | **{},** Outlook Looks Good  ".format(message.author.name),
                                                                  ":8ball: | **{},** Yes Bro ".format(message.author.name),
                                                                  ":8ball: | **{},** Signs point to yes ".format(message.author.name),
                                                                  ":8ball: | **{},** Reply lazy try again ".format(message.author.name),
                                                                  ":8ball: | **{},** Ask again later ".format(message.author.name),
                                                                  ":8ball: | **{},** Better not tell you now ".format(message.author.name),
                                                                  ":8ball: | **{},** Cannot predict now ".format(message.author.name),
                                                                  ":8ball: | **{},** Concentrate and ask again ".format(message.author.name),
                                                                  ":8ball: | **{},** Don't count on it  ".format(message.author.name),
                                                                  ":8ball: | **{},** My reply is no ".format(message.author.name),
                                                                  ":8ball: | **{},** My sources say no ".format(message.author.name),
                                                                  ":8ball: | **{},** Outlook is Not So Good  ".format(message.author.name),
                                                                  ":8ball: | **{},** Very doubtful  ".format(message.author.name)]))
    elif message.content.startswith("<tell"):
        text = message.content[len('<tell'):].strip()
        if "efnejifn" in text:
            await bot.send_message(message.channel , ":x: -{}-".format(message.author))
        elif "discord." in text:
            await bot.send_message(message.channel , ":x: -{}-".format(message.author))
        elif "@here" in text:
            await bot.send_message(message.channel , ":x: -{}-".format(message.author))
        elif "@everyone" in text:
            await bot.send_message(message.channel , ":x: -{}-".format(message.author))
        else:
            await bot.send_message(message.channel ,"{}".format(text))
            await bot.delete_message(message)

    elif message.content.startswith('<afk'):
        name = message.content[len("<afk"):].strip()
        if "@everyone" in name:
            await bot.send_message(message.channel , ":grin: I am Hello Bot :x: -{}-".format(message.author))
        elif "@here" in name:
            await bot.send_message(message.channel , ":grin: I am Hello Bot :x: -{}-".format(message.author))

        else:
            await bot.send_message(message.channel, '**{}** , I Have Set Your AFK : {}'.format(message.author.name , name))

        def check(msg):
            return msg.content.startswith('<back')

        message = await bot.wait_for_message(author=message.author, check=check)

        await bot.send_message(message.channel, "Welcome Back **{}** , I Removed Your AFK Status".format (message.author.name))

    elif message.content.upper().startswith('<Hey Hello'):
        if message.author.id == "429118689367949322":
            await bot.send_message(message.channel, "Hey {} !\n**Owner , Technical Staff , Suppport Team** ".format(message.author.mention))

        else:
              await bot.send_message(message.channel,"Hey {} !\n **Player**".format(message.author.mention))

    await bot.process_commands(message)
@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def reqpre (ctx , *args):
    txt = ' '.join(args)
    pre = bot.get_channel("451696819638894592")
    await bot.send_message(ctx.message.channel ,"Your Request Has Been Sent ! <:Pass:461924196390404106>\nGood Luck For The Approval ! ")
    await bot.send_message(pre ,"User:- {}\nID:- {}\nMessage:- {} ".format(message.author.mention , message.author.id ,text))
    await bot.delete_message(message)


@bot.command(pass_context=True)
async def test (ctx):
    await bot.say("<:Pass:461924196390404106> **Worked !**")

@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def askhelp (ctx):
    try:
        text = ctx.message.content[len('<askhelp'):].strip()
        channel = bot.get_channel("451695948704382978")
        await bot.delete_message(ctx.message)
        await bot.send_message(ctx.message.channel, "{}  , Your Message Has Been Sent In ! <:Pass:461924196390404106>" .format(ctx.message.author.mention))
        await bot.send_message(ctx.message.author, "**Hey There !** <:Pass:461924196390404106> \nWe Successfully Recorded You Issue !\n\n Please be Patient... Until We Check !")
        await bot.send_message(channel,"**User:-** <@{}>\n**Server:-** {} , {} \n**Problem:-** {}".format(ctx.message.author.id, ctx.message.server.name , ctx.message.server.id ,text))
    except:
        await bot.say("<:Fail:461924435176325120> Something is Wrong ! , Please Try Again !")


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def battle(ctx , user : discord.Member = None):

    team = random.choice([ctx.message.author.name , user.name])
    team2 = random.choice([ctx.message.author.name , user.name])
    team3 = random.choice([ctx.message.author.name , user.name])
    chan = ctx.message.channel
    rturr = random.choice(["Firebird" , "Freeze" , "Smoky" , "Hammer" , "Striker" ,"Thunder" , "Railgun" , "Shaft" , "Magnum" , "Terminator" ,"Railgun XT" ,"Terminator XT" ])
    rhull = random.choice(["Titan" , "Viking" , "Hornet" , "Mammoth" , "Wasp" ,"Juggernaut"])
    mturr = random.choice(["Firebird" , "Freeze" , "Smoky" , "Hammer" , "Striker" ,"Thunder" , "Railgun" , "Shaft" , "Magnum" , "Terminator" ])
    scree = random.choice(["https://cdn.discordapp.com/attachments/437510467196551168/456416178982748160/maxresdefault.jpg" , "https://cdn.discordapp.com/attachments/437510467196551168/437510909519200265/maxresdefault_2.jpg" , "https://cdn.discordapp.com/attachments/437510467196551168/442216558530658305/Screenshot_110.png" , "https://cdn.discordapp.com/attachments/437510467196551168/442225631686688768/striker_viking_stadium30000.png"])
    mhull = random.choice(["Titan" , "Viking" , "Hornet" , "Mammoth" , "Wasp" ,"Juggernaut"])
    winner = random.choice([ctx.message.author.name , user.name])
    if user is None:
        await bot.say(":x: Mention a User to Start the Battle With ! ")
    if user.id == bot.user.id:
        await bot.say("Nope ! I Don't Want To Battle :x: ")
    if user.id ==  ctx.message.author.id:
         await bot.say(":x: You Cannot Start the Battle Your Self")
    else:
        embed=discord.Embed(title="Battle Starts..", description="\n\n**Loading :<a:loading:438280917363195905>**\n\n")
        embed.set_author(name="{} VS {}".format(ctx.message.author.name , user.name), icon_url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
        embed.set_thumbnail(url=scree)
        embed.add_field(name="Battle Details", value="**{}** - {} M3 , {} M3\n**{}** - {} M3 , {} M3".format(ctx.message.author.name
        ,rturr
        ,rhull
        ,user.name
        ,mturr
        ,mhull), inline=False)
        embed.set_footer(text="Battle Starts in Few Seconds")
        x = await bot.send_message(chan ,embed=embed)
        await asyncio.sleep(5)
        embed=discord.Embed(title="Battle Log ")
        embed.set_author(name="{} VS {}".format(ctx.message.author.name , user.name), icon_url="https://cdn.discordapp.com/attachments/433182340211146755/433485204925972480/Tanki-Online-Logo.png")
        embed.set_thumbnail(url=scree)
        embed.add_field(name="Log..", value="{} Spawn\n{} Spawn\n{} Shoot {}\n{} Go {} Behind and Shoot Him\n{} Used Repair Kit\nFinally {} Did  {} Kills and Won !".format(team
        ,ctx.message.author.name
        ,user.name
        ,team
        ,team3
        ,team
        ,team2
        ,winner
        ,random.randint(1,100)), inline=False)
        embed.add_field(name="Winner", value=winner, inline=False)
        embed.add_field(name="Rewards", value="{} - **{}** Crystals\n{} - **{}** Crystals".format(ctx.message.author.name
        ,random.randint(1 , 100)
        ,user.name
        ,random.randint(2, 100)), inline=True)
        embed.add_field(name="Turrents and Hulls" , value="**{}** - {} M3 , {} M3\n**{}** - {} M3  , {} M3".format(ctx.message.author.name,
        rturr,
        rhull,
        user.name,
        mturr,
        mhull), inline=True)
        embed.set_footer(text="{} Won | Challenger {}".format(winner , ctx.message.author.name) , icon_url="https://cdn.discordapp.com/attachments/433182340211146755/433485204925972480/Tanki-Online-Logo.png")
        x = await bot.edit_message(x ,embed=embed)





@bot.command(pass_context = True)
async def checkrep(ctx, user : discord.Member):
    if ctx.message.server.id == "418001869781205002":
        #SCANNER'S
        await bot.say("Sent !")
        await bot.send_message(user ,"Your Report Was Checked By The Moderators In **{}** , Check There !".format(ctx.message.server.name))
    else:
        return

@bot.command(pass_context = True)
async def checksug(ctx, user : discord.Member):
    if ctx.message.server.id == "418001869781205002":
        #SCANNER'S
        await bot.say("Sent !")
        await bot.send_message(user ,"Your Report Was Checked By The Moderators In **{}** , Check There !".format(ctx.message.server.name))
    else:
        return

@bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def dropgold(ctx):
    embed = discord.Embed(description = "<:gold:419067513712672769> **| {}** Has Dropped a Gold Box ".format(ctx.message.author.name), color=0xfce700)
    await bot.say(embed=embed)

    await asyncio.sleep(0.5)
    msg = await bot.wait_for_message(channel=ctx.message.channel)
    if msg.author.id == bot.user.id:
        return
    else:
        embed = discord.Embed(description = "<:gold:419067513712672769> **| {}** Has Taken the Gold Box ".format(msg.author.name), color =0xfce700)
        await bot.say(embed=embed)


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def premium(ctx):
    await bot.say("**Hello Premium <:Premium:447648813331513354>**\nAllows You To Use Premium Commands\nType `<help` To Check premuim Commands\n$1 For a User , $3 For a Server ")


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def tolinks(ctx):
    await bot.send_message(ctx.message.channel,"**Tanki Online Useful Links :link:**\n\nTanki Online Official :- https://tankionline.com/\nTanki Online Ratings :-https://ratings.tankionline.com/en/\nTanki Online Forum :-https://en.tankiforum.com/\nTanki Online Wiki :-https://en.tankiwiki.com/Tanki_Online_Wiki/\nTanki Online Help:- https://help.tankionline.com/\n\n **Tanki Online EN | Hello 2018**")

@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def servericon(ctx):
    embed=discord.Embed(title="{} Icon URL".format(ctx.message.server.name), url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
    embed.set_image(url=ctx.message.server.icon_url)
    embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
    embed.set_footer(text="Requested By {} | {}".format(ctx.message.author.name , ctx.message.server.name) , icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)



@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def serverinfo(ctx):
    server = ctx.message.server
    text_channels = len([x for x in server.channels
                         if x.type == discord.ChannelType.text])
    voice_channels = len([x for x in server.channels
                         if x.type == discord.ChannelType.voice])

    embed=discord.Embed(title="Server Information", url="https://discordapp.com/branding")
    embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Server Owner", value=ctx.message.server.owner, inline=True)
    embed.add_field(name="Server Owner ID", value=ctx.message.server.owner.id, inline=True)
    embed.add_field(name="Server Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Server Members", value=len(ctx.message.server.members), inline=True)
    embed.add_field(name="Server Reigon", value=ctx.message.server.region, inline=True)
    embed.add_field(name="Text Channels", value=text_channels, inline=True)
    embed.add_field(name="Voice Channels", value=voice_channels, inline=True)
    embed.set_footer(text="Server Info Requested By {} | {} ".format(ctx.message.author.name , ctx.message.server.name),icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def avatar(ctx, user: discord.Member = None):
    if not user:
        if not ctx.message.author.avatar_url:
            embed=discord.Embed()
            embed=discord.Embed(title="Your Avatar Link", url="{}".format(ctx.message.author.default_avatar_url), color=0x070707)
            embed.set_author(name="{}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.default_avatar_url))
            embed.set_image(url=ctx.message.author.default_avatar_url)
            embed.set_footer(text="{}".format(ctx.message.server.name),icon_url="{}".format(ctx.message.server.icon_url))
            await bot.say(embed=embed)

        else:
            embed=discord.Embed()
            embed=discord.Embed(title="Your Avatar Link", url="{}".format(ctx.message.author.avatar_url), color=0x070707)
            embed.set_author(name="{}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
            embed.set_image(url=ctx.message.author.avatar_url)
            embed.set_footer(text="{}".format(ctx.message.server.name),icon_url="{}".format(ctx.message.server.icon_url))
            await bot.say(embed=embed)
    else:
        if not user.avatar_url:
            embed=discord.Embed()
            embed=discord.Embed(title="{}'s Avatar Link".format(user.name), url="{}".format(user.default_avatar_url), color=0x070707)
            embed.set_author(name="{}".format(user.name), icon_url="{}".format(user.default_avatar_url))
            embed.set_image(url=user.default_avatar_url)
            embed.set_footer(text="{} | Requested By {}".format(ctx.message.server.name ,ctx.message.author.name) ,icon_url="{}".format(ctx.message.server.icon_url))
            await bot.say(embed=embed)

        else:
            embed=discord.Embed()
            embed.set_author(name="{}".format(user.name), icon_url="{}".format(user.avatar_url))
            embed=discord.Embed(title="{}'s Avatar Link".format(user.name), url="{}".format(user.avatar_url), color=0x070707)
            embed.set_author(name="{}".format(user.name), icon_url="{}".format(user.avatar_url))
            embed.set_image(url=user.avatar_url)
            embed.set_footer(text="{} | Requested By {}".format(ctx.message.server.name ,ctx.message.author.name) ,icon_url="{}".format(ctx.message.server.icon_url))
            await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def userinfo(ctx, user: discord.Member = None):
    if user is None:
        if not ctx.message.author.avatar_url:
            avatar = ctx.message.author.default_avatar_url
        else:
            avatar = ctx.message.author.avatar_url

        embed=discord.Embed(title="{}'s Information".format(ctx.message.author.name), url=avatar)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=avatar)
        embed.add_field(name="User Name", value=ctx.message.author.name, inline=True)
        embed.add_field(name="User Tag", value="#" + ctx.message.author.discriminator, inline=True)
        embed.add_field(name="User ID", value=ctx.message.author.id, inline=True)
        embed.add_field(name="User Status", value=ctx.message.author.status, inline=True)
        embed.add_field(name="User Top Role", value=ctx.message.author.top_role, inline=True)
        embed.add_field(name="Playing", value=ctx.message.author.game, inline=True)
        embed.add_field(name="User Joined On", value=ctx.message.author.joined_at, inline=True)
        embed.set_footer(text="{}".format(ctx.message.server.name) ,icon_url="{}".format(ctx.message.server.icon_url))
        await bot.say(embed=embed)

    else:
        if not user.avatar_url:
            ava = user.default_avatar_url
        else:
            ava = user.avatar_url

        embed=discord.Embed(title="{}'s Information".format(user.name), url=ava)
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.set_thumbnail(url=ava)
        embed.add_field(name="User Name", value=user.name, inline=True)
        embed.add_field(name="User Tag", value="#" + user.discriminator, inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="User Status", value=user.status, inline=True)
        embed.add_field(name="User Top Role", value=user.top_role, inline=True)
        embed.add_field(name="Playing", value=user.game, inline=True)
        embed.add_field(name="User Joined On", value=user.joined_at, inline=True)
        embed.set_footer(text="{}".format(ctx.message.server.name) ,icon_url="{}".format(ctx.message.server.icon_url))
        await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def hug(ctx, *, member: discord.Member = None):
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " Has Been Hugged! :heart:")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " Has Hugged Him Self!")
            else:
                await bot.say(ctx.message.author.mention + " Has Hugged " + member.mention + "! :heart:")
    except:
        await bot.say("Something Went Wrong <:Fail:461924435176325120>")

@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def gaycal(ctx , user :discord.Member =  None):
    if user is None:
        await bot.say("<:Fail:461924435176325120> Mention a User to Check Gay Percentage !")
    
    else:
        embed=discord.Embed(title="Calculator ", description="**{}** is **{}%** Gay ".format(user.name , random.randint(1 , 100)))
        embed.set_author(name="Gay", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/462845519925084163/tumblr_p8us2iXWsD1viisjvo1_500.png")
        embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def lovecal(ctx , user1 :discord.Member =  None, user2 :discord.Member = None):
    if user1 is None:
        await bot.say("<:Fail:461924435176325120> Mention the First User to Check with Other")
    if user2 is None:
        await bot.say("<:Fail:461924435176325120> Mention the Second User Also !")
    if user1.id and user2.id == ctx.message.author.id:
        await bot.say("<:Fail:461924435176325120> I Can't Let You Do That ! xD") 
            
    else:
        embed=discord.Embed(title="Calcualtor ", description="Love Between **{}** and **{}** is \n**{}%**".format(user1.name , user2.name , random.randint(1 , 100)))
        embed.set_author(name="Love", icon_url="https://cdn.discordapp.com/attachments/418001869781205004/462843460052058132/images.png")
        embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
        await bot.say(embed=embed)


@bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def play(ctx):
    embed=discord.Embed(title="Go Ahead Play Tanki Click The Link ", url="https://tankionline.com/battle-en.html#/", color=0x070707)
    embed.set_author(name="Play Tanki Online ", icon_url="https://cdn.discordapp.com/attachments/433182340211146754/447402587822620673/8475ec065fffc1db1d0a9470a529ce67.jpg")
    embed.add_field(name=":link: Click To Play" , value="[Link Click To Start Blasting Enemy Tanks !](https://tankionline.com/battle-en.html#/)", inline=False)
    embed.set_footer(text="Hello | Tanki Online EN | 2018 ",icon_url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
    await bot.say(embed=embed)

@bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def invite(ctx):
    embed=discord.Embed(title="Invite Links", url="https://discord.gg/UWsfvzK", color=0x0d0d0d)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    embed.set_author(name="Hello Discord Bot", icon_url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    embed.add_field(name=":link:  Invite Hello Bot", value="[Click To Invite](https://discordapp.com/oauth2/authorize?client_id=445544179310002176&scope=bot&permissions=267779302)", inline=True)
    embed.add_field(name=":link: Offcial Hello Site", value="[Click Here to Vist](https://hello-bot.wixsite.com/hello-discord)", inline=False)
    embed.add_field(name=":tada:  Vote Me Discord Bot List", value="[Click To Vote](https://discordbots.org/bot/445544179310002176)", inline=False)
    embed.add_field(name=":tools: Join Support Server", value="[Click Here To Join](https://discord.gg/S6gDBqr)", inline=True)
    embed.set_footer(text="Hello Bot | 2018 | Scanner#4797" , icon_url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def serverinv(ctx):
    invitelinknew = await bot.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 100)
    await bot.send_message(ctx.message.channel , "Here is a Invite Link For {}\nMax Uses 100\n{}".format(ctx.message.server.name , invitelinknew))

@bot.command(pass_context = True)
@commands.has_role("jhgiudfiudz")
async def servers(ctx):
    x = '\n'.join([str(server) for server in bot.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color=0x111111)
    return await bot.say(embed = embed)

@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def getbans(ctx):
    if not ctx.message.author.server_permissions.administrator:
        return

    else:
        x = await bot.get_bans(ctx.message.server)
        x = '\n'.join([y.name for y in x])
        embed = discord.Embed(title = "<a:SARC:437630981034213376> List of Banned Members For {}".format(ctx.message.server.name), description = x, color=0x080808)
        return await bot.say(embed = embed)


@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)


@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def virus(ctx, user: discord.Member = None):
    if user is None:
        await bot.say("<:Fail:461924435176325120> Mention a User to Send Virus ! ")
    else:
        chan = ctx.message.channel
        x = await bot.send_message(chan , "<a:loading:438280917363195905> Packing Files.")
        await asyncio.sleep(1)
        x = await bot.edit_message(x , "<a:loading:438280917363195905> Packing Files..")
        await asyncio.sleep(1)
        x= await bot.edit_message(x , "<a:loading:438280917363195905> Packing Files...")
        await asyncio.sleep(3)
        x = await bot.edit_message(x ,"<a:loading:438280917363195905> Obtaining IP Aderess...")
        await asyncio.sleep(2.5)
        x = await bot.edit_message(x , "<a:loading:438280917363195905> Initializing Code...")
        await asyncio.sleep(2)
        x = await bot.edit_message(x, "<a:loading:438280917363195905> Installing Virus.")
        await asyncio.sleep(0.5)
        x = await bot.edit_message(x, "<a:loading:438280917363195905> Installing Virus..")
        await asyncio.sleep(0.5)
        x = await bot.edit_message(x, "<a:loading:438280917363195905> Installing Virus...")
        await asyncio.sleep(0.5)
        x = await bot.edit_message(x, "<a:loading:438280917363195905> Finshing...")
        await asyncio.sleep(2.5)
        x = await bot.edit_message(x, "<:verified:419067353545048064> **|** Virus Attack Success\nVirus Has Been Injected to **{}'s** System ".format(user.name))
        await bot.send_message(user , ":warning: **Alert !** :warning:\n\nYou May Have Been Hacked ! , `{}-Virus.exe` Have Been Found on Your Operating System.\nYour Data May Have Been Compromised. Please re-install Your OS Immediately.".format(ctx.message.author.name))
        await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def meme (ctx):
    memeran = random.choice(['https://i.imgur.com/hpB7qvi.png', 'https://i.imgur.com/vJ2TQwr.png',
                'https://i.imgur.com/m64uuhm.png', 'https://i.imgur.com/mMDZhos.png',
                'https://i.imgur.com/D2YNENN.png', 'https://media.giphy.com/media/aFTt8wvDtqKCQ/giphy.gif',
                'https://i.imgur.com/aNGHGzt.jpg', 'https://i.imgur.com/UWHgThx.jpg',
                'https://media.giphy.com/media/3oKIPmlzy5iyOyOyzK/giphy.gif', 'https://media.giphy.com/media/26gs6vEzlpaxuYgso/giphy.gif'])

    embed=discord.Embed()
    embed=discord.Embed(title="Here is a Meme For You ! ")
    embed.set_author(name="Meme Requested By {}".format(ctx.message.author.name) ,icon_url=ctx.message.author.avatar_url)
    embed.set_image(url=memeran)
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def cat (ctx):
    catcho = random.choice(['https://i.imgur.com/cnnG586.jpg', 'https://i.imgur.com/W5teHHG.png',
                'https://i.imgur.com/MUoXqDB.jpg', 'https://i.imgur.com/sLydwrm.jpg',
                'https://i.imgur.com/CCl6UOO.jpg', 'https://i.imgur.com/W0o3IIB.jpg',
                'https://i.imgur.com/0bLSY1H.jpg', 'https://i.imgur.com/l2UeDeA.jpg'])


    embed=discord.Embed()
    embed=discord.Embed(title=" Here is a Cute Cat For You ! :cat:", url="{}".format(ctx.message.author.avatar_url))
    embed.set_author(name="Cat Requested By {}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
    embed.set_image(url=catcho)
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def cheer(ctx):
    cher = random.choice(['https://media.giphy.com/media/TPkLd5oec1SzS/giphy.gif', 'https://media.giphy.com/media/m8Z2UqDYU20SY/giphy.gif',
                'https://media.giphy.com/media/xUPGcFeJiX8IImdEsw/giphy.gif', 'https://media.giphy.com/media/9DnHPHLhcgEVb3981r/giphy.gif',
                'https://media.giphy.com/media/xWDomsFyDpfy2G7rpx/giphy.gif', 'https://media.giphy.com/media/3oz8xEXgWWnUXIQI4o/giphy.gif',
                'https://media.giphy.com/media/9EoQM8QF6asUg/giphy.gif', 'https://media.giphy.com/media/8Fy7FayJ6Cjja/giphy.gif'])


    embed=discord.Embed()
    embed=discord.Embed(title=" Here is a Cheer For You ! :tada:", url="{}".format(ctx.message.author.avatar_url))
    embed.set_author(name="Cheer Requested By {}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
    embed.set_image(url=cher)
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def cry(ctx):
    cy = random.choice(['https://media.giphy.com/media/OPU6wzx8JrHna/giphy.gif', 'https://media.giphy.com/media/L95W4wv8nnb9K/giphy.gif',
                'https://media.giphy.com/media/5WmyaeDDlmb1m/giphy.gif', 'https://media.giphy.com/media/4bBLOhnMb0vHG/giphy.gif',
                'https://media.giphy.com/media/MSgJnzNSMGBc6BpGIc/giphy.gif', 'https://media.giphy.com/media/Ph8OWoJA2M3eM/giphy.gif'])


    embed=discord.Embed()
    embed=discord.Embed(title=" Very Sad ! :cry: ", url="{}".format(ctx.message.author.avatar_url))
    embed.set_author(name="Cry Requested By {}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
    embed.set_image(url=cy)
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def party(ctx):
    cyd = random.choice(['https://media.giphy.com/media/3rgXBQIDHkFNniTNRu/giphy.gif', 'https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif',
                'https://media.giphy.com/media/MS3XuWjQV1FiU/giphy.gif', 'https://media.giphy.com/media/xT8qAY7e9If38xkrIY/giphy.gif',
                'https://media.giphy.com/media/s2qXK8wAvkHTO/giphy.gif', 'https://media.giphy.com/media/l4pTfx2qLszoacZRS/giphy.gif',
                'https://media.giphy.com/media/YTbZzCkRQCEJa/giphy.gif', 'https://media.giphy.com/media/7vQZanyufdRe0/giphy.gif',
                'https://media.giphy.com/media/3KC2jD2QcBOSc/giphy.gif', 'https://media.giphy.com/media/10hO3rDNqqg2Xe/giphy.gif',
                'https://media.giphy.com/media/l41Yy2XyXWlSvupl6/giphy.gif', 'https://media.giphy.com/media/xUNd9HAossTNDyUUbS/giphy.gif',
                'https://media.giphy.com/media/bj09BK2BzLLQk/giphy.gif', 'https://media.giphy.com/media/AuMt534EY2Ahy/giphy.gif'])


    embed=discord.Embed()
    embed=discord.Embed(title="Let's Party ! :tada: ", url="{}".format(ctx.message.author.avatar_url))
    embed.set_author(name="Party Requested By {}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
    embed.set_image(url=cyd)
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    await bot.send_message(ctx.message.channel, embed=embed)


@bot.command(pass_context=True)
async def fortnite_dance (ctx):
    catfcho = random.choice(['https://media.giphy.com/media/1lwSiygGzLuk8cynYS/giphy.gif', 'https://media.giphy.com/media/4TrJMNlfxyg2H2nhx0/giphy.gif',
                            'https://media.giphy.com/media/pzKRxS42FLK81ZPz5C/giphy.gif', 'https://media.giphy.com/media/SG5paY6WxH6Ki2lWys/giphy.gif',
                            'https://media.giphy.com/media/fs6gcc4CxMTY5bAGyn/giphy.gif', 'https://media.giphy.com/media/1fmA4DHlleNG016sLE/giphy.gif',
                            'https://media.giphy.com/media/cNDb41n8Xv7C5j6hOO/giphy.gif', 'https://media.giphy.com/media/AhXOqQ7ts5J8Ri6V6P/giphy.gif'])


    embed=discord.Embed()
    embed=discord.Embed(title=" Here is a Fortnite Dance For You ! <:verified:419067353545048064>", url="{}".format(ctx.message.author.avatar_url))
    embed.set_author(name="Dance Requested By {}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
    embed.set_image(url=catfcho)
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    await bot.send_message(ctx.message.channel, embed=embed)


@bot.command(pass_context=True)
async def fortnite_drop (ctx):
    fdrop = random.choice(['Anarchy Acres','Dsuty Divot','Fatal Fields','Flush Factory','Greasy Grove','Haunted Hills','Junk Junktion','Lonely Lodge',
                                'Loot Lake','Lucky Landing','Moisty Mire','Pleasant Park','Retail Row','Risky Reels','Salty Springs','Shifty Shafts','Snobby Shores',
                                'Tilted Towers','Tomato Town','Wailing Woods'])

    embed=discord.Embed(title="You Should Drop ", url="https://cdn.discordapp.com/attachments/418005628255207424/462605605451071488/E7sI6zfOcqLf29xXX3311RL6F0MmTsvZkWhLAAAAAElFTkSuQmCC.png", description="\n**{}**\n".format(fdrop))
    embed.set_author(name="Fortnite Drop", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/462605605451071488/E7sI6zfOcqLf29xXX3311RL6F0MmTsvZkWhLAAAAAElFTkSuQmCC.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/418005628255207424/462605605451071488/E7sI6zfOcqLf29xXX3311RL6F0MmTsvZkWhLAAAAAElFTkSuQmCC.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def dog (ctx):
    dogcho = random.choice(['https://i.imgur.com/WcjwkUc.jpg', 'https://i.imgur.com/HSfhT9I.jpg',
                    'https://i.imgur.com/o2ryxRR.jpg', 'https://i.imgur.com/uBF6wqR.jpg',
                    'https://i.imgur.com/3Pu3DWL.jpg', 'https://i.imgur.com/4eVcOst.jpg',
                    'https://i.imgur.com/ypfT4Yn.jpg', 'https://i.imgur.com/AZpS0pF.jpg'])


    embed=discord.Embed()
    embed=discord.Embed(title=" Here is a Cute Dog For You ! :dog:", url="{}".format(ctx.message.author.avatar_url))
    embed.set_author(name="Dog Requested By {}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
    embed.set_image(url=dogcho)
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    await bot.send_message(ctx.message.channel, embed=embed)


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def troll(ctx, user: discord.Member = None):
    if user is None:
        await bot.send_message(ctx.message.channel,"<:Fail:461924435176325120> Mention a User to Troll !")

    else:
        await bot.send_message(ctx.message.channel,"{} **WAS BANNED** <a:TROLLDANCE:437631542446129163>  ".format(user.mention))
        await bot.delete_message(ctx.message)

@bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    pingtime = time.time()
    embed=discord.Embed(description="**Pong !...**")
    pingms = await bot.send_message(ctx.message.channel, embed=embed)
    await asyncio.sleep(2)
    ping = (time.time() - pingtime) * 1000
    embed.add_field(name=":ping_pong:", value="It Took Me :-\n**%d Micro Seconds**" % ping , inline=True)
    await bot.edit_message(pingms,embed=embed)

@bot.command(pass_context = True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def support(ctx):
    await bot.say("Need Help ? **Join Support Server :-** https://discord.gg/S6gDBqr, \n**Use the Special Command** `<askhelp <Your Question>` <a:yo:445638905874743302>")

@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def tankibot (ctx):
    await bot.say("**{}** , Here is the Best Bot I Would Recommend for Tanki Online\nLink :-https://discordbots.org/bot/408439037771382794\nBot Server:- https://discord.gg/cDH6VJg".format(ctx.message.author.name))

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick (ctx ,user : discord.Member = None , *args):
    channel = discord.utils.get(ctx.message.server.channels, name='hello-logs', type=discord.ChannelType.text)
    kReason = ' '.join(args)
    try:
        if user is None:
            await bot.say("<:Fail:461924435176325120> Mention a User to Kick !")
        else:
            if channel:
                if not user.avatar_url:
                    avaa = user.default_avatar_url
                else:
                    avaa = user.avatar_url
                embed=discord.Embed(title="{} Was Kicked".format(user.name))
                embed.set_author(name=user.name, icon_url=avaa)
                embed.set_thumbnail(url=avaa)
                embed.add_field(name="User Name", value=user.name, inline=True)
                embed.add_field(name="User ID", value=user.id, inline=True)
                embed.add_field(name="Admin/Mod", value=ctx.message.author.mention, inline=True)
                embed.add_field(name="Channel", value="<#{}>".format(ctx.message.channel.id), inline=True)
                embed.add_field(name="Reason", value=kReason, inline=False)
                embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
                await bot.send_message(channel , embed=embed)
                await bot.kick(user)
                await bot.say("**{}** Was Kicked From **{} |** <:Pass:461924196390404106> ".format(user , ctx.message.server.name))
                await bot.send_message(user, "You Were Kicked From {} , {}".format(ctx.message.server.name , kReason))
            else:
                await bot.delete_message(ctx.message)
                await bot.create_channel(ctx.message.server, "hello-logs", type=discord.ChannelType.text)
                await bot.say("<:Pass:461924196390404106> Channel Hello-Logs Were Created As The Log Channel(Required) , Try Again The Command !") #
    except:
        await bot.say("<:Fail:461924435176325120> Something is Wrong !")

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def ban (ctx ,user : discord.Member = None , *args):
    channel = discord.utils.get(ctx.message.server.channels, name='hello-logs', type=discord.ChannelType.text)
    kReason = ' '.join(args)
    try:
        if user is None:
            await bot.say("<:Fail:461924435176325120> Mention a User to Ban !")
        else:
            if channel:
                if not user.avatar_url:
                    avaa = user.default_avatar_url
                else:
                    avaa = user.avatar_url
                embed=discord.Embed(title="{} Was Banned".format(user.name))
                embed.set_author(name=user.name, icon_url=avaa)
                embed.set_thumbnail(url=avaa)
                embed.add_field(name="User Name", value=user.name, inline=True)
                embed.add_field(name="User ID", value=user.id, inline=True)
                embed.add_field(name="Admin/Mod", value=ctx.message.author.mention, inline=True)
                embed.add_field(name="Channel", value="<#{}>".format(ctx.message.channel.id), inline=True)
                embed.add_field(name="Reason", value=kReason, inline=False)
                embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
                await bot.send_message(channel , embed=embed)
                await bot.ban(user)
                await bot.say("**{}** Was Banned From **{} |** <:Pass:461924196390404106> ".format(user , ctx.message.server.name))
                await bot.send_message(user, "You Were Banned From {} , {}".format(ctx.message.server.name , kReason))
            else:
                await bot.delete_message(ctx.message)
                await bot.create_channel(ctx.message.server, "hello-logs", type=discord.ChannelType.text)
                await bot.say("<:Pass:461924196390404106> Channel Hello-Logs Were Created As The Log Channel(Required) , Try Again The Command !") #
    except:
        await bot.say("<:Fail:461924435176325120> Something is Wrong !")




@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def c_mute (ctx , user:discord.Member = None , *args):
   channel = discord.utils.get(ctx.message.server.channels, name='hello-logs', type=discord.ChannelType.text)
   reason = ' '.join(args)
   try:
        if channel:
            if user is None:
                await bot.say("<:Fail:461924435176325120> Mention a User to Mute in the Channel !")
            else:
                if user.avatar_url:
                    ava = user.avatar_url
                else:
                    ava = user.default_avatar_url
                if reason == "":
                    await bot.say("<:Fail:461924435176325120> Provide a Reason !")

                overwrite = discord.PermissionOverwrite()
                overwrite.read_messages = True
                overwrite.send_messages = False
                await bot.edit_channel_permissions(ctx.message.channel, user, overwrite)
                embed=discord.Embed(title="{} Was Muted In Channel".format(user.name))
                embed.set_author(name=user.name, icon_url=user.avatar_url)
                embed.set_thumbnail(url=ava)
                embed.add_field(name="User Name", value=user.name, inline=True)
                embed.add_field(name="User ID", value=user.id, inline=True)
                embed.add_field(name="Admin/Mod", value=ctx.message.author.mention, inline=True)
                embed.add_field(name="Channel", value="<#"+ctx.message.channel.id+">", inline=True)
                embed.add_field(name="Reason", value=reason, inline=False)
                embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
                await bot.send_message(channel, embed=embed)
                await bot.say("**{}** Was Muted in This Channel In **{} |** <:Pass:461924196390404106>".format(user , ctx.message.server.name ))
                await bot.delete_message(ctx.message)
                await bot.send_message(user , "You Were Muted In {} , {}".format(ctx.message.server.name , reason))


        else:
            await bot.delete_message(ctx.message)
            await bot.create_channel(ctx.message.server, "hello-logs", type=discord.ChannelType.text)
            await bot.say("<:Pass:461924196390404106> Channel Hello-Logs Were Created As The Log Channel(Required) , Try Again The Command !")
   except:
        await bot.say("<:Fail:461924435176325120> Something is Wrong !")

@bot.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
async def changenick (ctx , user : discord.Member = None , *args):
    msg = ' '.join(args)
    channel = discord.utils.get(ctx.message.server.channels, name='hello-logs', type=discord.ChannelType.text)
    try:
        if channel:
            if user is None:
                await bot.say("<:Fail:461924435176325120>  Mention a User to Change Nickname !")
            elif msg == "":
                await bot.say("<:Fail:461924435176325120>  Nickname is Empty !")
            else:
                if user.avatar_url:
                    av = user.avatar_url
                else:
                    av = user.default_avatar_url

                embed=discord.Embed(title="{}'s Nickname Changed".format(user.name))
                embed.set_author(name=user.name , icon_url=av)
                embed.set_thumbnail(url=av)
                embed.add_field(name="User Name", value=user.name, inline=True)
                embed.add_field(name="User ID", value=user.id, inline=True)
                embed.add_field(name="Admin/Mod", value=ctx.message.author.mention, inline=True)
                embed.add_field(name="Nickname Changed" , value=msg, inline=True)
                embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
                await bot.send_message(channel , embed=embed)

                await bot.change_nickname(user, msg)
                await bot.delete_message(ctx.message)
                await bot.say("**{}'s** Name Was Changed to **{}** In **{} |** <:Pass:461924196390404106>".format(user , msg , ctx.message.server.name))
        else:
            await bot.delete_message(ctx.message)
            await bot.create_channel(ctx.message.server, "hello-logs", type=discord.ChannelType.text)
            await bot.say("<:Pass:461924196390404106> Channel Hello-Logs Were Created As The Log Channel(Required) , Try Again The Command !")
    except:
        await bot.say("<:Fail:461924435176325120> Something is Wrong !")


@bot.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def warn(ctx , user : discord.Member = None ,*args ):
    channel = discord.utils.get(ctx.message.server.channels, name='hello-logs', type=discord.ChannelType.text)
    msg = ' '.join(args)

    try:
        if channel:
            if user is None:
                await bot.say("<:Fail:461924435176325120>  Mention a User to Warn !")
            else:
                if user.avatar_url:
                    av = user.avatar_url
                else:
                    av = user.default_avatar_url

                embed=discord.Embed(title="{} Warned".format(user.name))
                embed.set_author(name=user.name, icon_url=av)
                embed.set_thumbnail(url=av)
                embed.add_field(name="User Name", value=user.mention, inline=True)
                embed.add_field(name="User ID", value=user.id, inline=True)
                embed.add_field(name="Admin/Mod", value=ctx.message.author.mention, inline=True)
                embed.add_field(name="Channel", value="<#"+ctx.message.channel.id+">", inline=True)
                embed.add_field(name="Reason", value=msg, inline=False)
                embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
                await bot.send_message(channel , embed=embed)

                await bot.delete_message(ctx.message)
                await bot.send_message(user , "You Were Warned In {} , {}".format(ctx.message.server.name , msg))
                await bot.say("**{}** Was Warned In **{} |** <:Pass:461924196390404106>".format(user , ctx.message.server.name))
        else:
            await bot.delete_message(ctx.message)
            await bot.create_channel(ctx.message.server, "hello-logs", type=discord.ChannelType.text)
            await bot.say("<:Pass:461924196390404106> Channel Hello-Logs Were Created As The Log Channel(Required) , Try Again The Command !")
    except:
        await bot.say("<:Fail:461924435176325120> Something is Wrong !")

@bot.command(pass_context=True)
async def suggest(ctx , *args):
    try:
        suggest = ' '.join(args)
        suggestC = discord.utils.get(ctx.message.server.channels, name='suggestions', type=discord.ChannelType.text)
        if suggestC:
            await bot.say("{} , Your Suggestion Was Sent In ! **|** <:Pass:461924196390404106>".format(ctx.message.author.mention))
            await bot.delete_message(ctx.message)
            await bot.send_message(suggestC , "**User:-** {}\n**Suggestion:-** {}".format(ctx.message.author.mention , suggest))
        else:
            await bot.delete_message(ctx.message)
            await bot.create_channel(ctx.message.server, "suggestions", type=discord.ChannelType.text)
            await bot.say("<:Pass:461924196390404106> Channel Suggestions Were Created As The Suggestions Channel(Required) , Try Again The Command !")

    except:
        await bot.send_message(ctx.message.author , "<:Fail:461924435176325120> Something is Wrong !")


@bot.command(pass_context=True)
async def report(ctx , user:discord.Member = None , *args):
    try:
        report = ' '.join(args)
        reports = discord.utils.get(ctx.message.server.channels, name='reports', type=discord.ChannelType.text)
        if reports:
            if user is None:
                await bot.say("<:Fail:461924435176325120>  Usage :- `<report [user] [report]`")
            else:
                await bot.say("{} , Your Report Was Sent In ! **|** <:Pass:461924196390404106>".format(ctx.message.author.mention))
                await bot.send_message(reports , "**User:-** {}\n**Violater:-** {}\n**Report:-** {}".format(ctx.message.author.mention , user.mention , report ))
                await bot.delete_message(ctx.message)
                await bot.send_message(user , "You Were Reported In {} , {}".format(ctx.message.server.name , report))
        else:
            await bot.delete_message(ctx.message)
            await bot.create_channel(ctx.message.server, "reports", type=discord.ChannelType.text)
            await bot.say("<:Pass:461924196390404106> Channel Reports Were Created As The Reports Channel(Required) , Try Again The Command !")

    except:
        await bot.send_message(ctx.message.author , "<:Fail:461924435176325120> Something is Wrong !")


@bot.command(pass_context=True)
async def leave (ctx , *args):
    try:
        args = ' '.join(args)
        if message.author.id == bot.user.owner.id:
            server = bot.get_server(args)
            await bot.leave_server(server)
        else:
            return
    except:
        await ("Scanner ! , Ummm !")

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def c_unmute (ctx , user:discord.Member = None , *args):
   channel = discord.utils.get(ctx.message.server.channels, name='hello-logs', type=discord.ChannelType.text)
   try:
        if channel:
            if user is None:
                await bot.say("<:Fail:461924435176325120> Mention a Muted User to Unmute in the Channel !")
            else:
                if user.avatar_url:
                    ava = user.avatar_url
                else:
                    ava = user.default_avatar_url
                await bot.delete_channel_permissions(ctx.message.channel, user)

                embed=discord.Embed(title="{} Was Unmuted In Channel".format(user.name))
                embed.set_author(name=user.name, icon_url=user.avatar_url)
                embed.set_thumbnail(url=ava)
                embed.add_field(name="User Name", value=user.name, inline=True)
                embed.add_field(name="User ID", value=user.id, inline=True)
                embed.add_field(name="Admin/Mod", value=ctx.message.author.mention, inline=True)
                embed.add_field(name="Channel", value="<#"+ctx.message.channel.id+">", inline=True)
                embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
                await bot.send_message(channel, embed=embed)
                await bot.say("**{}** Was Unmuted in This Channel In **{} |** <:Pass:461924196390404106>".format(user , ctx.message.server.name ))
                await bot.delete_message(ctx.message)

        else:
            await bot.delete_message(ctx.message)
            await bot.create_channel(ctx.message.server, "hello-logs", type=discord.ChannelType.text)
            await bot.say("<:Pass:461924196390404106> Channel Hello-Logs Were Created As The Log Channel , Try Again The Command !")
   except:
       await bot.say("<:Fail:461924435176325120> Something is Wrong !")


@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def info(ctx):
    embed=discord.Embed(title="Info About The Bot", url="https://discord.gg/QP6ZdwK")
    embed.set_author(name="Hello Discord Bot", url="https://discord.gg/QP6ZdwK", icon_url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    embed.add_field(name="Servers", value="{:,}".format (len(bot.servers)), inline=True)
    embed.add_field(name="Channels", value="{:,}".format (len([c for c in bot.get_all_channels()])), inline=True)
    embed.add_field(name="Users", value="{:,}".format (len(set(bot.get_all_members()))), inline=True)
    embed.add_field(name="Discord API Version",value="{}".format(discord.__version__), inline=True)
    embed.add_field(name="Library", value="Python", inline=True)
    embed.add_field(name="Running On", value="Windows 10 x64", inline=True)
    embed.add_field(name="Library Version", value="3.6.4", inline=True)
    embed.add_field(name="Owner", value="<@429118689367949322>", inline=True)
    embed.add_field(name="Invite Link", value="[Link](https://discordapp.com/oauth2/authorize?client_id=445544179310002176&scope=bot&permissions=267779302)", inline=True)
    embed.set_footer(text="Hello Discord Bot | 2018 | Scanner#4797",icon_url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def insult(ctx , name: discord.Member = None):
    if name is None:
        await bot.say("<:Fail:461924435176325120> Mention a User to Insult !")
    else:
        await bot.delete_message(ctx.message)
        await bot.send_message(ctx.message.channel, random.choice([  ":skull: **|** {} , You’re So Ugly That When You Cry, The Tears Roll Down The Back Of Your Head…Just To Avoid Your Face.".format(name),
                                                                    ":skull: **|** {} , No Need For Insults, Your Face Says It All".format(name.mention),
                                                                    ":skull: **|** {} , People Like You Are The Reason We Have Middle Fingers.".format(name.mention),
                                                                    ":skull: **|** {} , Tell Me… Is Being Stupid A Profession Or Are You Just Gifted?".format(name.mention),
                                                                    ":skull: **|** {} , Why Don’t You Slip Into Something More Comfortable. Like A Coma?".format(name.mention),
                                                                    ":skull: **|** {} , When Your Mom Dropped You Off At The School, She Got A Ticket For Littering.".format(name.mention),
                                                                    ":skull: **|** {} , Zombies Eat Brains. You’re Safe, Because You’re a Type Of It !".format(name.mention),
                                                                    ":skull: **|** {} , What’s The Point Of Putting On Makeup, A Monkey Is Gonna Stay A Monkey.".format(name.mention),
                                                                    ":skull: **|** {} , It’s Not That You Are Weird…It’s Just That Everyone Else Is Normal.".format(name.mention),
                                                                    ":skull: **|** {} , It’s Not That I’m Smarter Than You, Its Just That You’re Dumber Than Everyone Else.".format(name.mention),
                                                                    ":skull: **|** {} , Act Your Age Not Your Shoe Size.".format(name.mention),
                                                                    ":skull: **|** {} , Scientists Are Trying To Figure Out How Long Human Can Live Without A Brain. You Can Tell Them Your Age.".format(name.mention),
                                                                    ":skull: **|** {} , Stupidity Is Not A Crime So You Are Free To Go.".format(name.mention),
                                                                    ":skull: **|** {} , Jealousy Is A Disease…Get Well Soon!".format(name.mention),
                                                                    ":skull: **|** {} , Everyone Has The Right To Be Stupid, But You’re Abusing The Privilege.".format(name.mention),
                                                                    ":skull: **|** {} , Just Keep Talking, I Yawn When I’m Interested.".format(name.mention),
                                                                    ":skull: **|** {} , Your Are The Reason , God To Make A Middle Finger".format(name.mention),
                                                                    ":skull: **|** {} , You’re So Much Smarter When You Don’t Speak!**".format(name.mention),
                                                                    ":skull: **|** {} , You’re So Ugly, When You Were Born, The Doctor Said “Wheres The Baby?”".format(name.mention),
                                                                    ":skull: **|** {} , You’re So Ugly, When You Were Born, Your Parents Sued The Doctor.".format(name.mention),
                                                                    ":skull: **|** {} , You’re So Ugly, When You Were Born, Your Parents Asked For A Refund. ".format(name.mention),
                                                                    ":skull: **|** {} , You’re So Ugly, When You Were Born, The Doctor Was The One Screaming Instead Of Your Mother.".format(name.mention),
                                                                    ":skull: **|** {} , Where Were You When God Was Giving Out Common Sense?".format(name.mention),
                                                                    ":skull: **|** {} , If I Hurt Your Feelings In Any Way I Just Want To Know From The Bottom Of My Heart That I Don’t Care.".format (name.mention),
                                                                    ":skull: **|** {} , Your Are The Reason That HD Leave Tanki Online" .format(name.mention)]))

@bot.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def open1(ctx , user : discord.Member = None):
     cho8 = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])

     embed=discord.Embed(description="<:411277821357457428:447650450024431626> **Opening a Container** <:411277821357457428:447650450024431626>",color=0x111111)
     x = await bot.send_message(ctx.message.channel , embed=embed)
     await asyncio.sleep(0.3)
     embed=discord.Embed(title="Container Opened", description=cho8, color=0x111111)
     embed.set_author(name="Container ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
     embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
     x = await bot.edit_message(x , embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 20, commands.BucketType.user)
async def open10(ctx):

    cho = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])

    cho2 = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])

    cho3 = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])

    cho4 = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])

    cho5 = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])

    cho6 = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])

    cho7 = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])

    cho8 = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])

    cho9 = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])

    cho10 = random.choice(["<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 ":regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 ":a: **|** You've just received **250 of all Supplies** ",
                                                                 ":regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 ":regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 ":regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"])


    embed=discord.Embed(description="**Opening Containers** <:411277821357457428:447650450024431626>",color=0x111111)
    x = await bot.send_message(ctx.message.channel , embed=embed)
    await asyncio.sleep(1.5)

    embed=discord.Embed(title="Container Opened", description=cho, color=0x111111)
    embed.set_author(name="Container 1 ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    x = await bot.edit_message(x , embed=embed)
    await asyncio.sleep(2.5)

    embed=discord.Embed(title="Container Opened", description=cho2, color=0x111111)
    embed.set_author(name="Container 2 ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    x = await bot.edit_message(x , embed=embed)
    await asyncio.sleep(2.5)

    embed=discord.Embed(title="Container Opened", description=cho3, color=0x111111)
    embed.set_author(name="Container 3 ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    x = await bot.edit_message(x , embed=embed)
    await asyncio.sleep(2.5)

    embed=discord.Embed(title="Container Opened", description=cho4, color=0x111111)
    embed.set_author(name="Container 4 ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    x = await bot.edit_message(x , embed=embed)
    await asyncio.sleep(2.5)

    embed=discord.Embed(title="Container Opened", description=cho5, color=0x111111)
    embed.set_author(name="Container 5 ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    x = await bot.edit_message(x , embed=embed)
    await asyncio.sleep(2.5)

    embed=discord.Embed(title="Container Opened", description=cho6, color=0x111111)
    embed.set_author(name="Container 6 ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    x = await bot.edit_message(x , embed=embed)
    await asyncio.sleep(2.5)

    embed=discord.Embed(title="Container Opened", description=cho7, color=0x111111)
    embed.set_author(name="Container 7 ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    x = await bot.edit_message(x , embed=embed)
    await asyncio.sleep(2.5)

    embed=discord.Embed(title="Container Opened", description=cho8, color=0x111111)
    embed.set_author(name="Container 8 ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    x = await bot.edit_message(x , embed=embed)
    await asyncio.sleep(2.5)

    embed=discord.Embed(title="Container Opened", description=cho9, color=0x111111)
    embed.set_author(name="Container 9 ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    x = await bot.edit_message(x , embed=embed)
    await asyncio.sleep(2.5)

    embed=discord.Embed(title="Container Opened", description=cho10 , color=0x111111)
    embed.set_author(name="Container 10 ", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/456751945185493004/389886353430544387.png")
    embed.set_footer(text=ctx.message.server.name , icon_url=ctx.message.server.icon_url)
    x = await bot.edit_message(x , embed=embed)

async def tutorial_uptime():
    await bot.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not bot.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1

bot.loop.create_task(tutorial_uptime())
bot.run(os.getenv("TOKEN"))
