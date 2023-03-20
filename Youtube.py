from pytube import *  # for youtube downloader
import os  # use  of directory and file


def video():  # """Video Download Defination"""
    try:
        # take link from user
        link = input(">>Please Paste Your Youtube Video Link Here : ")
        yt = YouTube(link)

        yt.streams.filter(mime_type="video/mp4").get_highest_resolution().download(
            output_path="C:\\Users\Public\Youtube_Downloads")

############## Here is working for title and file name ##############
        print(
            f"\n>>Title: {yt.title[0:30]}...video(720p) has been successfully downloaded")
        print(">>Saved Location >> C:\\Users\Public\Youtube_Downloads\n")
    except Exception as e:
        print(f"\nWarning! Please Provide Proper Link. {e} \n")


def audio():  # """Audio Download Defination"""
    try:
        # take link from user
        link = input(">>Please Paste Your Youtube Video Link Here : ")
        yt = YouTube(link)
        aud = yt.streams.filter(only_audio=True).get_audio_only().download(
            output_path="C:\\Users\Public\Youtube_Downloads")

############## Here is working for Rename mp4 file to mp3 ##############
        base, ext = os.path.splitext(aud)
        new_file = base + '.mp3'
        os.rename(aud, new_file)

############## Here is working for title and file name ##############
        print(
            f"\n>>Title: {yt.title[0:30]}...audio has been successfully downloaded")
        print(">>Saved Location >> C:\\Users\Public\Youtube_Downloads\n")
    except Exception as e:
        print(f"\nWarning! Please Provide Proper Link. {e} \n")


def plist():  # """Playlist Downloader Download Defination"""
    try:
        # take link from user
        link = input(">>Please Paste Your Youtube Playlist URL Here : ")
        ytp = Playlist(link)

############## Here is working for making folder same as playlist name ##############
        directory = ytp.title
        parent_dir = "C:/Users/Public/Youtube_Downloads/"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        print(f">>Playlist Title : {ytp.title}")
        print(f"Playlist Save Location >> {path}")
        i = 1
        for video in ytp.videos:
            video.streams.get_highest_resolution().download(output_path=path)
            print(f"{i} ► Title: {video.title[0:50]}...video(720p) has been successfully downloaded")
            i = i+1
        print("\n>>Playlist Completely Downloaded...")

    except Exception as e:
        print(
            f"\nWarning! {e} >> File Already Exists OR Please Provide Playlist Url Properly.\n")


# Program Start From Here :


print("###########################################################################\n\n     +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+\n     |Y|o|u|t|u|b|e| |D|o|w|n|l|o|a|d|e|r| |B|y| |M|i|n|g|h|1|1|1|2|\n     +-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+\n\n###########################################################################")
# User Input Section >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

num = (input(">>1._Video_ \n>>2._Audio_\n>>3._Playlist Downloader_\n>>4._Infinity_Mode_\n>>Press Any Key + Hit Enter To Exit Program..\n>>Choose : "))

if os.path.exists("C:\\Users\Public\Youtube_Downloads"):
    pass
else:
    os.makedirs("C:\\Users\Public\Youtube_Downloads")


try:
    choose_right_msg = ">>Program Terminated ,Choose Right One!"
except Exception as e:
    print(e)
if num.isnumeric():     # It will check string is number or not..
    if int(num) < 5 and int(num) > 0:
        if int(num) == 1:
            video()  # Go to Video Defination
        elif int(num) == 2:
            audio()  # Go to Audio Defination
        elif int(num) == 3:
            plist()  # Go to Playlist_Downloader Defination

        elif int(num) == 4:
            num = (input(">>1._Video_ \n>>2._Audio_\n>>Press Any Key + Hit Enter To Exit Program..\n>>Choose : "))

            while (True):
                if num.isnumeric():     # It will check string is number or not..
                    if int(num) < 3 and int(num) > 0:
                        print("\n>>Press Ctrl+C For Exist")
                        if int(num) == 1:
                            video()  # Go to Video Defination
                        if int(num) == 2:
                            audio()  # Go to Audio Defination
                        if int(num) == 3:
                            break
                    else:
                        # it will execute when num<3 and num>0
                        print(choose_right_msg)
                        break
                else:
                    # it will execute when string is not number
                    print(choose_right_msg)
                    break

    else:
        # it will execute when num<4 and num>0
        print(choose_right_msg)
else:
    # it will execute when string is not number
    print(choose_right_msg)
