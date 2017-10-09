import webbrowser

class Movie():
    """ This class will define the class Movie """
    VALID_RATINGS = ["G","PG","PG-13","R"]

    """ __init__ initializes the variables movie_title, movie_storyline,
    poster_image, and trailer_youtube """
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    """ show_trailer opens a inbedded youtube browser window for the trailer to
    play """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

