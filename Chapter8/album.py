def make_album(artist, title):
    album_dictionary = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dictionary

album = make_album('Reba McEntire', 'The Night That The Lights Went Out In Georgia')
print(album)

album = make_album('Don Williams', 'Stand On It')
print(album)

album = make_album('CW McCall', 'Convoy')
print(album)
print("---------------Part 2---------------")

def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('Reba McEntire', 'The Night That The Lights Went Out In Georgia')
print(album)

album = make_album('Don Williams', 'Stand On It')
print(album)

album = make_album('CW McCall', 'Convoy')
print(album)

album = make_album('Your The Only One', 'Melissa Ethridge', tracks=10)
print(album)

print("--------------------8-8--------------------")
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")

