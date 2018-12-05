# This file gets and stores the collection of a discogs authenticated user
# including Album names, Artist names, and album artwork

# TODO:
# turn into class

import discogs_client as dc
import keys
import pickle

def main():
	# TEST
	# get username
	username = input("Enter your discogs username:\n")
	# open file that contains user-specific keys
	infile = open("access_keys_{0}.txt".format(username), 'rb')
	key_dict = pickle.load(infile)
	access_token = key_dict['access_token']
	access_secret = key_dict['access_secret']

	d_keys = keys.discogsKeys()
	user_agent = d_keys._user_agent
	consumer_key = d_keys._consumer_key
	consumer_secret = d_keys._consumer_secret
	client = dc.Client(
		user_agent, 
		consumer_key=consumer_key, 
		consumer_secret=consumer_secret,
		token=access_token,
		secret=access_secret
	)

	user = client.identity()

	# create empty dict to hold collection
	collection_dict = dict()
	collection = user.collection_folders[0].releases

	#create file to save collection
	outfile = open("{0}_collection.txt".format(user.username), 'wb')

	# get data for each release and add to dictionary:
	# key = release ID, value = [title, artist, cover image]
	for release in collection:
		info = release.data['basic_information']
		artist = ''
		for inst in info['artists']:
			if info['artists'].index(inst) > 0:
				artist += 'and {0}'.format(inst['name'])
			else:
				artist += inst['name']
		title = info['title']
		cover = get_cover(release)
		collection_dict[release.id] = [title, artist, cover]

	pickle.dump(collection_dict, outfile)
	outfile.close()

def get_cover(release):

	if 'cover_image' in release.data['basic_information'].keys():
		image_url = release.data['basic_information']['cover_image']
	elif 'images' in release.data['basic_information'].keys():
		image_url = release.data['basic_information']['images'][0]['uri']
	elif 'thumb' in release.data['basic_information'].keys():
		image_url = release.data['basic_information']['thumb']
	else:
		image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSghqQngc01lPwC40kPJ3zBmv0onzsn0X06dSj7oza0PLH7VY-t1Q"
	return image_url

main()