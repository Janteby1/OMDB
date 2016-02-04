# API OMDB App (MVP)
import sys
import pudb

class View ():

	def welcome (self):
		print ("")
		print ("Welcome to the OMDB app!")
		print ("This app allows you to search for a movie and get back information about it.")
		print ("Lets get started ... ")

	def movie_choice (self):
		while True:
			print ("")
			self.movie = input ("What movie would you like to search?: ")
			if self.movie != None:
				break
			print ("Please enter a movie")
		return self.movie

	def print_movie_choice (self, movie):
		print ("")
		print ("Great! You pciked to search for the movie -- ", self.movie)
		print ("")
		self.choice = input("If that is correct press 1, if not press any other key: ")
		print ("Processing ... ")
		return self.choice

	def print_movie_info (self, movie_info):
		print ("")
		print ("Movie title: ", movie_info['Title'])
		print ("Movie year: ", movie_info["Year"])
		print ("Movie director: ", movie_info["Director"])
		print ("Movie cast: ", movie_info["Actors"])
		print ("Movie plot: ", movie_info["Plot"])
		print ("")
		print ("Thank you.")

	def print_many_movie_info (self, movie_info):
		# pu.db
		length = len("Search")
		for i in range (0,length):
			print ("")
			print ("Movie title: ", movie_info["Search"][i]['Title'])
			print ("Movie year: ", movie_info["Search"][i]["Year"])
			print ("Movie ID: ", i)
			print ("")
		choice = input ("Please enter the ID of the movie you want more information about: ")
		return choice





