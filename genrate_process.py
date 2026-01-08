#this file look for new folder inside user uploads and convert them into reel if they are not already converted
import os
import time
from text_to_audio import text_to_speech_file
def text_to_audio(folder):
    print("TTA -",folder)
    with open(f"reel_genrator/user_uploads/{folder}/desc.txt") as f:
        text=f.read()
    print(text,folder)
    # text_to_speech_file(text,folder)
    

def create_reel(folder):
    print("CR -",folder)


if __name__=="__main__":
    while True:
        print("processing queue....")
        with open("reel_genrator/done.txt","r") as f:
            done_folders=f.readlines()
        done_folders=[f.strip()for f in done_folders]
        folders=os.listdir("reel_genrator/user_uploads")
        for folder in folders:
            if(folder not in done_folders):
                text_to_audio(folder) #generat4e the audio from desc.txt
                create_reel(folder) #convert the image and audio.inside the folder to a reel
                with open("reel_genrator/done.txt","a")as f:
                    f.write(folder+"\n")
        time.sleep(4)