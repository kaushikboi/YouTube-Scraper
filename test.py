from pytube import YouTube
import csv
filename = "data.csv" #the  file containing all the youtube links
csvfile = open(filename,'r') #opening the file in read mode
datareader = csv.reader(csvfile)
for row in datareader:
	link = str(row) # converting all the links in to strings
	yt = YouTube(link) 
	print("Title: ",yt.title) #getting the youtube video title
	ys = yt.streams.get_highest_resolution() # getting the highest resolution of the video
	ys.download() # downloading the video in the pwd

