from main import app
from flask_testing import TestCase
class TestHomeRoute(TestCase):
    def create_app(self):
        return app

    def test_home_route(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('index.html')

    def test_home_route_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_route_content(self):
        response = self.client.get('/')
        self.assertIn(b'Female Idol Top Trumps', response.data)


class TestChooseCardsRoute(TestCase):
    def create_app(self):
        return app

    def test_choose_cards_route(self):
        form_data = {'choice': '0'}
        response = self.client.post('/submit/', data=form_data, follow_redirects=True)
        self.assert_200(response)
        self.assert_template_used('choose_cards.html')

    def test_choose_cards_route_status_code(self):
        response = self.client.post('/submit/')
        self.assertEqual(response.status_code, 200)

    def test_choose_cards_route_content(self):
        response = self.client.post('/submit/')
        self.assertIn(b'Choose Card', response.data)

class TestBattleRoute(TestCase):
    def create_app(self):
        return app

    def test_battle_route_status_code(self):
        form_data = {'choice': '0'}
        response = self.client.post('/battle', data=form_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_battle_route(self):
        form_data = {'choice': '0'}  
        response = self.client.post('/battle', data=form_data, follow_redirects=True)
        self.assert200(response)
        self.assert_template_used('battle.html')

class TestResultsRoute(TestCase):
    def create_app(self):
        return app

    def test_results_route(self):
        response = self.client.post('/results', data={'attribute': '#Creativity'}, follow_redirects=True)
        self.assert_200(response)
        self.assert_template_used('result.html')
        self.assertIn(b'See Results', response.data)

    def test_results_invalid_route(self):
        response = self.client.get('/invalid', follow_redirects=True)
        self.assert_404(response)

    def test_results_content(self):
        response = self.client.post('/results', data={'attribute': '#Innovation'}, follow_redirects=True)
        self.assertIn(b'Next Round', response.data)


class TestEndRoute(TestCase):
    def create_app(self):
        return app

    def test_end_route(self):
        response = self.client.get('/end', follow_redirects=True)
        self.assert_200(response)
        self.assert_template_used('end.html')

    def test_end_route_scores(self):
        response = self.client.get('/end', follow_redirects=True)
        self.assert_200(response)
        self.assertIn(b'Computer Score:', response.data)
        self.assertIn(b'Player Score:', response.data)

    def test_end_route_content(self):
        response = self.client.get('/end', follow_redirects=True)
        self.assert_200(response)
        self.assertIn(b'Game Over!', response.data)

class TestRestart(TestCase):
    def create_app(self):
        return app

    def test_restart_game(self):
        response = self.app.post('/restart', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

