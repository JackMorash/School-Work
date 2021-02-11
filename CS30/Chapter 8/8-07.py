def make_album(artist, title):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('radiohead', 'ok computer')
print(album)

album = make_album('the beatles', 'yellow submarine')
print(album)

album = make_album('pink floyd', 'the dark side of the moon')
print(album)