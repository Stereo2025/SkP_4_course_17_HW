from app import app


movie_keys = {'id', 'title', 'description', 'trailer', 'year',
              'rating', 'genre_id', 'director_id'}
genre_keys = {'id', 'name'}
director_keys = {'id', 'name'}


class TestApi:

    def test_element_keys_from_movies(self):
        response = app.test_client().get('/movies/')
        assert len(response.json[0]) == len(movie_keys), 'Ошибка в количестве ключей'
        assert set(response.json[0]) == movie_keys, 'Ошибка в названии ключей'

    def test_element_keys_from_genres(self):
        response = app.test_client().get('/genres/')
        assert len(response.json[0]) == len(genre_keys), 'Ошибка в количестве ключей'
        assert set(response.json[0]) == genre_keys, 'Ошибка в названии ключей'

    def test_element_keys_from_directors(self):
        response = app.test_client().get('/directors/')
        assert len(response.json[0]) == len(director_keys), 'Ошибка в количестве ключей'
        assert set(response.json[0]) == director_keys, 'Ошибка в названии ключей'

    def test_page_from_movies(self):
        response = app.test_client().get('/movies/')
        assert response.status_code == 200, 404
        assert type(response.json) == list, 'Это не список'

    def test_page_from_genres(self):
        response = app.test_client().get('/genres/')
        assert response.status_code == 200, 404
        assert type(response.json) == list, 'Это не список'

    def test_page_from_directors(self):
        response = app.test_client().get('/directors/')
        assert response.status_code == 200, 404
        assert type(response.json) == list, 'Это не список'

    def test_page_from_one_movie(self):
        response = app.test_client().get('/movies/1/')
        assert response.status_code == 200, 404
        assert type(response.json) == dict, 'Это не список'

    def test_page_from_one_genre(self):
        response = app.test_client().get('/genres/1/')
        assert response.status_code == 200, 404
        assert type(response.json) == dict, 'Это не список'

    def test_page_from_one_director(self):
        response = app.test_client().get('/directors/1/')
        assert response.status_code == 200, 404
        assert type(response.json) == dict, 'Это не список'

    def test_page_from_error_page(self):
        response = app.test_client().get('/qwerty/')
        assert response.status_code == 404

    def test_page_not_found_movie(self):
        response = app.test_client().get('/movies/444', follow_redirects=True)
        assert response.status_code == 404

    def test_page_not_found_genre(self):
        response = app.test_client().get('/genres/444', follow_redirects=True)
        assert response.status_code == 404

    def test_page_not_found_director(self):
        response = app.test_client().get('/directors/444', follow_redirects=True)
        assert response.status_code == 404
