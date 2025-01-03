def make_album(artist, album, songs=None):
	album = {'Artist : ':artist, 'Album : ':album}
	if songs:
		album['songs']=songs
	return album

print(make_album('U2', 'Under a blood red sky'))
print(make_album('Queen', 'A night at the opera', 12))
print(make_album('Prince', 'Purple rain'))
print(make_album('Radiohead', 'OK Computer', 8))