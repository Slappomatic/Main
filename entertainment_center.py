import media
import fresh_tomatoes


""" Opens the file Movies.txt and sends it through a for loop to populate the
    list movies[] and then opens the fresh_tomatoes.open_movies_page """
movies= []
f = open(r"movies.txt")
for line in f:
    fields = line.split("|")
    movies.append(media.Movie(fields[0],fields[1],fields[2],fields[3]))

f.close()

fresh_tomatoes.open_movies_page(movies)


