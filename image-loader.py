# loads images from a users collection

import pickle
import webbrowser

username = input("Enter your discogs username:\n")

infile = open("{0}_collection.txt".format(username), 'rb')
collection_dict = pickle.load(infile)

for album in collection_dict:
	image_url = collection_dict[album][2]
	webbrowser.open(image_url)