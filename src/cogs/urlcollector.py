"""
/collect-urls command collects all external URLs from recent messages in the channel.
"""

import re
import discohook
from typing import List

URL_PATTERN = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

@discohook.command.slash('collect-urls', description='Collect all URLs from recent messages')
async def collect_urls_command(interaction, limit: int = 100):
    # Defer the response since message history fetch might take time
    await interaction.response.defer()
    
    # Get message history
    messages = await interaction.channel.history(limit=limit).flatten()
    
    # Extract URLs from messages
    urls: List[str] = []
    for message in messages:
        found_urls = re.findall(URL_PATTERN, message.content)
        if found_urls:
            urls.extend(found_urls)
    
    if not urls:
        await interaction.followup.send("No URLs found in the recent messages!")
        return
    
    # Format response
    response = "Found URLs in recent messages:\n\n"
    for i, url in enumerate(urls, 1):
        response += f"{i}. {url}\n"
        
    # Split response if too long
    if len(response) > 2000:
        response = response[:1997] + "..."
        
    await interaction.followup.send(response)