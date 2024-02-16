movie_ratings = {}

while True:
    print("Movie Rating System:")
    print("1. Rate a movie")
    print("2. View average ratings")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        movie_title = input("Enter the movie title: ")
        rating = int(input("Rate the movie (1-5): "))

        if 1 <= rating <= 5:
            if movie_title in movie_ratings:
                movie_ratings[movie_title].append(rating)
            else:
                movie_ratings[movie_title] = [rating]
            print(f"Rating {rating} added for {movie_title}.")
        else:
            print("Invalid rating. Please enter a number between 1 and 5.")
    elif choice == "2":
        print("Average Ratings:")
        for movie, ratings in movie_ratings.items():
            average_rating = sum(ratings) / len(ratings)
            print()
            print(f"{movie}: {average_rating:.2f} stars")
            print()
    elif choice == "0":
        print("Bye...")
        break
    else:
        print("Invalid choice. Please select a valid option.")