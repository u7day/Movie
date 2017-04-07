import webbrowser


class Movie():
    # Class is consisting of 2 methods.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # This method set value of variables: title, storyline,
        # poster_image_url, trailer_youtube_url
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # This method uses "open" function of webbrowser to open
        # the trailer link 
        webbrowser.open(self.trailer_youtube_url)
