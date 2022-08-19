from os import path, rename
from pytube import YouTube as yt

destination_path = desktop = path.expanduser("~/Desktop")
# link input for user
link = input("Enter the link of YouTube video: ")
youtube = yt(link)
# download file
video = youtube.streams.first()
downloaded_file = video.download(destination_path)
base, ext = path.splitext(downloaded_file)
new_file = base + '.mp3'
# rename audio file
rename(downloaded_file, new_file)
# success message
print('Download Complete')
input("Please press Enter to exit...")
