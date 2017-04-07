import fresh_tomatoes
import media

# Below code sends 4 values, that is title, storyline, poster_image_url and
# trailer_youtube_url, to constructor of Movie class in media.py
# to create its instances.
# Here is first object named logan.
logan = media.Movie("Logan",
                    "Logan is a 2017 American superhero film featuring the Mar"
                    "vel Comics character Wolverine",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017"
                    "_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo&t=18s")

# Here is second object named iron_man.
iron_man = media.Movie("Iron Man", "I"
                       "ron Man is a 2008 American superhero film based on the"
                       " Marvel Comics character of the same name, produced by"
                       " Marvel Studios and distributed by Paramount Pictures",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/Ironma"
                       "nposter.JPG",
                       "https://www.youtube.com/watch?v=byQpcN78UjQ")

# Here is third object named despicable_me.
despicable_me = media.Movie("Despicable Me",
                            "Despicable Me is a 2010 American 3D computer-ani"
                            "mated comedy film from Universal Pictures and Il"
                            "lumination Entertainment",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/D"
                            "espicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=zzCZ1W_CUoI")

# Here is fourth object named furious_7.
furious_7 = media.Movie("Furious 7",
                        "Furious 7 (often stylized as Furious Seven and altern"
                        "atively known as Fast 7 and Fast & Furious 7) is a 20"
                        "15 American action film directed by James Wan and wri"
                        "tten by Chris Morgan. It is the seventh installment "
                        "in The Fast and the Furious franchise.",
                        "https://upload.wikimedia.org/wikipedia/en/b/b8/Furiou"
                        "s_7_poster.jpg",
                        "https://www.youtube.com/watch?v=Skpu5HaVkOc")

# Here is fifth object named white_house_down.
white_house_down = media.Movie("White House Down",
                               "White House Down is a 2013 American political"
                               " action thriller film directed by Roland Emme"
                               "rich about an assault on the White House by a "
                               "paramilitary group and the Capitol Police Off"
                               "icer who tries to stop them.",
                               "https://upload.wikimedia.org/wikipedia/en/5/5d"
                               "/White_House_Down_poster_with_billing_block.j"
                               "pg",
                               "https://www.youtube.com/watch?v=WfaTlmYvTA8")

# Here is sixth object named wild_child.
wild_child = media.Movie("Wild Child",
                         "Wild Child is a 2008 British-French-American teen "
                         "comedy film starring Emma Roberts, Alex Pettyfer and"
                         " Georgia King.",
                         "https://upload.wikimedia.org/wikipedia/en/f/fa/Wild_"
                         "child_poster.jpg",
                         "https://www.youtube.com/watch?v=WNDJMos8h-0")

# This sends all above objects to a list named movie.
movies = [logan, iron_man, despicable_me, furious_7, white_house_down,
          wild_child]

# This sends the movie list to fresh_tomatoes page.
fresh_tomatoes.open_movies_page(movies)
