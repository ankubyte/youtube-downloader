import yt_dlp,json,humanfriendly
from datetime import datetime

def video_info(url):
    ydl_opts = {
    "format": "best",
    "no_warnings": True, 
    }
    vid_info={}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info=ydl.extract_info(url=url,download=False)
    best = info["formats"][-1] 

    size = best.get("filesize") or best.get("filesize_approx")

    duration=humanfriendly.format_timespan(info['duration'])
    vid_info['Title']= info['title']
    vid_info['Creator']= info['creator']
    vid_info['Total likes']= info['like_count']
    vid_info['Duration']= duration
    vid_info[' Total size']= f"{size / (1024*1024):.2f} MB"

    return vid_info
     
def yt_down(url):
    ydl_opts = {
    "format": "best",
    "no_warnings": True,

    }
    print('downloading...')
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

while True:
    link=input("Enter Video Link: ").strip()
    # print('Showing video information...')
    download=video_info(link)
    print("Video informations...")
    for x,y in download.items():
        print(f'{x}={y}')
    choise=input(f'Do You want to download?\nEnter y/n >>>').strip()
    if choise.lower()!='n':
        yt_down(link)
    else:
        break