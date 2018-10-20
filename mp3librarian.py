# Renames mp3 files based on id3 tags, creates a folder structure and moves the files around accordingly.
# Google's archaic naming system and distaste for locally stored music made me do this.
# Pekka Sinkkonen 20.10.2018



import os
import eyed3
import eyed3.mp3
import datetime
import string


# Prompt for path
wrkdir = input('''To ensure the sanctity of your existing library, 
move the files you want to be sorted into a separate directory and enter it's path here: ''')
os.chdir(wrkdir)

# Make a list of the files (and folders) in the working directory
files = os.listdir(wrkdir)
print(files)

for i in files:
    # Ignore folders
    if os.path.isdir(i):
       continue
    # Ignore everything except mp3 files
    if not eyed3.mp3.isMp3File(i):
        continue

    audiofile = eyed3.load(i)                   
    date = audiofile.tag.getBestDate()
    date_string = str(date.year)

    # Check for artist and album directories, and create one if it doesn't exist
    if not os.path.exists(audiofile.tag.artist + '\\' + date_string + ' - ' + audiofile.tag.album):
        os.makedirs(audiofile.tag.artist + '\\' + date_string + ' - ' + audiofile.tag.album)

    albumdir = (audiofile.tag.artist + '\\' + date_string + ' - ' + audiofile.tag.album)
    track = str(audiofile.tag.track_num[0])
    if len(track) < 2:
        track = '0' + track

    os.rename(i, albumdir + '\\' + track + ' - ' + audiofile.tag.title + '.mp3')




















