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

def show_playlist(songs):
    print("--- 🎵 Your Playlist ---")

    for i, song in enumerate(songs, 1):
        print(f"{i}. {song['title']:<20} - Artist {song['artist']:<15} - Duration {song['duration']} mins.")
        print("------------------------")

def get_total_duration(songs):
    total = 0

    for song in songs:
        total += song["duration"]
    return total

def longest_song(songs):
    longest = songs[0]

    for song in songs:
        if song['duration'] > longest['duration']:
            longest = song
    return longest

def search_song(songs, keyword):
    result = []

    for song in songs:
        if keyword.lower() in song['title'].lower() or \
        keyword.lower() in song['artist'].lower():
            result.append(song)
    return result


        