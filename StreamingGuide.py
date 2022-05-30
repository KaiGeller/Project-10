class Movie:

   def __init__ (self, title, genre, director, year):
       self.title = title
       self.genre = genre
       self.director = director
       self.year = year

   def get_title(self):
       return self.title

   def get_genre(self):
       return self.genre

   def get_director(self):
       return self.director

   def get_year(self):
       return self.year

class StreamingService:

   def __init__ (self, name):
       self.name = name
       self.catalog = {}

   def get_name(self):
       return self.name

   def get_catalog(self):
       return self.catalog

   def add_movie(self, movie):
       self.catalog[movie.get_title()] = movie

   def delete_movie(self, movie):
       if movie.get_title() in self.catalog:
           del self.catalog[movie.get_title()]

class StreamingGuide:

   def __init__ (self):
       self.streaming_service_list = []

   def add_streaming_service (self, streaming_service):
       self.streaming_service_list.append(streaming_service)

   def delete_streaming_service (self, streaming_service):
       for i in self.streaming_service_list:
           if i == streaming_service:
               self.streaming_service_list.remove(i)

   def where_to_watch(self, movie):
       search_results = []
       for i in self.streaming_service_list:
           if movie in i.get_catalog():
               search_results.append(i.get_name())
       return search_results






