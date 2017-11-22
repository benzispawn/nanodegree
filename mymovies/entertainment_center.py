import my_site
import media

godfather = media.Movie("GodFather",
                        "The aging patriarch of an organized crime dynasty \
                        transfers control of his clandestine empire to his \
                        reluctant son.",
                        "https://images-na.ssl-images-amazon.com/images/I/41h38v3Wm5L.jpg",  # noqa
                        "https://www.youtube.com/watch?v=5DO-nDW43Ik")
# Instance

godfather2 = media.Movie("GodFather part II",
                         "The early life and career of Vito Corleone in \
                         1920s New York is portrayed while his son, Mic \
                         hael, expands and tightens his grip on the fam \
                         ily crime syndicate. ",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMjZiNzIxNTQtNDc5Zi00YWY1LThkMTctMDgzYjY4YjI1YmQyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,702,1000_AL_.jpg",  # noqa
                         "https://www.youtube.com/watch?v=qJr92K_hKl0")
# Instance

godfather3 = media.Movie("GodFather part III",
                         "In the midst of trying to legitimize his busi \
                         ness dealings in New York and Italy in 1979, a \
                         ging Mafia don Michael Corleone seeks to avow \
                         for his sins while taking his nephew Vincent M \
                         ancini under his wing.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczMDcxNDA4MV5BMl5BanBnXkFtZTgwNjY1NTk4NjE@._V1_.jpg",  # noqa
                         "https://www.youtube.com/watch?v=z8h3LVb8cl8")
# Instance

carlitos = media.Movie("Carlito's Way",
                       "A Puerto Rican former convict, just released fr \
                       om prison, pledges to stay away from drugs and v \
                       iolence despite the pressure around him and lead \
                       on to a better life outside of N.Y.C.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BZmQ1ZDc0MDAtNjVmYi00MDkxLWE5MDItZmJmNjcxZGEyMWRjXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg",  # noqa
                       "https://www.youtube.com/watch?v=0yehgqPtG3Y")
# Instance

cassino = media.Movie("Cassino",
                      "A tale of greed, deception, money, power, and mu \
                      rder occur between two best friends: a mafia enfo \
                      rcer and a casino executive, compete against each \
                      other over a gambling empire and over a fast livi \
                      ng and fast loving socialite. ",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcxOWYzNDYtYmM4YS00N2NkLTk0NTAtNjg1ODgwZjAxYzI3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=EJXDMwGWhoA")
# Instance

movies = [godfather, godfather2, godfather3, carlitos, cassino]
# array of movies
my_site.open_movies_page(movies)  # Executing my_site
