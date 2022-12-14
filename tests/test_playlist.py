'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DO NOT EDIT THIS FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

import io
from unittest import mock, TestCase

from playlist import display_playlist, add_song, get_playlist_length, play_track


class TestPlaylistFunctions(TestCase):
    def setUp(self) -> None:
        # Runs before every test case
        super().setUp()

        self.playlist = [
            {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything', 'plays': 0},
            {'artist': 'Lizzo', 'title': 'Special', 'plays': 0},
            {'artist': 'Lizzo', 'title': 'Good as Hell', 'plays': 0}
        ]

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_playlist(self, mock_stdout):
        display_playlist(self.playlist)

        expected = ''
        for i in range(len(self.playlist)):
            expected += f'Track {i + 1}: 0 plays\n\t- {self.playlist[i]["title"]} by {self.playlist[i]["artist"]}\n'

        self.assertEqual(expected, mock_stdout.getvalue())

    
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_playlist_empty(self, mock_stdout):
        playlist = []
        display_playlist(playlist)

        expected = 'Playlist is empty!\n'

        self.assertEqual(expected, mock_stdout.getvalue())


    def test_add_song(self):
        add_song(self.playlist, {'artist': 'Sia', 'title': 'Cheap Thrills'})

        self.assertTrue('Cheap Thrills', self.playlist[3]['title'])
        self.assertEqual(0, self.playlist[3]['plays'])
    

    def test_get_playlist_length(self):
        playlist_len = get_playlist_length(self.playlist)

        self.assertEqual(3, playlist_len)


    def test_get_playlist_length_empty(self):
        playlist_len = get_playlist_length([])

        self.assertEqual(0, playlist_len)


    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_play_track_success(self, mock_stdout):
        play_track(self.playlist, 3)

        expected = "Now playing Track 3: Good as Hell by Lizzo\n"

        self.assertEqual(expected, mock_stdout.getvalue())


    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_play_track_failure(self, mock_stdout):
        play_track(self.playlist, 4)

        self.assertEqual('', mock_stdout.getvalue())
