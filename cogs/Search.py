from disnake.ext import commands

from utils.bot import OGIROID


class Search(commands.Cog):
    """Search stuff"""

    def __init__(self, bot: OGIROID):
        self.bot = bot

    @commands.slash_command(description="Returns a google search for your query")
    async def google(self, inter, query):
        """Googles the keyword entered"""
        query = query.rstrip().replace(" ", "+")
        await inter.send(f"https://www.google.com/search?q={query}")

    @commands.slash_command(name="feeling-lucky", description="Returns the first google result for your query")
    async def lucky(self, inter, query):
        """Googles the keyword entered and returns the first result"""
        query = query.rstrip().replace(" ", "+")
        await inter.send(f"https://www.google.com/search?q={query}&btnI")

    @commands.slash_command(description="Returns a StackOverflow search for your query")
    async def stackoverflow(self, inter, query):
        """Searches StackOverflow for the query"""
        query = query.rstrip().replace(" ", "+")
        await inter.send(f"https://stackoverflow.com/search?q={query}")


def setup(bot: commands.Bot):
    bot.add_cog(Search(bot))