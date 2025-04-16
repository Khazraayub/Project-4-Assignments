import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f"⏳ Time left: {timer}", end='\r')  # overwrite same line
        time.sleep(1)
        seconds -= 1
    print("\n🚨 Time's up!")

def main():
    print("🕒 Countdown Timer")
    try:
        choice = input("Do you want to enter time in (s)econds or (m)inutes? ").lower()
        if choice == 's':
            total_seconds = int(input("Enter time in seconds: "))
        elif choice == 'm':
            minutes = int(input("Enter time in minutes: "))
            total_seconds = minutes * 60
        else:
            print("Invalid choice ❌..Firstly enter seconds or minutes?")     
            return 0 
        countdown_timer(total_seconds)
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
