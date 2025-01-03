def make_album(artist, album, songs=None):
	the_album = {'Artist : ':artist, 'Album : ':album}
	if songs:
		the_album['songs']=songs
	print(the_album)


def enter_infos():
	while True:
		print("\nTapez 'q' pour quitter à tout moment")
		artist = input('Artiste : ')
		if artist == 'q':
			break
		album = input('Album : ')
		if album == 'q':
			break
		songs = input('Songs : ')
		if songs == 'q':
			break
		make_album(artist, album, songs)
enter_infos()