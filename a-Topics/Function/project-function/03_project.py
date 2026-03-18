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

def sort_by_duration(songs):
    sorted_songs = sorted(songs, key=lambda s: s["duration"], reverse=True)
    return sorted_songs

def full_playlist_report():
    print("\n============================================")
    print("      🎵  MUSIC PLAYLIST MANAGER  🎵      ")
    print("============================================")

    # Step 1 — collect songs
    songs = add_song()

    # Step 2 — show playlist
    show_playlist(songs)
    
    # Step 3 — total duration
    total = get_total_duration(songs)
    print(f"\n  ⏱  Total Duration  : {total} mins")

    # Step 4 — longest song
    longest = longest_song(songs)
    print(f"  🎵 Longest Song    : {longest['title']} - Artist: {longest['artist']} - Duration: {longest['duration']} mins")

    # Step 5 — sorted playlist
    sorted_songs = sort_by_duration(songs)
    print("\n--- 🔃 Sorted Playlist (Longest First) ---")

    for i, song in enumerate(sorted_songs, 1):
        print(f"  {i}. {song['title']:<20} - Artist: {song['artist']:<15} - Duration: {song['duration']} mins")
    print("------------------------------------------")

    # Step 6 — search song
    keyword = input("\n  Search a song: ")
    results = search_song(songs, keyword)

    if results:
        print(f'\n  Results for "{keyword}":')
        for i, song in enumerate(results, 1):
            print(f"  {i}. {song['title']} - Artist: {song['artist']} - Duration: {song['duration']} mins")
    else:
        print("  No song found! 🚫")

    print("\n============================================")


# --- Run the program ---
full_playlist_report()