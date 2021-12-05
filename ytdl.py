# Source Code : X - Nabil354
# github.com/nabilhnzm354

# instalation #
# pip install -r require.txt

import moviepy.editor
from pytube import YouTube, Playlist

# System Color
cyan  = '\x1b[36m'

# ========================================= MAIN CODE =========================================   #

def DownladerYt():
    print('\n\n=================================YOUTUBE SERVER DOWNLOADER======================================\n\nList Server :\n[1]. PlayList\n[2]. Audio\n[3]. Video\n Example : 1')
    choose = input('Choose Your Type : ')
    if choose=='1':
        urlPlaylist = input('Masukkan URL Youtube Playlist : ')
        playlist = Playlist(urlPlaylist)
        print('Total Videos In PLaylist : %s' % len(playlist.video_urls))
        for video_url in playlist.video_urls:
            print('\n\n' + video_url)
        print('\n\nDone...')
    elif choose=='2':
        urlVideo = input('Masukkan URL Youtube Video : ')
        queryTitle = input('Input Name For Audio : ')
        yt = YouTube(urlVideo)
        result = yt.streams.get_highest_resolution().download('download')
        video = moviepy.editor.VideoFileClip(result)
        audio = video.audio

        audio.write_audiofile(queryTitle + '.mp3')
        print('Done...')
    elif choose=='3':
        urlVideo = input('Masukkan URL Youtube Video : ')
        yt = YouTube(urlVideo)
        yt.streams.get_highest_resolution().download('download')
        print('Done...')
    else:
      print('Gabener Anjing')
      
# DEFAULT SYSTEM MAIN
if __name__=="__main__":
    while True:
        try:
            DownladerYt()
        except KeyboardInterrupt:
                print('{}\nOke Byeee....'.format(cyan))
                exit()
