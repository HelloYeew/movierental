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


