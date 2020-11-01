import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?')

budget = 0
budgetList = {}
market = {'wheat': 1840, 'barley': 1440, 'gram': 4620}

@client.event
# ready check
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Necro down! Commands wont work'))
    print("Bot is ready")

@client.command()
async def setBudget(ctx, b):
    global budget
    budget = int(b)
    await ctx.send(f"Your budget has been set to {b}")

@client.command()
async def checkBudget(ctx):
    global budget, budgetList
    total = 0
    msg = f"Your total budget for the month is: {budget}\n"
    for k in budgetList:
        msg += f"{k} -> {budgetList[k]}\n"
        total += int(budgetList[k])
    if budget >= total:
        await ctx.send(f"Congrats, you're making savings this month!")
    else:
        await ctx.send(f"You're requirements are a bit too high for your income. Consider reducing some or increasing your pay")
    await ctx.send(msg)


@client.command()
async def addToBudget(ctx, title, money):
    global budgetList
    budgetList[str(title)] = int(money)
    await ctx.send(f"{title} added to budget!")


@client.command()
async def checkPrice(ctx, crop, quintal):
    global market
    price = market[crop] * int(quintal)
    await ctx.send(f"You can sell you {quintal} of {crop} for {price} INR")

client.run('NzIyNjkwNzgxNTI1MTgwNDM3.XxfEbQ.NQ5x2_k6i3pss0RU_rAzwRZtVy4')
