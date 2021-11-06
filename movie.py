import csv

class Movie:
    """A movie available for rent."""

    # The types of movies (price_code).

    def __init__(self, title, year, genre):
        # Initialize a new movie.
        self.__title = title
        self.__year = year
        self.__genre = genre

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def is_genre(self, genre: list) -> bool:
        """Returns true if the string parameter matches one of the movie’s genre."""
        return genre in self.__genre

    def __str__(self):
        return self.__title


class MovieCatalog:
    """A movie catalog that fetch the data from CSV file"""

    def __int__(self):
        self.catalog = {}
        self.index_count = 0

    def load_data(self):
        """Load the data from CSV file"""
        with open('movies.csv', 'r') as f:
            row = list(csv.reader(f))
            self.catalog[row[self.index_count][1]] = Movie(row[self.index_count][1], row[self.index_count][2], row[self.index_count][3].split('|'))
        self.index_count += 1

    def get_movie(self, title: str) -> Movie:
        """Get movie from the catalog"""
        while True:
            if title in self.catalog:
                return self.catalog[title]
            else:
                try:
                    self.load_data()
                except IndexError:
                    break
