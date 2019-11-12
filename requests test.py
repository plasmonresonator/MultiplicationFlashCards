from google_images_download import google_images_download
import os



download_path = 'C:\\Users\\212330207\\Box Sync\\PythonFiles\\Scripts\\MultiplicationFlashCards\\Pictures\\google test'
os.chdir(download_path)

print(f'Images will be saved to: {os.getcwd()}\n')

response = google_images_download.googleimagesdownload()

search_queries = [
	'funny cat pictures',
	'funny kitten pictures',
	]




def downloadimages(query):
	# keywords is the search query 
	# format is the image file format 
	# limit is the number of images to be downloaded 
	# print urs is to print the image file url 
	# size is the image size which can 
	# be specified manually ("large, medium, icon") 
	# aspect ratio denotes the height width ratio 
	# of images to download. ("tall, square, wide, panoramic") 
	arguments = {"keywords": query, 
				 "format": "jpg", 
				 "limit":20, 
				 "print_urls":True, 
				 "size": "medium", 
				 "aspect_ratio":"panoramic"} 

	try:
		response.download(arguments)

	except FileNotFoundError:
		arguments = {"keywords": query, 
					 "format": "jpg", 
					 "limit":20, 
					 "print_urls":True, 
					 "size": "medium"} 

		try:
			response.download(arguments)

		except:
			print(f'ran into an error...passing\n')
			pass


for query in search_queries:
	downloadimages(query)
	print(query)