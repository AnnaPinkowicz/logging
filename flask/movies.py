import random
import datetime


class Picture:
    def __init__(self, title, release_year, genre, played):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.played = played

    def play(self):
        self.played += 1

    def show(self):
        print(f"{self.title} {self.played}")


class Movie(Picture):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.release_year})'


class Serie(Picture):
    def __init__(self, title, release_year, genre, played, season, episode):
        super().__init__(title, release_year, genre, played)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title}({self.release_year}),S{self.season:02}E{self.episode:02}'


def get_movies(pict):
    movies = []
    for p in pict:
        if isinstance(p, Movie):
            movies.append(p)
    return movies


def get_series(pict):
    series = []
    for p in pict:
        if isinstance(p, Serie):
            series.append(p)
    return series


def search(title):
    for x in pictures:
        if x.title == title:
            return x
        elif x.title == title:
            break


def generate_views(pictures):
    n = len(pictures)
    i = random.randint(0, n - 1)
    picture = pictures[i]
    picture.played += random.randint(1, 100)


def gen_10(pict):
    for _ in range(10):
        generate_views(pictures)
        pict.sort(key=lambda x: x.played, reverse=True)


def top_titles(picts, n=3, content_type=None):
    if content_type == "movies":
        picts = get_movies(picts)
    elif content_type == "series":
        picts = get_series(picts)

    picts.sort(key=lambda x: x.played, reverse=True)
    return picts[:n]


if __name__ == "__main__":
    pictures = [
        Movie("Titanic", 1996, "drama", 0),
        Movie("Annie", 2014, "musical", 0),
        Movie("Amelia", 2008, "drama", 0),
        Movie("Rocky", 1987, "drama", 0),
        Serie("Friends", 2000, "comedy", 0, 6, 6),
        Serie("Wilfred", 2011, "drama", 0, 6, 9),
        Serie("Suits", 2011, "drama", 0, 6, 9),
        Serie("Dexter", 2005, "drama", 0, 6, 9),
    ]
    print("Available:")
    for p in pictures:
        print(p)
    print("----------------------------------")

    print("Top titles:")
    for picture in top_titles(pictures, content_type="series"):
        print(picture)

    print("----------------------------------")
    print("Sorten by views on:")
    dzis = datetime.datetime.now()
    print(dzis)
    gen_10(pictures)
    for p in pictures:
        p.show()

    print("----------------------------------")

    print("----------------------------------")
    print(search("Annie"))
