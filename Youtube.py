from pytube import YouTube

link = input("Enter link :")
YT=YouTube(link, use_oauth=True, allow_oauth_cache=True)
YT.streams.get_highest_resolution().download()
print("Successfull")

