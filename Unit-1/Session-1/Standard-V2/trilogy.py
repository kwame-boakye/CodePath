# Write a function trilogy() that accepts an integer year and prints the title of
# the Batman trilogy movie released that year as outlined below.
# Year 	Movie Title
# 2005 	"Batman Begins"
# 2008 	"The Dark Knight"
# 2012 	"The Dark Knight Rises"
# If the given year does not match one of the years in the table above, print
# "Christopher Nolan did not release a Batman movie in <year>."


def trilogy(year):
    movies_titles = {
        2005: "Batman Begins",
        2008: "The Dark Knight",
        2012: "The Dark Knight Rises",
    }

    if year in movies_titles:
        print(movies_titles[year])
    else:
        print(f"Christopher Nolan did not release a Batman movie in {year}.")


trilogy(2020)
