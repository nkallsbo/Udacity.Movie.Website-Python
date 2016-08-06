import webbrowser

class Movie():
    """ Create object Movie, a class """
     
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # Constructor for movies
        """
        Saves information about the movies
        :param movie_title: Name of the movie
        :param movie_storyline: About the movie
        :param poster_image: URL to poster/ picture/ cover
        :param trailer_youtube: URL to trailer on YouTube
        :return: None
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
        #shows trailer in browser
        webbrowser.open(self.trailer_youtube_url)

    
