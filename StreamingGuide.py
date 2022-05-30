#Kai Geller
#GitHub Username:KaiGeller
#5/29/2022
#The point of this code is to class a movie and streaming service and a streamig guide and use those to find which movies are in which streaming guides.



class Movie:
   """This classifies the Movie"""

   def __init__ (self, title, genre, director, year):
       """This function takes the details of the movie"""
       self.title = title
       self.genre = genre
       self.director = director
       self.year = year

   def get_title(self):
       """This function gets the title"""
       return self.title

   def get_genre(self):
       """This function gets the genre"""
       return self.genre

   def get_director(self):
       """This function gets the director"""
       return self.director

   def get_year(self):
       """This function gets the year"""
       return self.year

class StreamingService:
   """This class classifies the streaming services"""

   def __init__ (self, name):
       """This function takes the name and makes an empty list"""
       self.name = name
       self.catalog = {}

   def get_name(self):
       """This function gets the name of the streaming service"""
       return self.name

   def get_catalog(self):
       """This function gets the catalog"""
       return self.catalog

   def add_movie(self, movie):
       """This function adds a movie to the catalog"""
       self.catalog[movie.get_title()] = movie

   def delete_movie(self, movie):
       """This function deletes a movie from the catalog"""
       if movie.get_title() in self.catalog:
           del self.catalog[movie.get_title()]

class StreamingGuide:
   """This class classifies the StreamingGuide"""

   def __init__ (self):
       """This function creates a streaming service list"""
       self.streaming_service_list = []

   def add_streaming_service (self, streaming_service):
       """This function adds a streaming service to the list"""
       self.streaming_service_list.append(streaming_service)

   def delete_streaming_service (self, streaming_service):
       """This function deletes a streaming service from the list"""
       for i in self.streaming_service_list:
           if i == streaming_service:
               self.streaming_service_list.remove(i)

   def where_to_watch(self, movie):
       """This function tells you where to watch the movie that is entered"""
       search_results = []
       search_results.append(movie)
       movie_object= Movie("","","",0)
       for i in self.streaming_service_list:
           if movie in i.get_catalog():
               movie_object=i.get_catalog()[movie]
               search_results.append(i.get_name())
       search_results[0]=search_results[0]+ " ("+str(movie_object.get_year())+")"
       if len(search_results) < 2:
           search_results.clear()
           search_results.append("None")
       return search_results






