from pytube import YouTube
import os
import moviepy.editor as mp
from colorama import Fore, Back, Style
from pathlib import Path


Downloads = str(Path.home() / "Downloads")


def on_complete(stream, path):
    print("Do you want  an audio for this "+Fore.GREEN+"(y)"
    +"\033[39m"+" or "+Fore.RED+"(n)"+"\033[39m"+" | "+Fore.GREEN+"(Y)"
    +"\033[39m"+" or "+Fore.RED+"(N)"+"\033[39m")
    choice = input("Choice: ")
    if choice == 'y' or choice == 'Y':
        clip = mp.VideoFileClip(path)
        clip.audio.write_audiofile(path+".mp3")
    os.startfile(Downloads+r"\Youtube")

def displayViews(views):
    if views/1000000 >= 1:
        return  f"{round(views/1000000,2)} Millions Views"
    elif views/1000 >= 1:
        return f"{round(views/1000,2)} Thousands Views"
    else:
        return views

def on_progress(stream, chuck, remaining):
    print(Fore.BLUE+f'{100-(remaining*100/stream.filesize)} %'+"\033[39m")

def main ():
    print(Fore.RED+"****** Youtube Downloader ******"+"\033[39m")

    link = input("Video Link: ")

    video = YouTube(link, on_complete_callback=on_complete, on_progress_callback=on_progress)

    print(Fore.GREEN+"Video Title: "+"\033[39m"+video.title)
    print(Fore.GREEN+"Author     : "+"\033[39m"+video.author)
    print(Fore.GREEN+"Views      : "+"\033[39m"+displayViews(video.views))

    print(Fore.RED+"\nIs it the right video?\nChoose:"+"\033[39m")

    print(Fore.GREEN+"(Y)"+"\033[39m"+" or "+Fore.GREEN+"(y)"+"\033[39m"+" to download or any other key to exit"+"\033[39m")

    choice = input(" Choice: ")

    if choice == "y" or choice == "Y":
        video.streams.get_highest_resolution().download(Downloads+r'\Youtube')
    else:
        print(Fore.RED+"Thank you !!"+"\033[39m")


canDownload = True

while(canDownload):
 
    main()
 
    print("\n Do you want to download another video"+Fore.GREEN
    +" (y/Y) "+"\033[39m"+"or "
    +Fore.RED+"(n/N)"+"\033[39m")

    choice = input("Choice: ")
 
    if choice == "Y" or choice == "y":
        canDownload = True
    else:
        canDownload = False


