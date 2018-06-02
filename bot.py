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

bot = discord.Client()
bot_prefix= "<"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_command(command, ctx):
    chane = bot.get_channel("451696010914299905")
    await bot.send_message(chane,'Command -- `<{}` Server: `{}` | `{}` User: `{}` | `{}`'.format(command,
            ctx.message.server.name,
            ctx.message.server.id,
            ctx.message.author.name,
            ctx.message.author.id))

@bot.event
async def on_server_join(server):
    channel = bot.get_channel("452352293275172894")
    await bot.send_message(server.owner ,"Hey There ! I am Hello , A Discord Bot By Scanner#4797")
    await bot.send_message(channel, "**The bot has just joined a new server! :tada:**\n **Server name:** {}\n **Total members:** {:,}".format(server.name,len(server.members)))

@bot.event
async def on_server_remove(server):
    channel = bot.get_channel("452352293275172894")
    await bot.send_message(channel, "**The bot has just left a server! :cry:**\n **Server name:** {}\n **Total members:** {:,}".format(server.name,len(server.members)))

@bot.event
async def on_member_join(member):
    server = member.server
    if server.id == "433182340211146752":
        #Test Server#
        channel = bot.get_channel("433182340211146754")
        server = member.server
        msg = "**:tada: Welcome to {} {}. You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        await bot.send_message(channel, msg)

    elif server.id == "418001869781205002":
        #Scanner#
        channel1 = bot.get_channel("418001869781205004")
        server = member.server
        msg = "**:tada: Welcome to {} {}. You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        await bot.send_message(channel1, msg)

    elif server.id == "419567438452097027":
        #Games Server (Prince)#
        channel1 = bot.get_channel("419567438972059649")
        server = member.server
        msg = "**:tada: Welcome to {} {}. You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        await bot.send_message(channel1, msg)
    
    elif server.id == "446967025773051905":
        #hello
        chan = bot.get_channel("446972812712738816")
        server = member.server
        msg = "**:tada: Welcome to {} {}. You are the {} User!**".format(member.server.name, member.mention, len(server.members))
        await bot.send_message(chan, msg)
    else:
        return

@bot.event
async def on_member_remove(member):
    server = member.server
    if server.id == "419567438452097027":
        channel = bot.get_channel("419567438972059649")
        msg = ":wave: ** {} Has Just Left the Server !**".format(member)
        await bot.send_message(channel, msg)

    else:
        return



        

print("Logging...")


@bot.event
async def on_ready():
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Users: {}".format(len(set(bot.get_all_members()))))
    await bot.change_presence(game=discord.Game(name="<HELP | {} Users ".format(len(set(bot.get_all_members()))),type=3))

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.BadArgument):
        await bot.send_message(ctx.message.channel," :x: Bad Argument")
    elif isinstance(error, commands.CommandNotFound):
        chan =  bot.get_channel ("451695928336842753")
        await bot.send_message(chan, "{} Used Not Avalible Command On {} With Server ID {}" .format(ctx.message.author.mention , ctx.message.server.name , ctx.message.server.id))
    elif isinstance(error, commands.CheckFailure):
        await bot.send_message(ctx.message.channel, "You Don't Have Enough  Permissions to Excute this Command ! :x:")
    elif isinstance(error, discord.errors.Forbidden):
        await bot.send_message(ctx.message.author , ":x: Missing Permissions to Excute the Command !")


    else:
        await bot.send_message(ctx.message.channel , "Something is Wrong ! :x:")

