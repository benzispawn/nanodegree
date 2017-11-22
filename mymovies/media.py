import webbrowser


class Movie():  # Class
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):  # Constructor
        self.title = movie_title  # Instance Variables
        self.storyline = movie_storyline  # Instance Variables
        self.poster_image_url = poster_image  # Instance Variables
        self.trailer_youtube_url = trailer_youtube  # Instance Variables

    def show_trailer(self):  # Instance Methods
        webbrowser.open(self.trailer_youtube_url)
