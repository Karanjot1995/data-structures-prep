package LLD.FlightReservation;

public class Main {
    public static void main(String[] args) {
        FlightReservationSystem system = new FlightReservationSystem();

        // Adding flights
        system.addFlight("AA101", "Dallas", "New York", 10);
        system.addFlight("AA102", "Los Angeles", "Chicago", 5);

        // Display available seats
        system.displayAvailableSeats("AA101");

        // Booking seats
        system.bookSeat("AA101", 3);
        system.bookSeat("AA101", 3);  // Trying to book the same seat again (should fail)

        // Display available seats after booking
        system.displayAvailableSeats("AA101");

        // Booking a seat on a non-existent flight (should fail)
        system.bookSeat("AA999", 1);
    }
}
