# Add song function
def add_song():
    songs = []
    total_songs = int(input("Enter how many song to add : "))

    for i in range(1, total_songs + 1):
        title = input(f"Enter song {i} title : ")
        artist = input(f"Enter the name of song {i} artist : ")
        duration = int(input(f"Enter the song's {i} duration : "))

        songs.append ({
            "title" : title,
            "artist" : artist,
            "duration" : duration
        })

    return songs