bot.remove_command("help")
@bot.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="Help is Here (Prefix "<")", url="https://discord.gg/SsndPjB")
    embed.set_author(name="Help", icon_url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
    embed.add_field(name="<:discord:450901180097363968> Discord Daily Commands", value="`afk-back` - Set a AFK Status\n`count` - Tell How Many Messages You have Sent in The Channel\n`serverinv` - Gives You a Server Invite of the Server\n`servericon` - Bring Out the Server Icon\n`serverinfo` - Shows Server Information\n`avatar` - Shows the Avatar of a User\n`userinfo` - Shows Info of a User", inline=True)
    embed.add_field(name=":trophy:  Moderation Commands", value="`clear` - Delete Bulk-Messages\n`getbans` - Gives a Banned Members List\n`cmute` - Mutes a User in a Channel<:Premium:447648813331513354>\n`cunmute` - Unmutes the Muted user in the Channel<:Premium:447648813331513354>\n`smute` - Mute a User in Server <:Premium:447648813331513354>\n`sunmute` - Unmutes the user muted in the Server <:Premium:447648813331513354>\n`report` - Send a Report Message for a Certain Channel <:Premium:447648813331513354>\n`ban` - Ban Members in the Server <:Premium:447648813331513354>\n`kick` - Kicks a User from the Server <:Premium:447648813331513354>\n`warn` - Warn a User <:Premium:447648813331513354>", inline=False)
    embed.add_field(name=":joy: Fun Commands", value="`yay` - IDK You Check!\n`virus` - Send a Virus to Your Friend\n`insult` - Insult a User By Mentioning Them\n`lovecal` - Check Love Percentage Between You and Your Friend\n`troll` - Test the Command :)\n`hug` - Hug a User\n`rps paper` - Play R.P.S With the Bot\n`rps rock` - Play R.P.S With the Bot\n`rps scissor` - Play R.P.S With the Bot\n`8ball` - Ask a 8Ball Question\n`tell` - Say Something as the Bot", inline=False)
    embed.add_field(name="<:tanki:447387948086722560> Tanki Online Commands", value="`open10` - Open 10 Containers :)\n`open1` - Open a Conatiner\n`tankibot` - Gives the Invite Link of the Tanki Bot\n`play` - Get The Tanki Online Playing Link\n`tolinks`  - All Tanki Useful Links\n`vlog`- Check the latest Tanki V-LOG", inline=False)
    embed.add_field(name=":robot: Bot Info Commands", value="`info` - Gives Some Info About the Bot\n`ping` - Check the bot response time\n`reqpre` - Request Premium and Check Advantages\n`support` - Gives You Support Info\n`askhelp` - Ask Help From Bot Owners\n`invite` - Get the Invite Link Other Links of the Bot", inline=True)
    embed.add_field(name=":information_source: Information", value="`reqpre` - Request Hello Premium \n<:Premium:447648813331513354> This Type Of Commands Work Only For Premium Users ($1) Month Per User , ($3) For a Server", inline=True)
    embed.set_footer(text="Hello Bot | 2018 | Scanner #4797 | Help" ,icon_url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
    await bot.say(embed=embed)



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    elif message.content.startswith('<reqpre'):
        text = message.content[len('<report'):].strip()

        pre = bot.get_channel("451696819638894592")
        await bot.send_message(message.channel ,"Your Request Has Been Sent ! :tada:\nGood Luck For The Approval  ")
        await bot.send_message(pre ,"User:- {}\nID:- {}\nMessage:- {} ".format(message.author.mention , message.author.id ,text))
        await bot.delete_message(message)



    elif message.content.startswith('<report'):
        ###-Scanner's Server-###
        if message.server.id == "418001869781205002":
            log = bot.get_channel ("418004548523655169")
            sent = bot.get_channel("419143404631621652")
            text = message.content[len('<report'):].strip()
            await bot.delete_message(message)

            embed=discord.Embed()
            embed.add_field(name="REPORT", value="**User:** {}\n**Channel:**<#{}>\n**Report:**{}".format(message.author.mention , message.channel.id , text), inline=True)
            embed.set_footer(text="{} | User ID: {}".format(message.server.name , message.author.id),icon_url="{}".format(message.server.icon_url))
            await bot.send_message(message.channel , "**{}** , Your Report Has Sent In !".format(message.author.name))
            await bot.send_message(sent,embed=embed)
            embed=discord.Embed(title="<:Premium:447648813331513354> Hello Premium Users | New Report")
            embed.set_author(name="{}".format(message.server.name), icon_url="{}".format(message.server.icon_url))
            embed.add_field(name="User", value=" {}".format(message.author), inline=True)
            embed.add_field(name="Channel", value=" <#{}>".format(message.channel.id), inline=True)
            embed.add_field(name="Report:", value=" {}".format(text), inline=False)
            embed.set_footer(text="User: {} | ID: {}".format(message.author.name , message.author.id) ,icon_url="{}".format(message.author.avatar_url))
            await bot.send_message(log, embed=embed)
            await bot.delete_message(message)

        elif message.server.id == "419567438452097027":
            #prince
            sent = bot.get_channel("428191385557139456")
            text = message.content[len('<report'):].strip()
            await bot.delete_message(message)

            embed=discord.Embed()
            embed.add_field(name="REPORT", value="**User:** {}\n**Channel:**<#{}>\n**Report:**{}".format(message.author.mention , message.channel.id , text), inline=True)
            embed.set_footer(text="{} | User ID: {}".format(message.server.name , message.author.id),icon_url="{}".format(message.server.icon_url))
            await bot.send_message(message.channel , "**{}** , Your Report Has Sent In !".format(message.author.name))
            await bot.send_message(sent,embed=embed)
            #embed=discord.Embed(title="<:Premium:447648813331513354> Hello Premium Users | New Report")
            #embed.set_author(name="{}".format(message.server.name), icon_url="{}".format(message.server.icon_url))
            #embed.add_field(name="User", value=" {}".format(message.author), inline=True)
            #embed.add_field(name="Channel", value=" <#{}>".format(message.channel.id), inline=True)
            #embed.add_field(name="Report:", value=" {}".format(text), inline=False)
            #embed.set_footer(text="User: {} | ID: {}".format(message.author.name , message.author.id) ,icon_url="{}".format(message.author.avatar_url))
            #await bot.send_message(log, embed=embed)
            #await bot.delete_message(message)

        else:
            await bot.send_message(message.channel , ":x: This Server or The User Doesn't Have Hello Premium to Excute this Command <:Premium:447648813331513354>")





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

    elif message.content.startswith("<askhelp"):
        text = message.content[len('<askhelp'):].strip()
        channel = bot.get_channel("451695948704382978")
        await bot.send_message(message.channel, "{} Your Message Has Been Sent In !" .format(message.author.mention))
        await bot.send_message(message.author, "**Hey There !**\nWe Successfully Recorded You Issue !\n\n Issue ID :- {}\n Please be Patient... Until We Check !".format(message.server.id))
        await bot.send_message(channel,"**User:-** <@{}>\n**Server:-** {} , {} \n**Problem:-** {}".format(message.author.id, message.server.name , message.server.id ,text))
        await bot.delete_message(message)


    elif message.content.startswith('<vlog'):

        embed=discord.Embed(title="Episode 172")
        embed.set_author(name="Tanki Online V-LOG", icon_url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
        embed.add_field(name="Link ...", value="[Click Here](https://www.youtube.com/watch?v=l2W-wRBlfeo&t=2s)", inline=True)
        embed.set_footer(text="Tanki Online | Hello | 2018", icon_url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
        await bot.send_message(message.channel,embed=embed)

    elif message.content.startswith('<reqreport'):
        if message.author.id == message.server.owner.id:
            if message.server.id == "418001869781205002":
                await bot.send_message(message.channel , "Your Server Has Report Command Already ! :x:")
            else:
                name = message.content[len("<reqreport"):].strip()
                chann = bot.get_channel("450276717614071809")
                invitelinknew = await bot.create_invite(destination =message.channel, xkcd = True, max_uses = 100)
                await bot.send_message(chann ,"New Request\n\n**Server Name:-**{}\n**Server ID:-**{}".format(message.server.name , message.server.id))
                await bot.send_message(chann ,"**Text:-** {}".format(name))
                await bot.send_message(chann ,"**Link:-** {}".format(invitelinknew))
                await bot.send_message(message.author ,"Hey There !\nYou Have Request Report Command For \n\n**Server Name:-** {}\n**Owner Name:-**{}\n Please Be Patient Until We Do it !\nYou Will Get a Message Once it is Done ! , Thank You ! ".format(message.server.name , message.server.owner.name))
                await bot.send_message(message.channel,"Success \nI Sent a Message to My Technical Team !")
        else:
            await bot.send_message(message.channel , "Your Are Not the Server Owner to Do this Command ! :x:")



    elif message.content.startswith('<afk'):
        name = message.content[len("<afk"):].strip()
        if "@everyone" in name:
            await bot.send_message(message.channel , ":x: -{}-".format(message.author))
        elif "@here" in name:
            await bot.send_message(message.channel , ":x: -{}-".format(message.author))

        else:
            await bot.send_message(message.channel, '**{}** , I Have Set Your AFK : {}'.format(message.author.name , name))

        def check(msg):
            return msg.content.startswith('<back')

        message = await bot.wait_for_message(author=message.author, check=check)

        await bot.send_message(message.channel, "Welcome Back **{}** , I Removed Your AFK Status".format (message.author.name))

    elif message.content.startswith('<Hey Hello'):
        if message.author.id == "429118689367949322":
            await bot.send_message(message.channel, "Hey {} !\n**Founder , Technical Staff , Suppport Team** ".format(message.author.mention))

        else:
              await bot.send_message(message.channel,"Hey {} !\n **Player**".format(message.author.mention))



    await bot.process_commands(message)




@bot.command(pass_context = True)
#@commands.has_permissions(manage_channels=True)
async def cmute(ctx, *, member : discord.Member):
    '''Mutes A Memeber'''
    #user_roles = [r.name.lower() for r in ctx.message.author.roles]

    #if "admin" not in user_roles:
    #    return await client.say("You do not have the role: Admin")
    #pass
    await bot.send_message(ctx.message.channel , ":x: This Server or The User Doesn't Have Hello Premium to Excute this Command <:Premium:447648813331513354>")

#Unmutes a member

@bot.command(pass_context = True)
@commands.has_permissions(manage_channels=True)
async def cunmute(ctx, *, member : discord.Member):
    await bot.send_message(ctx.message.channel , ":x: This Server or The User Doesn't Have Hello Premium to Excute this Command <:Premium:447648813331513354>")



@bot.command(pass_context=True)
async def premium(ctx):
    await bot.say("Hello Premium<:Premium:447648813331513354>\nAllows You To Use Premium Commands\nType `<help` To Check premuim Commands\n$1 For a User , $3 For a Server ")



@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban (ctx, user: discord.Member = None):
    botlog = bot.get_channel("433182340211146755")
    text = ctx.message.content[len("<ban"):].strip()
    try:
        #Test Server#
        if ctx.message.server.id == "433182340211146752":
            if user is None:
                await bot.say(":x: Mention a User to BAN!")
            elif user.id == ctx.message.author.id:
                await bot.say(":x: You Cannot Ban Your Self :face_palm: ")
            elif user.id == ctx.message.server.owner.id:
                await bot.say(":x: You Cannot Ban Your Boss !")
            else:
                await bot.send_message(ctx.message.channel , "{} Was Banned From {} :white_check_mark:".format(user, ctx.message.server.name))
                await bot.ban(user)
                await bot.send_message(user,"You Have Been Banned From **{}** , {}".format(ctx.message.server.name, text))
                embed=discord.Embed(title="New Ban ! {}".format(ctx.message.server.name))
                embed.set_author(name="{}".format(ctx.message.server.name), icon_url=ctx.message.server.icon_url)
                embed.add_field(name="Admin or Mod", value=ctx.message.author, inline=True)
                embed.add_field(name="Channel", value=ctx.message.channel.name, inline=True)
                embed.add_field(name="Banned User ID", value=user.id, inline=True)
                embed.add_field(name="Reason", value=text, inline=True)
                await bot.send_message(botlog ,embed=embed)
        else:
            await bot.send_message(ctx.message.channel , ":x: This Server or The User Doesn't Have Hello Premium to Excute this Command <:Premium:447648813331513354>")

    except :
        if discord.errors.Forbidden:
            await bot.say("Missing Permissions , I Need `KICK_MEMBERS` Permission To Do This :()")
        else:
             await bot.say(":x: Something Went Wrong !")



@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick (ctx , user: discord.Member = None ):
    botlog = bot.get_channel("433182340211146755")
    text = ctx.message.content[len("<kick"):].strip()
    try:
        #Test Server#
        if ctx.message.server.id == "433182340211146752":
            if user is None:
                await bot.say(":x: Mention a User to KICK !")
            if user.id == ctx.message.author.id:
                await bot.say(":x: You Cannot KICK Your Self :face_palm: ")
            if user.id == ctx.message.server.owner.id:
                await bot.say(":x: You Cannot Kick Your Boss !")
            else:
                await bot.send_message(ctx.message.channel , "{} Was Kicked From {} :white_check_mark:".format(user, ctx.message.server.name))
                await bot.kick(user)
                await bot.send_message(user,"You Have Been Kicked From **{}** , {}".format(ctx.message.server.name, text))
                embed=discord.Embed(title="New KICK ! {}".format(ctx.message.server.name))
                embed.set_author(name="{}".format(ctx.message.server.name), icon_url=ctx.message.server.icon_url)
                embed.add_field(name="Admin or Mod", value=ctx.message.author, inline=True)
                embed.add_field(name="Channel", value=ctx.message.channel.name, inline=True)
                embed.add_field(name="KICK User ID", value=user.id, inline=True)
                embed.add_field(name="Reason", value=text, inline=True)
                await bot.send_message(botlog ,embed=embed)
        else:
            await bot.send_message(ctx.message.channel , ":x: This Server or The User Doesn't Have Hello Premium to Excute this Command <:Premium:447648813331513354>")

    except :
        if discord.errors.Forbidden:
            await bot.say("Missing Permissions , I Need `KICK_MEMBERS` Permission To Do This :()")
        else:
             await bot.say(":x: Something Went Wrong !")

@bot.command(pass_context=True)
async def yay(ctx):
    await bot.say("https://media.giphy.com/media/3kvYEldEEr0DC/giphy.gif")


@bot.command(pass_context=True)
async def tolinks(ctx):
    await bot.send_message(ctx.message.channel,"**Tanki Online Useful Links**\n\nTanki Online Official :- https://tankionline.com/\nTanki Online Ratings :-https://ratings.tankionline.com/en/\nTanki Online Forum :-https://en.tankiforum.com/\nTanki Online Wiki :-https://en.tankiwiki.com/Tanki_Online_Wiki/\nTanki Online Help:- https://help.tankionline.com/\n\n **Tanki Online EN | Hello 2018**")

@bot.command(pass_context=True)
async def servericon(ctx):
    embed=discord.Embed(title="{} Icon URL".format(ctx.message.server.name), url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
    embed.set_image(url=ctx.message.server.icon_url)
    embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.server.icon_url)
    embed.set_footer(text="Requested By {} | {}".format(ctx.message.author.name , ctx.message.server.name) , icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
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
async def avatar(ctx, user: discord.Member = None):
    if not user:
        embed=discord.Embed()
        embed.set_author(name="{}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
        embed=discord.Embed(title="Your Avatar Link", url="{}".format(ctx.message.author.avatar_url), color=0x070707)
        embed.set_author(name="{}".format(ctx.message.author.name), icon_url="{}".format(ctx.message.author.avatar_url))
        embed.set_image(url=ctx.message.author.avatar_url)
        embed.set_footer(text="{}".format(ctx.message.server.name),icon_url="{}".format(ctx.message.server.icon_url))
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
async def userinfo(ctx, user: discord.Member = None):
    if user is None:
        embed=discord.Embed(title="{}'s Information".format(ctx.message.author.name), url=ctx.message.author.avatar_url)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.add_field(name="User Name", value=ctx.message.author.name, inline=True)
        embed.add_field(name="User Tag", value="#" + ctx.message.author.discriminator, inline=True)
        embed.add_field(name="User ID", value=ctx.message.author.id, inline=True)
        embed.add_field(name="User Status", value=ctx.message.author.status, inline=True)
        embed.add_field(name="User Top Role", value=ctx.message.author.top_role, inline=True)
        embed.add_field(name="User Mention", value=ctx.message.author.mention, inline=True)
        embed.add_field(name="User Joined On", value=ctx.message.author.joined_at, inline=True)
        embed.set_footer(text="{}".format(ctx.message.server.name) ,icon_url="{}".format(ctx.message.server.icon_url))
        await bot.say(embed=embed)

    else:
        embed=discord.Embed(title="{}'s Information".format(user.name), url=user.avatar_url)
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="User Name", value=user.name, inline=True)
        embed.add_field(name="User Tag", value="#" + user.discriminator, inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="User Status", value=user.status, inline=True)
        embed.add_field(name="User Top Role", value=user.top_role, inline=True)
        embed.add_field(name="User Mention", value=user.mention, inline=True)
        embed.add_field(name="User Joined On", value=user.joined_at, inline=True)
        embed.set_footer(text="{}".format(ctx.message.server.name) ,icon_url="{}".format(ctx.message.server.icon_url))
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hug(ctx, *, member: discord.Member = None):
    try:
        if member is None:
            await bot.say(ctx.message.author.mention + " Has Been Hugged! :heart:")
        else:
            if member.id == ctx.message.author.id:
                await bot.say(ctx.message.author.mention + " Has Hugged Him Self!")
            else:
                await bot.say(member.mention + " Has Been Hugged By " + ctx.message.author.mention + "! :heart:")
    except:
        await bot.say("**Eww Something Went Wrong** :x:")

@bot.command(pass_context=True)
async def lovecal(ctx , user: discord.Member = None):
    if user is None:
        await bot.say(":x: Mention a User to Check The Love Percenatge")
    if user.id == ctx.message.author.id:
        embed=discord.Embed(color=0x040404)
        embed.add_field(name=":heart: Love Calculator",value="Love Percentage between {} and {}\n **0%**".format(ctx.message.author.mention , user.mention), inline=False)
        await bot.send_message(ctx.message.channel,embed=embed)
    else:
        embed=discord.Embed(color=0x040404)
        embed.add_field(name=":heart: Love Calculator", value="Love Percentage between {} and {}\n **{}%**".format(ctx.message.author.mention , user.mention , random.randint(1,100)), inline=False)
        await bot.send_message(ctx.message.channel,embed=embed)

@bot.command(pass_context=True)
async def warn(ctx):
    await bot.send_message(ctx.message.channel , ":x: This Server or The User Doesn't Have Hello Premium to Excute this Command <:Premium:447648813331513354>")

@bot.command(pass_context = True)
async def play(ctx):
    embed=discord.Embed(title="Go Ahead Play Tanki Click The Link ", url="https://tankionline.com/battle-en.html#/", color=0x070707)
    embed.set_author(name="Play Tanki Online ", icon_url="https://cdn.discordapp.com/attachments/433182340211146754/447402587822620673/8475ec065fffc1db1d0a9470a529ce67.jpg")
    embed.add_field(name=":link: Click To Play" , value="[Link Click To Start Blasting Enemy Tanks !](https://tankionline.com/battle-en.html#/)", inline=False)
    embed.set_footer(text="Hello | Tanki Online EN | 2018 ",icon_url="https://cdn.discordapp.com/avatars/445544179310002176/6843573388ba5ae8092b234c8b35bc2e.webp?size=1024")
    await bot.say(embed=embed)

@bot.command(pass_context = True)
async def invite(ctx):
    embed=discord.Embed(title="Invite Links", url="https://discord.gg/UWsfvzK", color=0x0d0d0d)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    embed.set_author(name="Hello Bot", icon_url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    embed.add_field(name=":link:  Invite Hello Bot", value="[Click To Invite](https://discordapp.com/oauth2/authorize?client_id=445544179310002176&scope=bot&permissions=267779302)", inline=True)
    embed.add_field(name=":link: Offcial Hello Site", value="[Click Here to Vist](https://hello-bot.wixsite.com/hello-discord)", inline=False)
    embed.add_field(name=":tada:  Vote Me Discord Bot List", value="[Click To Vote](https://discordbots.org/bot/445544179310002176)", inline=False)
    embed.add_field(name=":tools: Join Support Server", value="[Click Here To Join](https://discord.gg/S6gDBqr)", inline=True)
    embed.set_footer(text="Hello Bot | 2018 | Scanner#4797" , icon_url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
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
async def getbans(ctx):
    if not ctx.message.author.server_permissions.administrator:
        return

    else:
        x = await bot.get_bans(ctx.message.server)
        x = '\n'.join([y.name for y in x])
        embed = discord.Embed(title = "<a:SARC:437630981034213376> List of Banned Members For {}".format(ctx.message.server.name), description = x, color=0x080808)
        return await bot.say(embed = embed)


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)



@bot.command(pass_context=True)
async def eye(ctx):
    chan = ctx.message.channel
    x = await bot.send_message(chan , "o.O xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "O.o xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "o.O xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "O.o xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "o.O xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "O.o xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "o.O xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "O.o xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "o.O xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "O.o xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "o.O xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "O.o xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "o.O xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "O.o xD")
    await asyncio.sleep(1)
    x = await bot.edit_message(x , "o.O xD")
    
  






   



    
@bot.command(pass_context=True)
async def virus(ctx, user: discord.Member = None):
    if user is None:
        await bot.say(":x: Mention a User to Send Virus ! ")
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
async def troll(ctx, user: discord.Member = None):
    if user is None:
        await bot.send_message(ctx.message.channel,":x: Mention a User to Troll !")

    else:
        await bot.send_message(ctx.message.channel,"{} **WAS BANNED** <a:TROLLDANCE:437631542446129163>  ".format(user.mention))
        await bot.delete_message(ctx.message)

@bot.command(pass_context = True)
async def ping(ctx):
    pingtime = time.time()
    embed=discord.Embed(description="Pong !...")
    pingms = await bot.send_message(ctx.message.channel, embed=embed)
    await asyncio.sleep(2)
    ping = (time.time() - pingtime) * 1000
    embed.add_field(name=":ping_pong:", value="It Took Me :-\n**%d Micro Seconds**" % ping , inline=True)
    await bot.edit_message(pingms,embed=embed)

@bot.command(pass_context = True)
async def support(ctx):
    await bot.say("Need Help ? **Join Support Server :-** https://discord.gg/S6gDBqr, \n**Use the Special Command** `<askhelp <Your Question>` <a:yo:445638905874743302>")

@bot.command(pass_context=True)
async def tankibot (ctx):
    await bot.say("**{}** , Here is the Best Bot I Would Recommend for Tanki Online\nLink :-https://discordbots.org/bot/408439037771382794\nBot Server:- https://discord.gg/cDH6VJg".format(ctx.message.author.name))

@bot.command(pass_context=True)
async def info(ctx):
    embed=discord.Embed(title="Info About The Bot", url="https://discord.gg/QP6ZdwK")
    embed.set_author(name="Hello Discord Bot", url="https://discord.gg/QP6ZdwK", icon_url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    embed.add_field(name="Servers", value="{}".format (len(bot.servers)), inline=True)
    embed.add_field(name="Channels", value="{}".format (len([c for c in bot.get_all_channels()])), inline=True)
    embed.add_field(name="Users", value="{}".format (len(set(bot.get_all_members()))), inline=True)
    embed.add_field(name="Discord API Version",value="{}".format(discord.__version__), inline=True)
    embed.add_field(name="Library", value="Python", inline=True)
    embed.add_field(name="Running On", value="Windows 10 x64", inline=True)
    embed.add_field(name="Library Version", value="3.6.4", inline=True)
    embed.add_field(name="Owner", value="<@429118689367949322>", inline=True)
    embed.add_field(name="Invite Link", value="[Link](https://discordapp.com/oauth2/authorize?client_id=445544179310002176&scope=bot&permissions=267779302)", inline=True)
    embed.set_footer(text="Hello Discord Bot | 2018 | Scanner#4797",icon_url="https://cdn.discordapp.com/avatars/445178799932440576/6843573388ba5ae8092b234c8b35bc2e.jpg?size=2048")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def insult(ctx , name: discord.Member = None):
    if name is None:
        await bot.say(":x: Mention a User to Insult !")

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

@bot.command(pass_context = True)
async def open1(ctx):
    await bot.send_message(ctx.message.channel, random.choice (["**Container 1**\n\n<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**. ",
                                                                 "**Container 1**\n\n<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "**Container 1**\n\n<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "**Container 1**\n\n<:nb:447648823507157012> **|** You've just received **125 Speed Boost**. ",
                                                                 "**Container 1**\n\n<:mine:447651503210233866> **|** You've just received **125 Mines**. ",
                                                                 "**Container 1**\n\n<:Crystals:447647301826117634> **|** You've just received **3,500 Crystals**.",
                                                                 "**Container 1**\n\n<:armor:447647517597892638> **|** You've just received **125 Double Armor**.",
                                                                 "**Container 1**\n\n<:dd:447648822265380867> **|** You've just received **125 Double Damage**.",
                                                                 "**Container 1**\n\n:regional_indicator_p: **|** You've just received **Mosaic Paint** !",
                                                                 "**Container 1**\n\n<:Premium:447648813331513354> **|** You've just received **3 days of Premium Account** ",
                                                                 "**Container 1**\n\n:a: **|** You've just received **250 of all Supplies** ",
                                                                 "**Container 1**\n\n:regional_indicator_p: **|** You've just received **Frost paint** ",
                                                                 "**Container 1**\n\n<:eternity:447648817282547723> **|** You've just received **Eternity Paint** ",
                                                                 "**Container 1**\n\n<:riprip:419067396779933707> **|** You've just received **System Cant Read The Item** ",
                                                                 "**Container 1**\n\n<:gold:447648811779620864> **|** You've just received **10 Gold Boxes** ",
                                                                 "**Container 1**\n\n<:gold:447648811779620864> **|** You've just received **5 Gold Boxes** ",
                                                                 "**Container 1**\n\n<:gold:447648811779620864> **|** You've just received **999999 Gold Boxes** ! Man Stop Using Hack ",
                                                                 "**Container 1**\n\n:regional_indicator_p: **|** You've just received **Spark Paint** ! Go Ahead You Just Look Like Claudiu",
                                                                 "**Container 1**\n\n<:Crystals:447647301826117634> **|** You've just received **25.000 Crystals** !" ,
                                                                 "**Container 1**\n\n<:411277821357457428:447650450024431626> **|** You've just received **Conatainer x5** ! Sounds Good !",
                                                                 "**Container 1**\n\n:regional_indicator_p: **|** You've just received **Vanadium Paint** ! ",
                                                                 "**Container 1**\n\n<:riprip:419067396779933707> **|** You've just received a **Slap** From Community Manager For Hacking a The Yesterday RIP Bro !"]))


@bot.command(pass_context=True)
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



    x = await bot.send_message(ctx.message.channel , "<:411277821357457428:447650450024431626>  Opening Containers... <:411277821357457428:447650450024431626> ")
    await asyncio.sleep(1.5)
    x = await bot.edit_message(x ,"**Container 1**\n\n" + cho )
    await asyncio.sleep(2.5)
    x = await bot.edit_message(x ,"**Container 2**\n\n{}".format(cho2))
    await asyncio.sleep(2.5)
    x = await bot.edit_message(x ,"**Container 3**\n\n{}".format(cho3))
    await asyncio.sleep(2.5)
    x = await bot.edit_message(x ,"**Container 4**\n\n".format(cho4))
    await asyncio.sleep(2.5)
    x = await bot.edit_message(x ,"**Container 5**\n\n{}".format(cho5))
    await asyncio.sleep(2.5)
    x = await bot.edit_message(x ,"**Container 6**\n\n{}".format(cho6))
    await asyncio.sleep(2.5)
    x = await bot.edit_message(x ,"**Container 7**\n\n{}".format(cho7))
    await asyncio.sleep(2.5)
    x = await bot.edit_message(x ,"**Container 8**\n\n{}".format(cho8))
    await asyncio.sleep(2.5)
    x = await bot.edit_message(x ,"**Container 9**\n\n{}".format(cho9))
    await asyncio.sleep(2.5)
    x = await bot.edit_message(x ,"**Container 10**\n\n{}".format(cho10))


bot.run(os.getenv("TOKEN"))

