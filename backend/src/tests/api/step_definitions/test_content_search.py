from fastapi.testclient import TestClient
from src.main import app  # Importe a instância da aplicação FastAPI
from unittest.mock import MagicMock
from src.service.impl.song_service import SongService

client = TestClient(app)

def test_search_songs_by_genre_existent():
    # Dado que o SongService retorna as músicas "Lover", "Vampire" e "August"
    SongService.get_by_genre = MagicMock(return_value={
        "songs": [
            {"title": "Lover", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2020, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"},
            {"title": "Vampire", "artist": "John Doe", "genre": "Pop", "release_year": 2020, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"},
            {"title": "August", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2020, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"}
        ]
    })

    # Quando uma requisição "GET" for enviada para "/songs/songs_by_genre" com o parâmetro de consulta "genre" definido como "Pop"
    response = client.get("/songs/songs_by_genre/Pop")
    print(response.json())

    # Então o status da resposta deve ser "200"
    assert response.status_code == 200

    # E o JSON da resposta deve conter uma lista de músicas do gênero "Pop", "release_year": "2020" com os nomes "Lover", "Vampire" e "August"
    expected_json = {
        "songs": [
            {"title": "Lover", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2020, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"},
            {"title": "Vampire", "artist": "John Doe", "genre": "Pop", "release_year": 2020, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"},
            {"title": "August", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2020, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"}
        ]
    }
    print(expected_json)
    assert response.json() == expected_json

def test_search_songs_by_year():
    # Dado que o SongService retorna as músicas "Lover" e "Cruel Summer" para o ano de lançamento 2019

    SongService.get_by_year = MagicMock(return_value={
        "songs": [
            {"title": "Lover", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2019, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"},
            {"title": "Cruel Summer", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2019, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"}
        ]
    })

    # Quando uma requisição "GET" for enviada para "/songs/songs_by_year" com o parâmetro de consulta "release_year" definido como "2019"
    response = client.get("/songs/songs_by_year/2019")
    print(response.json())

    # Então o status da resposta deve ser "200"
    assert response.status_code == 200

    # E o JSON da resposta deve conter uma lista de músicas com o ano de lançamento "2019" com os nomes "Lover" e "Cruel Summer"
    expected_json = {
        "songs": [
            {"title": "Lover", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2019, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"},
            {"title": "Cruel Summer", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2019, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"}
        ]
    }
    print(expected_json)
    assert response.json() == expected_json

def test_search_songs_by_artist():

    # Dado que o SongService retorna as músicas "Lover" e "Cruel Summer" para o artista "Taylor Swift"
    SongService.get_by_artist = MagicMock(return_value={
        "songs": [
            {"title": "Lover", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2019, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"},
            {"title": "Cruel Summer", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2019, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"}
        ]
    })

    # Quando uma requisição "GET" for enviada para "/search" com o parâmetro de consulta "query" definido como "Taylor Swift"
    response = client.get("/songs/songs_by_artist/Taylor@Swift")
    print(response.json())

    # Então o status da resposta deve ser "200"
    assert response.status_code == 200

    # E o JSON da resposta deve conter uma lista de músicas da "Taylor Swift" com os nomes "Lover" e "Cruel Summer"
    expected_json = {
        "songs": [
            {"title": "Lover", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2019, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"},
            {"title": "Cruel Summer", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2019, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"}
        ]
    }
    print(expected_json)
    assert response.json() == expected_json

def test_search_artist_unexistent():

    # Dado que o SongService não possui a música "NX Zero"
    SongService.get_by_artist = MagicMock(return_value={
        "songs": [
            {"title": "Lover", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2019, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"},
            {"title": "Cruel Summer", "artist": "Taylor Swift", "genre": "Pop", "release_year": 2019, "id":"x", "popularity": 10, "available_on": {}, "created_at": "2023-08-15T12:00:00Z"}
        ]
    })

    # Quando uma requisição "GET" for enviada para ""/songs/get_by_artist/NX@Zero"
    response = client.get("/songs/get_by_artist/NX@Zero")

    # Então o status da resposta deve ser "404"
    assert response.status_code == 404

    # E o JSON da resposta deve conter uma lista vazia
    expected_json = {
        'detail': 'Not Found'
    }
    assert response.json() == expected_json

