import datetime
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class MovieTicketBooking:
    def __init__(self):
     
        self.movies = {
            "1": {"name": "KARUDAN", "price": 800.0},
            "2": {"name": "MAHARAJA", "price": 550.0},
            "3": {"name": "GHILLI ", "price": 400.0},
            "4": {"name": "KALKI" , "price": 350},
            "5": {"name": "PT SIR", "price" : 300}
        }
        self.bookings = {movie: [] for movie in self.movies.keys()}
        self.selected_movie = None
        self.seat_number = None
        self.booking_time = None
        self.email = None

    def display_movies(self):
        print("Available Movies:")
        for key, movie in self.movies.items():
            print(f"{key}. {movie['name']} - Rs. {movie['price']}")

    def select_movie(self):
        self.display_movies()
        choice = input("Select a movie by entering the corresponding number: ")
        if choice in self.movies:
            self.selected_movie = choice
        else:
            print("Invalid selection. Please try again.")
            self.select_movie()

    def display_booked_seats(self):
        print("Currently booked seats:")
        if self.bookings[self.selected_movie]:
            for seat in self.bookings[self.selected_movie]:
                print(seat, end=" ")
            print()
        else:
            print("No seats booked yet.")

    def choose_seat(self):
        self.display_booked_seats()
        seat = input("Enter seat number (e.g., A10): ")
        if seat in self.bookings[self.selected_movie]:
            print("Seat already booked. Please choose another seat.")
            self.choose_seat()
        else:
            self.seat_number = seat
            self.bookings[self.selected_movie].append(seat)

    def input_email(self):
        email = input("Enter your email address: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.email = email
        else:
            print("Invalid email address. Please try again.")
            self.input_email()

    def generate_bill(self):
        self.booking_time = datetime.datetime.now()
        bill = f"""
        ---------------------------------
        Movie Ticket Booking Receipt
        ---------------------------------
        Movie: {self.movies[self.selected_movie]['name']}
        Date and Time: {self.booking_time.strftime('%Y-%m-%d %H:%M:%S')}
        Seat Number: {self.seat_number}
        Ticket Amount: ${self.movies[self.selected_movie]['price']}
        Email: {self.email}
        ---------------------------------
        Thank you for booking with us!
        """
        return bill

    def send_email(self, bill):
        # Email configuration
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        receiver_email = self.email

        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Your Movie Ticket Booking Receipt"
        msg.attach(MIMEText(bill, 'plain'))

        # Send the email
        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                print(f"Receipt sent to {self.email}")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")

    def book_ticket(self):
        self.select_movie()
        self.choose_seat()
        self.input_email()
        bill = self.generate_bill()
        print(bill)
        self.send_email(bill)

# Example usage
if __name__ == "__main__":
    booking_system = MovieTicketBooking()
    booking_system.book_ticket()

while True:
    display = input('Press enter to continue.')
    booking_system = MovieTicketBooking()
    booking_system.book_ticket()