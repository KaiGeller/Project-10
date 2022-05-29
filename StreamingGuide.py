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
       movie_details = [movie.get_genre(), movie.get_director(), movie.get_year()]
       self.catalog[movie.get_title()] = movie_details
   def delete_movie(self, movie):
       if movie in self.catalog is True:
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
       search_results.append(movie.get_title())
       for i in self.streaming_service_list:
           print("check1")

           print(movie.get_title() in i.get_catalog())
           if movie.get_title() in i.get_catalog() is True:

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

               search_results.append(i.get_name())
               print("check2")
       print(search_results)
       print(len(search_results))
       if len(search_results) < 2:
           search_results.clear()
           search_results.append("none")
       return search_results




Morbius = Movie("Morbius", "action/fantasy", "Daniel Espinosa", "2022")

Theaters = StreamingService("Theaters")
Theaters.add_movie(Morbius)
print(Theaters.get_catalog())

Netflix = StreamingService("Netflix")
Netflix.add_movie(Morbius)
Netflix.delete_movie(Morbius)
Netflix.delete_movie("Touch_With_reality")

streaming_guide = StreamingGuide()
streaming_guide.add_streaming_service(Theaters)
streaming_guide.add_streaming_service(Netflix)
streaming_guide.delete_streaming_service(Netflix)
search_results = streaming_guide.where_to_watch(Morbius)
print(search_results)



