from fastapi import APIRouter, status, HTTPException
from src.schemas.music import MusicGet, MusicModel, MusicDelete, MusicList, MusicNameList
from starlette.responses import JSONResponse
from src.db import database as db

from src.service.impl.music_service import MusicService
from src.schemas.music import SongCreateModel

router = APIRouter()

# Get a specific song
@router.get(
    "/song/{song_id}",
    response_model=MusicModel,
    response_class=JSONResponse,
    summary="Get a specific song",
)
def get_song(song_id: str):
    song_get_response = MusicService.get_song(song_id)

    return song_get_response

@router.put(
    "/song/{song_id}",
    response_model=MusicModel,
    response_class=JSONResponse,
    summary="update a song",
)
def edit_song(song_id: str, song: SongCreateModel):
    song_edit_response = MusicService.edit_song(song_id, song)

    return song_edit_response


# Add a song
@router.post(
    "/song",
    response_model=MusicModel,
    response_class=JSONResponse,
    summary="create a song",
)
def add_song(song: SongCreateModel):
    song_add_response = MusicService.add_song(song)

    return song_add_response

@router.delete(
    "/song/{song_id}",
    response_model=MusicDelete,
    response_class=JSONResponse,
    summary="delete a song",
)
def delete_song(song_id: str):
    song_delete_response = MusicService.delete_song(song_id)
    return song_delete_response

@router.get(
    "/top-rated",
    response_model=MusicNameList,  # Assuming Song model has a field for average rating
    description="Retrieve top-rated songs"
)
def get_top_rated_songs(limit: int = 5):
    """
    Get the top-rated songs based on average rating.

    Args:
    - limit (int): How many top-rated songs to retrieve. Default is 10.

    Returns:
    - A list of top-rated songs.
    """
    print('teste')
    songs = db.get_top_rated_songs('musicas', limit)
    print('TESTE2 ')
    print(songs)
    return {'musics':songs}


# Edit a song's genre
# @router.put(
#     "/song/{song_id}/genre",
#     response_model=HttpResponseModel,
#     status_code=status.HTTP_200_OK,
#     responses={
#         status.HTTP_404_NOT_FOUND: {
#             "description": "Song not found",
#         }
#     },
# )
# def edit_genre(song_id: str, genre: str) -> HttpResponseModel:
#     edit_genre_response = MusicService.edit_genre(song_id, genre)
#     return edit_genre_response
