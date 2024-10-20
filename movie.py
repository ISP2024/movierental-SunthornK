import csv
import logging
from dataclasses import dataclass
from datetime import datetime
from pricing import NewRelease, RegularPrice, ChildrensPrice
from typing import Collection, Optional


@dataclass(frozen=True)
class Movie:
    title: str
    year: int
    genre: Collection[str]

    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrensPrice()

    @classmethod
    def price_code_for_movie(cls, movie):
        if movie.year == datetime.now().year:
            return cls.NEW_RELEASE
        for genre in movie.genre:
            if genre.lower() in ["children", "childrens"]:
                return cls.CHILDRENS
        return cls.REGULAR

    def is_genre(self, genre: str) -> bool:
        return genre.lower() in (i.lower() for i in self.genre)

    def get_title(self):
        return self.title

    def __str__(self):
        return f"{self.title} ({self.year})"


class MovieCatalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.movies = {}
            cls._instance.load_data("Movie Rental Part 2.csv")
        return cls._instance

    def load_data(self, filepath: str):
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for line, row in enumerate(reader):
                if not row or row[0].startswith('#'):
                    continue
                if len(row) < 4:
                    logging.error(f"Line {line+1}: Unrecognized format \"{','.join(row)}\"")
                    continue
                title = row[1]
                try:
                    year = int(row[2])
                except ValueError:
                    logging.error(f"Line {line+1}: Invalid year '{row[2]}'")
                    continue
                genres = {genre for genre in row[3].split("|")}
                self.movies[(title, year)] = Movie(title, year, genres)

    def get_movie(self, title: str, year: Optional[int] = None):
        if year is not None:
            return self.movies.get((title, year))
        for (t, y), movie in self.movies.items():
            if t.lower() == title.lower():
                return movie
        return None