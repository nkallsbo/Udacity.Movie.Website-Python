import fresh_tomatoes
import media

# Name, storyline, URL to poster and trailer
the_jungle_book = media.Movie("The Jungle Book",
                              "About a boy named Mowgli that lives in the jungle",
                              "http://ia.media-imdb.com/images/M/MV5BMTc3NTUzNTI4MV5BMl5BanBnXkFtZTgwNjU0NjU5NzE@._V1_SY1000_SX675_AL_.jpg",
                              "http://www.youtube.com/watch?v=HcgJRQWxKnw")

the_legend_of_tarzan = media.Movie("The Legend of Tarzan",
                                   "Tarzan, a jungle man",
                                   "http://ia.media-imdb.com/images/M/MV5BMzY3OTI0OTcyMF5BMl5BanBnXkFtZTgwNjkxNTAwOTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                                   "http://www.youtube.com/watch?v=Aj7ty6sViiU")

jason_bourne = media.Movie("Jason Bourne",
                           "He's a former CIA agent who uncover the hidden truth",
                           "http://ia.media-imdb.com/images/M/MV5BMTU1ODg2OTU1MV5BMl5BanBnXkFtZTgwMzA5OTg2ODE@._V1_SY1000_SX632_AL_.jpg",
                           "http://www.youtube.com/watch?v=MIJ53m77-kw")

suicide_squad = media.Movie("Suicide Squad",
                            "A secret government agency recruits imprisoned supervillains",
                            "http://ia.media-imdb.com/images/M/MV5BMjM1OTMxNzUyM15BMl5BanBnXkFtZTgwNjYzMTIzOTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                            "http://www.youtube.com/watch?v=CmRih_VtVAs")

dawn_of_justice = media.Movie("Batman v Superman: Dawn of Justice",
                              "Fearing that the actions of Superman are left unchecked, Batman takes on the Man of Steel",
                              "http://ia.media-imdb.com/images/M/MV5BYThjYzcyYzItNTVjNy00NDk0LTgwMWQtYjMwNmNlNWJhMzMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                              "http://www.youtube.com/watch?v=eX_iASz1Si8")

captain_america = media.Movie("Captain America: Civil War",
                              "A rift between former allies Captain America and Iron Man",
                              "http://ia.media-imdb.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                              "http://www.youtube.com/watch?v=uVdV-lxRPFo")
                              
# List with movies                              
movies = [the_jungle_book, the_legend_of_tarzan, jason_bourne, suicide_squad, dawn_of_justice, captain_america]

# Uses list of movie instances as input to generate an HTML file and open it in the browser
fresh_tomatoes.open_movies_page(movies)
                                                          
                    


                    

