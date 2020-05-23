def make_album(artist_name, album_title, track_count = None):
	"""Returns a dictionary describing an album"""
	album = {'artist name': artist_name.title(), 'title': album_title.title()}
	if track_count:
		album['track_count'] = track_count
	return album

beatles_info = make_album('the beatles', 'the white album')
print(beatles_info)

shlohmo_info = make_album('shlohmo', 'bad vibes')
print(shlohmo_info)

joji_info = make_album('joji','midsummer madness')
print(joji_info)

frank_info = make_album('frank ocean','blonde','10')
print(frank_info)