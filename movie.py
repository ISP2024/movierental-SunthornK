from dataclasses import dataclass
from typing import Collection


@dataclass(frozen=True)
class Movie:
    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, genre: str) -> bool:
        return genre.lower() in (i.lower() for i in self.genre)

    def get_title(self):
        return self.title

    def __str__(self):
        return f"{self.title} ({self.year})"
