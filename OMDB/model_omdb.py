import requests
import pudb 

class Model:
	# do I neeed an init ?!

	def movie_info(self, movie):
		movie_info = requests.get("http://www.omdbapi.com/?t=%s&y=&plot=short&r=json" % (movie)).json()
		return movie_info

	def many_movie_info(self, movie):
		movie_info = requests.get("http://www.omdbapi.com/?s=%s&y=&plot=short&r=json" % (movie)).json()
		return movie_info

