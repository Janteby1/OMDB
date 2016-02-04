# API OMDB App (MVP)
import sys
import pudb

from view_omdb import View
from model_omdb import Model

class Run():
	def __init__ (self, movie, id):
		self.movie = None
		self.id = None
		self.view = View()
		self.model= Model()

	def __repr__ (self):
		return str(self.value)

	def welcome (self):
		"Print a welcome statement"
		self.view.welcome()

	def movie_choice (self):
		"Gets a movie choice from the users and checks that they entered it correctly"
		self.movie = self.view.movie_choice()
		self.choice = self.view.print_movie_choice(self.movie)
		if self.choice == "1":
			return self.movie
		else:
			self.movie_choice()

	def many_movie_string (self, movie):
		"Gets ride of all spaces in the movie title and replaces them with + signs"
		if " " in self.movie:
			self.movie = self.movie.replace(" ", "+")
			return self.movie
		else:
			self.get_many_movie_info(self.movie)

	def get_many_movie_info(self, movie):
		"Asks the user which movie he wants more info about"
		movie_info = self.model.many_movie_info(self.movie)
		choice = self.view.print_many_movie_info(movie_info)
		choice = int(choice)
		new_movie_title = movie_info["Search"][choice]['Title']
		self.new_movie = self.movie_string(new_movie_title)
		return self.new_movie

	def movie_string (self, movie):
		"Gets ride of all spaces in the movie title and replaces them with + signs"
		if " " in movie:
			movie = movie.replace(" ", "+")
			return movie
		else:
			return movie

	def get_movie_info(self, new_movie):
		"Sends the updated movie string to the API to get info back"
		movie_info = self.model.movie_info(new_movie)
		self.view.print_movie_info(movie_info)

	def run(self):
		# pu.db
		self.welcome()
		movie_choice = self.movie_choice()
		string = self.many_movie_string(movie_choice)
		many_movie_pick = self.get_many_movie_info (string)
		final_string = self.movie_string (many_movie_pick)
		self.get_movie_info (final_string)


run1 = Run(None,None)
run1.run()

