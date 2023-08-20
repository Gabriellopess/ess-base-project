from fastapi import APIRouter, HTTPException, Path, status
from src.db import database as db
from src.schemas.song import SongGet, SongModel, SongDelete,SongList
from starlette.responses import JSONResponse
from src.service.impl.song_service import SongService
from src.schemas.song import SongCreateModel

router = APIRouter()

# Get a specific song
@router.get(
    "/{song_id}",
    response_model=SongModel,
    response_class=JSONResponse,
    summary="Get a specific song",
)
def get_song(song_id: str):
    song_get_response = SongService.get_song(song_id)

    return song_get_response

@router.get(
    "/",
    response_model=SongList,
    response_class=JSONResponse,
    description="Retrieve all songs"
)
def get_songs():
    songs = db.get_all_items('songs')
    return {
        'songs': songs
    }

@router.put(
    "/{song_id}",
    response_model=SongModel,
    response_class=JSONResponse,
    summary="update a song",
)
def edit_song(song_id: str, song: SongCreateModel):
    song_edit_response = SongService.edit_song(song_id, song)

    return song_edit_response

# Add a song
@router.post(
    "/create",
    response_model=SongModel,
    response_class=JSONResponse,
    summary="create a song",
)
def add_song(song: SongCreateModel):
    song_add_response = SongService.add_song(song)

    return song_add_response

@router.get(
    "/songs",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get all songs",
)
def get_songs():
    songs_get_response = SongService.get_songs()

    return {
        "musics": songs_get_response
    }

@router.delete(
    "/{song_id}",
    response_model=SongDelete,
    response_class=JSONResponse,
    summary="delete a song",
)
def delete_song(song_id: str):
    song_delete_response = SongService.delete_song(song_id)
    return song_delete_response

@router.get(
    "/higlighted",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get highlighted songs",
)
def get_highlighted():
    highlighted_response = SongService.get_highlighted()
    return {
        "musics": highlighted_response
    }

@router.get(
    "/songs_by_year/{year}",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get all songs",
)
def get_by_year(year):
    song_get_response = SongService.get_by_year(year)

    return song_get_response

@router.get(
    "/songs_by_genre/{genre}",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get all songs",
)
def get_by_genre(genre):
    song_get_response = SongService.get_by_genre(genre)

    return song_get_response

@router.get(
    "/songs_by_artist/{artist}",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get all songs",
)
def get_by_artist(artist):
    song_get_response = SongService.get_by_artist(artist)

    return song_get_response

@router.get(
    "/songs_by_album/{album}",
    response_model=SongList,
    response_class=JSONResponse,
    summary="get all songs",
)

def get_songs():
    """
    Get all songs.

    Returns:
    - A list of all songs.
    """

    songs = db.get_all_items('songs')

    # Fetch music links for each song and add them to the response
    songs_with_links = []
    for song in songs:
        song_links = db.get_available_on_for_song(song.id)  # Substitua pela função real para obter os links
        song_with_links = song.dict()
        song_with_links['available_on'] = song_links
        songs_with_links.append(song_with_links)

    return songs_with_links


@router.get(
    "/{song_id}",
    response_model=SongModel, # Se der erro foi pq coloquei SongModel
    description="Retrieve a song by ID",
    tags=["songs"],
)
def get_song_by_id(song_id: int = Path(..., description="The ID of the song to retrieve")):
    """
    Get a song by its ID.

    Args:
    - song_id (int): The ID of the song to retrieve.

    Returns:
    - The requested song.

    Raises:
    - HTTPException(404) if the song is not found.
    """

    song = db.get_item_by_id('songs', song_id)
    if song is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")

    # Fetch music links for the song and add them to the response
    song_links = db.get_available_on_for_song(song_id)  # Substitua pela função real para obter os links
    song['available_on'] = song_links

    return song
