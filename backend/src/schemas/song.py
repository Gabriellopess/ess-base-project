from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class SongModel(BaseModel):
    id: str
    title: str
    genre: str
    artist: str
    release_year: int
    popularity: Optional[int] = None


class SongGet(BaseModel):
    id: str
    title: str
    genre: str
    artist: str
    release_year: int
    popularity: Optional[int] = None


class SongCreateModel(BaseModel):
    id: str
    title: str
    genre: str
    artist: str
    release_year: int
    popularity: Optional[int] = None


class SongList(BaseModel):
    songs: list[SongGet]


class SongDelete(BaseModel):
    id: str
