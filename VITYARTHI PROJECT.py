# ==================== EASYBOOK - MOVIE TICKET BOOKING ====================


shows = [
    {"id": 1, "movie": "Avatar 3",     "date": "2025-11-25", "time": "10:00 AM", "seats_left": 60},
    {"id": 2, "movie": "Avatar 3",     "date": "2025-11-25", "time": "06:00 PM", "seats_left": 60},
    {"id": 3, "movie": "Wicked",       "date": "2025-11-26", "time": "02:00 PM", "seats_left": 60},
    {"id": 4, "movie": "Deadpool 3",   "date": "2025-11-27", "time": "09:00 PM", "seats_left": 60},
    {"id": 5, "movie": "Moana 2",      "date": "2025-11-28", "time": "11:00 AM", "seats_left": 60},
]

users = {}        
bookings = {}     

def clear_screen():
    print("\n" * 50)

def print_header(text):
    print("\n" + "=" * 50)
    print(text.center(50))
    print("=" * 50)

def view_shows():
    print("\nAVAILABLE SHOWS")
    print("-" * 70)
    print(f"{'ID':<4} {'Movie':<20} {'Date':<12} {'Time':<12} {'Seats Left'}")
    print("-" * 70)
    for show in shows:
        if show["seats_left"] > 0:
            print(f"{show['id']:<4} {show['movie']:<20} {show['date']:<12} {show['time']:<12} {show['seats_left']}")
    print("-" * 70)

def register():
    print_header("REGISTER")
    username = input("Enter username: ").strip().lower()
    password = input("Enter password: ").strip()
    
    if username in users:
        print("Username already exists!")
    elif len(password) < 4:
        print("Password too short!")
    else:
        users[username] = password
        print("Registration successful!")
    input("\nPress Enter to continue...")

def login():
    print_header("LOGIN")
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()
    
    if username in users and users[username] == password:
        print(f"\nWelcome {username.capitalize()}!")
        return username
    else:
        print("Wrong username or password!")
        return None

def book_ticket(username):
    view_shows()
    try:
        show_id = int(input("\nEnter Show ID: "))
        tickets = int(input("Number of tickets: "))
        
        show = next((s for s in shows if s["id"] == show_id), None)
        if not show:
            print("Invalid Show ID!")
        elif show["seats_left"] < tickets:
            print("Not enough seats!")
        else:
            price = tickets * 200
            if username not in bookings:
                bookings[username] = []
            bookings[username].append(f"{show['movie']} | {show['date']} {show['time']} | {tickets} ticket(s) | ₹{price}")
            show["seats_left"] -= tickets
            print(f"\nBOOKED SUCCESSFULLY! Total: ₹{price}")
    except:
        print("Invalid input!")
    input("\nPress Enter to continue...")

def my_bookings(username):
    print_header("MY BOOKINGS")
    if username not in bookings or not bookings[username]:
        print("No bookings yet!")
    else:
        for i, booking in enumerate(bookings[username], 1):
            print(f"{i}. {booking}")
    input("\nPress Enter to continue...")

def cancel_booking(username):
    my_bookings(username)
    if username not in bookings or not bookings[username]:
        return
    
    try:
        num = int(input("\nEnter booking number to cancel: ")) - 1
        if 0 <= num < len(bookings[username]):
            cancelled_booking = bookings[username][num]
            movie_name = cancelled_booking.split(" | ")[0]
            
            tickets_count = int(cancelled_booking.split(" ticket")[0].split()[-1])
            
            for show in shows:
                if show["movie"] == movie_name and show["date"] + " " + show["time"] == cancelled_booking.split(" | ")[1]:
                    show["seats_left"] += tickets_count
                    break
            del bookings[username][num]
            print("Booking cancelled successfully!")
        else:
            print("Invalid number!")
    except:
        print("Invalid input!")
    input("\nPress Enter to continue...")


while True:
    clear_screen()
    print_header(" EASYBOOK - MOVIE TICKETS ")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose (1-3): ")

    if choice == "3":
        print("Thank you for using EasyBook!")
        break
    elif choice == "1":
        register()
    elif choice == "2":
        username = login()
        if username:
            while True:
                clear_screen()
                print_header(f" WELCOME {username.upper()} ")
                print("1. Book Ticket")
                print("2.My Bookings")
                print("3. Cancel Booking")
                print("4. Logout")
                ch = input("Choose (1-4): ")

                if ch == "1":
                    book_ticket(username)
                elif ch == "2":
                    my_bookings(username)
                elif ch == "3":
                    cancel_booking(username)
                elif ch == "4":
                    break