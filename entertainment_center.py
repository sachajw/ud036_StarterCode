"""Displays the movies and there details."""
import fresh_tomatoes
import media

pulp_fiction = media.Movie("Pulp Fiction", "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption",
                        "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                        "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

baby_driver = media.Movie("Baby Driver", "After being coerced into working for a crime boss, a young getaway driver finds himself taking part in a heist doomed to fail.",
                     "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg",
                     "https://www.youtube.com/watch?v=z2z857RSfhk")

big_lebowski = media.Movie("Big Lebowski", "Jeff Bridges plays Jeff Lebowski who insists on being called the Dude a laid-back easygoing burnout who happens to have the same name as a millionaire whose wife owes a lot of dangerous people a whole bunch of moneyresulting in the Dude having his rug soiled sending him spiraling into the Los Angeles underworld",
                           "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y")

grand_budapest_hotel = media.Movie("Grand Budapest Hotel", "The adventures of Gustave H, a legendary concierge at a famous hotel from the fictional Republic of Zubrowka between the first and second World Wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend.",
                             "https://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
                             "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

the_royal_tenenbaums = media.Movie("The Royal Tenenbaums", "A clan's estranged patriarch loses his home and learns that his ex-wife plans to remarry.",
                         "https://upload.wikimedia.org/wikipedia/en/3/3b/The_Tenenbaums.jpg",
                         "https://www.youtube.com/watch?v=8Eg6yIwP2vs")

napoleon_dynamite = media.Movie("Napoleon Dynamite", "A listless and alienated teenager decides to help his new friend win the class presidency in their small western high school, while he must deal with his bizarre family life back home.",
                                "https://upload.wikimedia.org/wikipedia/en/8/87/Napoleon_dynamite_post.jpg",
                                "https://www.youtube.com/watch?v=ZHDi_AnqwN4")

dogtown_and_z_boys = media.Movie("Dogtown and Z-Boys", "Documentary about the pioneering 1970s Zephyr skating team",
                           "https://upload.wikimedia.org/wikipedia/en/d/db/Dogtown_and_Z-Boys_FilmPoster.jpeg",
                           "https://www.youtube.com/watch?v=xP9EMH6R50w")

"""A list that stores the movie objects."""
movies = [pulp_fiction, baby_driver, big_lebowski, grand_budapest_hotel, the_royal_tenenbaums, napoleon_dynamite, dogtown_and_z_boys]

"""Opens the movies in the users web browser."""
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__doc__)
