import fresh_tomatoes
import media

# instance variables
pulp_fiction = media.Movie(
                "Pulp Fiction", "The lives of two mob hit men, a boxer,"
                "a gangster's wife, and a pair of diner bandits intertwine in"
                "four tales of violence and redemption",
                "https://goo.gl/VTvhgq",
                "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

baby_driver = media.Movie(
                "Baby Driver", "After being coerced into working for a crime"
                "boss, a young getaway driver finds himself taking part in a"
                "heist doomed to fail.",
                "https://goo.gl/LF5F5x",
                "https://www.youtube.com/watch?v=z2z857RSfhk")

big_lebowski = media.Movie(
                "Big Lebowski", "Jeff Bridges plays Jeff Lebowski"
                "who insists on being called the Dude a laid-back easygoing"
                "burnout who happens to have the same name as a millionaire"
                "whose wife owes a lot of dangerous people a whole bunch of"
                "money resulting in the Dude having his rug soiled sending him"
                "spiraling into the Los Angeles underworld",
                "https://goo.gl/QjE7f1",
                "https://www.youtube.com/watch?v=cd-go0oBF4Y")

grand_budapest_hotel = media.Movie(
                "Grand Budapest Hotel", "The adventures of Gustave H, a"
                "legendary concierge at a famous hotel from the fictional"
                "Republic of Zubrowka between the first and second World Wars,"
                "and Zero Moustafa, the lobby boy who becomes his most trusted"
                "friend.",
                "https://goo.gl/iwjXLx",
                "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

the_royal_tenenbaums = media.Movie(
                "The Royal Tenenbaums",
                "A clan's estranged patriarch loses his"
                "home and learns that his ex-wife plans to remarry.",
                "https://goo.gl/bLy64q",
                "https://www.youtube.com/watch?v=8Eg6yIwP2vs")

napoleon_dynamite = media.Movie(
                "Napoleon Dynamite",
                "A listless and alienated teenager decides"
                "to help his new friend win the class presidency"
                "in their small western high school,"
                "while he must deal with his bizarre family life back home.",
                "https://goo.gl/3pYvwX",
                "https://www.youtube.com/watch?v=ZHDi_AnqwN4")

dogtown_and_z_boys = media.Movie(
                "Dogtown and Z-Boys", "Documentary about the pioneering 1970s"
                "Zephyr skating team",
                "https://goo.gl/FJPVZZ",
                "https://www.youtube.com/watch?v=xP9EMH6R50w")

baraka = media.Movie(
        "Baraka", "A collection of expertly photographed scenes of"
        "human life and religion.",
        "https://upload.wikimedia.org/wikipedia/en/6/64/Baraka.jpg",
        "https://www.youtube.com/watch?v=ZSfFHxyYJJA")

samsara = media.Movie(
        "Samsara", "Filmed over nearly five years in twenty-five countries on"
        "five continents, and shot on seventy-millimetre film, Samsara"
        "transports us to the varied worlds of sacred grounds, disaster zones,"
        "industrial complexes, and natural wonders.",
        "https://goo.gl/ZAvQdJ",
        "https://www.youtube.com/watch?v=HCkEILshUyU")
# an array / list
movies = [
    pulp_fiction,
    baby_driver,
    big_lebowski,
    grand_budapest_hotel,
    the_royal_tenenbaums,
    napoleon_dynamite,
    dogtown_and_z_boys,
    baraka,
    samsara
        ]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__doc__)
