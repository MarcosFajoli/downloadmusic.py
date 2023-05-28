import os
import pafy
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GOOGLE_API_ID')
MAIN_PATH = os.getenv('MAIN_PATH')

youtube = build('youtube', 'v3', developerKey=API_KEY)

arq = open("lista.txt")
url_playlists = arq.readlines()

typeaudio = input("Qual o formato de áudio preferido?: ")

for url_playlist in url_playlists:
    pl_params = url_playlist.split(" -- ")
    pl_params[0] = pl_params[0].split("list=")[1]

    playlist_videos = []
    nextPage_token = None

    while True:
        res = youtube.playlistItems().list(part='snippet', playlistId = pl_params[0], maxResults=50, pageToken=nextPage_token).execute()
        playlist_videos += res['items']
        
        nextPage_token = res.get('nextPageToken')

        if nextPage_token is None:
            break

    
    print("Número total de vídeos na playlist: ", len(playlist_videos))
    os.mkdir(MAIN_PATH + "/audio/%s" % pl_params[1])

    print(f"Downloading playlist \"{pl_params[1]}\"")

    for info_video in playlist_videos:
        try:
            print("Trying to download %s" % info_video['snippet']['title'])

            video = pafy.new(info_video['snippet']['resourceId']['videoId'])
            sound = video.getbestaudio(preftype=typeaudio)
            print("Size is %s" % sound.get_filesize())
            filename = sound.download(quiet=False, filepath=MAIN_PATH + "/audio/%s" % pl_params[1]) 
        except Exception:
            print(f"An error occurred while downloading the video \"{info_video['snippet']['title']}\": {Exception};")
    
    print(f"Playlist \"{pl_params[1]}\"")

