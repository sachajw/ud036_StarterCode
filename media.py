"""The Movie class that contains the details of a movie."""
import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # inir function
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Invokes the Movie class instance variables."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self) :
        """Plays the movie trailer in the web browser."""
        webbrowser.open(self.trailer_youtube_url)
