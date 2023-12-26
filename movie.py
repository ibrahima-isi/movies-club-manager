import os 
import json
import logging



CUR_DIR = os.path.dirname(__file__) 
DATA_FILE = os.path.join(CUR_DIR, 'data', 'movies.json')

class Movie:
    def __init__(self, title) -> None:
        self.title = title.title()
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    # def __repr__(cls) -> str:
    #     return f"Class Movie(movie_title)"

    def _get_movies(self):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, 'w') as f:
            json.dump(movies, f, indent=4, ensure_ascii=False)
            return True
        return False
    

    def add_to_movies(self):
        movies = self._get_movies()
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies=movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est deja dans la liste")
            return False
        
    def remove_from_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        logging.warning(f"Le film {self.title} n'est pas dans la liste des films")
        return False

def get_movies():
    obj_movies = []
    with open(DATA_FILE) as f:
        movies = json.load(f)
    for movie in movies:
        obj_movies.append(Movie(movie))
    return obj_movies

if __name__ == "__main__":
    m = Movie("Harry Potter")
    # m.add_to_movies()
    # m.remove_from_movies()
    # print(get_movies())
    # movies = get_movies()
    # for m in movies:
    #     if isinstance(m, Movie):
    #         print(m)