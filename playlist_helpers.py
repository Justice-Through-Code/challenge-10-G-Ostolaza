# NOTE: DO NOT EDIT `display_playlist` and `add_song`


def display_playlist(playlist):
    # This function prints out what is in your playlist
    # Takes one argument: 'playlist' (a list)
    if len(playlist) == 0:
        print('Playlist is empty!')
    else:
        for i in range(len(playlist)):
            print(
                f'Track {i + 1}: {playlist[i]["plays"]} plays\n\t- {playlist[i]["title"]} by {playlist[i]["artist"]}'
            )


def add_song(playlist, song):
    # This function ads a song to the playlist
    # Takes two arguments: 'playlist' (a list), and 'song' (a dictionary)

    # Automatically initialize play count of song to 0
    song['plays'] = 0
    playlist.append(song)


'''
6.1 TODO: Define a function called `get_playlist_length`
This function should have one parameter called 'playlist'
The function should return an integer value indicating how many songs there are
The function should NOT print anything out
'''


'''
9.0 TODO: Define a function `called play_track`
It should have two parameters
-'playlist' (a list)
-'track' (an integer) - this should be optional, and by default play track 1
This function should 'play' the song corresponding to the input track #
For example play_track(my_playlist, 3) should print out:
'Now playing Track 3: Controversy by Prince' 
Assuming that the third track in your playlist 'Controversy' by 'Prince'
This function should ALSO increase the 'plays' value for that song's dictionary by 1
So, if 'Controversy' has 0 plays so far, it should now be increased to 1
'''