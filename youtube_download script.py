# importing the module
from pytube import YouTube

# where to save
#SAVE_PATH = "C:\Users\ARTH\Desktop\download/" #to_do

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=1--qqQrimMA"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.streams.get_audio_only()

#to set the name of the file
#yt.set_filename('GeeksforGeeks Video')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension,mp4files[-1].)
try:
	# downloading the video
	mp4files.download()
	#d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
