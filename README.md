# Multi-Purpose Discord Bot Commands

Welcome to the repository! This repository showcases the code of my upcoming Discord bot, Imperial. It's an ambitious project aimed at creating a comprehensive multi-purpose bot designed to enhance the Discord experience. Currently equipped with essential moderation tools, Imperial is on a path of continuous development to integrate a wide array of features.

## Current Features
- **Slash Commands Support**
- **Sync**: Synchronize new commands.
- **tempmute**: Temporarily silence members to maintain order in your channels.
- **Ban list**: Get user IDs of members in the ban list.
- **Unmute**: Unmute members.
- **Kick Members**: Punish bad behavior by throwing members out of the server.
- **Ban Members**: Keep your server safe by banning disruptive members.
- **Unban Members**: Allow members another chance by lifting bans when appropriate.
- **Purge Messages**: Clean up your chat by bulk-deleting messages quickly and efficiently.
- **Softban**: Ban & unban members at the same time.
- **Restriction**: Restrict members from accessing the server.
- **Embed Creator**: Create customizable embed messages with the help of the Dispie library.
- **Server Boost Event**: Manage server boosters.


## Installing the Discord.py Library and Setting Up a Discord Bot

To create and set up your own Discord bot, you'll first need to install the `discord.py` library.

Follow these steps to install `discord.py` and set up your bot:

1. Visit the official `discord.py` [documentation](https://discordpy.readthedocs.io/en/stable/intro.html) for detailed installation instructions.

2. Ensure you have Python 3.8 or higher installed, as it is a prerequisite for using `discord.py`.

## Setting Up Your Discord Bot

3. Create your bot account on the Discord Developer Portal. This is where you'll get your bot token, which is essential for your bot to log in and interact on Discord servers.

4. Once your bot account is set up, you'll receive a unique token. **Never share this token with anyone**, as it allows full access to your bot. Store it securely and use it in your bot's login code.

5. To add your bot to a server, you'll need to generate an invite URL with the appropriate permissions. You can do this from the bot's application page on the Discord Developer Portal. The URL will look something like this: `https://discordapp.com/oauth2/authorize?client_id=YOUR_BOT_CLIENT_ID&scope=bot&permissions=PERMISSIONS_INTEGER`. Replace `YOUR_BOT_CLIENT_ID` with your bot's client ID and `PERMISSIONS_INTEGER` with the permissions your bot needs, encoded as an integer.



## Getting Started with the Bot

To get the bot up and running on your own server, follow these steps:

1. **Clone the Repository**
   First, clone the repository to your local machine using Git. Open your terminal and run:
   ```bash
   git clone https://github.com/zLEXTRO/Multi-Purpose-Discord-Bot-Project-Imperial-.git
   ```

2. **Navigate to the Bot Directory**
   Change into the directory where the bot code is located:
   ```bash
   cd Multi-Purpose-Discord-Bot-Project-Imperial-
   ```

3. **Install Dependencies**
   Install all the required dependencies for the bot to work. If you have a `requirements.txt` file, you can use the following command:
   ```bash
   pip install -r requirements.txt
   ```
Requirements Files, are just a list of pip install arguments placed into a file. 

For better installation method visit [this](https://docs.discloudbot.com/v/en/suport/languages/python/requirements.txt) Document.

4. **Insert Your Discord Token**
   Open the bot's main file `Imperial.py` in a text editor. Scroll all the way down to the last line of the code where the Discord token is supposed to be set, which might look like this:
   ```python
   bot.run('BOT_TOKEN')
   ```
   Replace `YOUR_DISCORD_TOKEN` with the token you obtained from the Discord Developer Portal.

5. **Run the Bot**
   Start your bot by running the main script file. This might be something like:
   ```bash
   python Imperial.py
   ```
   or if you're using a launcher script:
   ```bash
   ./start_Imperial.sh
   ```

6. **Verify the Bot is Running**
   After starting the bot, check your Discord server to see if the bot appears online. If it does, try out some of the commands to ensure it's functioning correctly.
Example: `-rise`
Remember to keep your Discord token private and never share it with anyone. If you suspect that your token has been compromised, regenerate it immediately on the Discord Developer Portal.
```

## Contributing
I welcome contributions from the community. Whether it's feature suggestions, bug reports, or code contributions, your input is valuable.
