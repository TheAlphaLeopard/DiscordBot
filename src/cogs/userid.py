"""
/userid is a simple command that echoes back the user's Discord ID.
"""

import discohook

@discohook.command.slash('userid', description='Shows your Discord user ID')
async def userid_command(interaction):
    user_id = interaction.user.id
    username = interaction.user.name
    
    response = f"Hello {username}!\nYour Discord User ID is: `{user_id}`"
    
    await interaction.response.send(response)