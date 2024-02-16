song_library = {}

while True:
    print("\nSong Library Menu:")
    print("1. Add a song")
    print("2. Sort songs by title")
    print("3. Sort songs by artist")
    print("4. Sort songs by genre")
    print("5. Search for a song")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the song title: ")
        artist = input("Enter the artist name: ")
        genre = input("Enter the genre: ")
        song_library[title] = {"artist": artist, "genre": genre}
        print(f"{title} added to the song library.")
    elif choice == "2":
        print("\nSorted songs by title:")
        for title in sorted(song_library.keys()):
            print(f"{title} - {song_library[title]['artist']} ({song_library[title]['genre']})")
    elif choice == "3":
        print("Sorted songs by artist:")
        for title in sorted(song_library.keys(), key=lambda x: song_library[x]['artist']):
            print(f"{title} - {song_library[title]['artist']} ({song_library[title]['genre']})")
    elif choice == "4":
        print("Sorted songs by genre:")
        for title in sorted(song_library.keys(), key=lambda x: song_library[x]['genre']):
            print(f"{title} - {song_library[title]['artist']} ({song_library[title]['genre']})")
    elif choice == "5":
        search_title = input("Enter the song title to search: ")
        if search_title in song_library:
            details = song_library[search_title]
            print(f"\nSong: {search_title}")
            print(f"Artist: {details['artist']}")
            print(f"Genre: {details['genre']}")
        else:
            print(f"{search_title} not found in the song library.")
    elif choice == "0":
        print("Exiting. Keep the music playing!")
        break
    else:
        print("Invalid choice. Please select a valid option.")