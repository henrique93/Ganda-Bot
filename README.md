# Ganda-Bot
![Avatar](Avatar.png "Ganda bot avatar")

[Discord](https://discord.com) bot using [discord.py](https://discordpy.readthedocs.io/en/latest/)


[Heroku](https://www.heroku.com) buildpacks:

[Python](heroku/python) / [ffmpeg](https://github.com/kitcast/buildpack-ffmpeg.git) / [libopus](https://github.com/codeinteger6/heroku-buildpack-libopus.git)

### Features:
+ Flip - Flip a coin. Result heads or tails;
+ Highlander - Kick every member from the current voice channel except for one;
+ Init - Keeps the bot connected to one voice channel;
+ Destroy - Disconnects the bot from a voice channel;
+ Mute - Keeps a member server muted;
+ Unmute - Stops server muting a member;
+ Russian roulette - Kicks one member from the current voice channel;
+ Shuffle - Moves every member in the current voice channel to random voice channels;
+ The bot has a queue for sounds
+ Play - Plays a sound:
    + "Play" followed by a sound from the list plays that sound;
    + "Play" followed by a youtube URL plays it's audio;
    + "Play random" - Plays a random sound from the list;
    + "Play ariana" - Plays a random Ariana Grande song.
+ Pause - Pauses the current sound;
+ Resume - Resumes the current sound;
+ Stop - Stops playing the current sound and clears the queue;
+ Skip - Skips the current sound and plays the next one in queue;
+ The bot removes user messages commanding him to play/pause/skip/stop/resume sounds to avoid spam in channels
+ When certain members join a voice chat, the bot plays a random sound assigned to them;
+ When members leave a voice channel the bot plays a sound;
+ When members self deafen when in a voice channel the bot plays a sound;
+ When members self undeafen when in a voice channel the bot plays a sound;
+ When members don't have permission to performe an action plays a sound;
+ The bot automatically disconnects from the voice channel if there are no other non-bot members connected to that channel;
+ Gives specific members specific roles when they join the server;
+ Gives specific members specific nicknames when they join the server.
