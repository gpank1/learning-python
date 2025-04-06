# Discord bot for playing music
# author: @gpank1


# Discord library
# Communicates with Discord API, handles events, command parsing and execution, voice channel connectivity
import discord
from discord.ext import commands
# Handles everything related to retrieving audio
# Searching YouTube for songs
# Fetching video metadata
# Downloading audio streams
# Converts video formats to audio formats
# Supports various video platforms beyond YouTube
import youtube_dl
# Manages timeouts for asynchronous operations
# Helps prevent the bot from getting stuck if operations take too long
# Used for timing out voice connections and downloads
import asyncio
from async_timeout import timeout
import functools
import itertools
import math
import random

# YouTube DL options
ytdl_format_options = {
    'format': 'bestaudio/best', # Prioritize audio quality
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s', # Output filename template
    'restrictfilenames': True, # Avoid illegal filename characters
    'noplaylist': True, # Don't download entire playlists
    'nocheckcertificate': True, # Don't verify SSL certificates
    'ignoreerrors': False, # Stop on errors
    'logtostderr': False, # Don't log to stderr
    'quiet': True, # Don't print messages to console
    'no_warnings': True, # Don't print warnings
    'default_search': 'auto', # Auto-search if not a URL
    'source_address': '0.0.0.0', # Bind to this IP
}