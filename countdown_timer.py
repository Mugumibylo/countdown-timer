import time

def countdown_timer(seconds):
    """Start a countdown timer for the given number of seconds."""
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(time_format, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up! 🎉")

def main():
    """Main function to run the Countdown Timer app."""
    print("Welcome to the Countdown Timer!")
    try:
        seconds = int(input("Enter the countdown time in seconds: "))
        if seconds <= 0:
            print("Please enter a positive number.")
        else:
            print(f"Starting countdown for {seconds} seconds...")
            countdown_timer(seconds)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
