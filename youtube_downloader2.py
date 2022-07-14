from pytube import YouTube

link = "https://www.youtube.com/watch?v=1--qqQrimMA"

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, 
file_extension = "mp4").first().download(output_path = "C:\Users\ARTH\Desktop\download", 
filename = "Reiner and Bertholdt Transformation scene")
except:
    print("Some Error!")
print('Task Completed!')
