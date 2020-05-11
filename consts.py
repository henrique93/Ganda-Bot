#consts.py

#---------------------------- SOUNDS ----------------------------
#join sound path
joinSoundPath = "audio//Join//"

#jajao
jajao = "audio//Highlander//Play//last_surprise.mp3"

#yt_dl options
ytdl_opts = {
    'format' : 'bestaudio/best',
    'postprocessors' : [{
        'key' : 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality' : '192'
    }]
}
