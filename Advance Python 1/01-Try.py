while (True):
    print("Enter q to end this game")
    a = input("Enter a number\n")

    if a == 'q':
        break
    try:
        a = int(a)
        if a > 6:
            print("You have enterd a number greater than 6")
    except Exception as e:         # It will tell to user that what error is occuring ang program will not crash
        print(f"Your input result in an Error: {e}")


print("Thanks for playing this game")
