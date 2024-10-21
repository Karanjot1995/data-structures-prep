package LLD.FlightReservation;

import java.util.HashMap;
import java.util.Map;

public class FlightReservationSystem {
    // Map from flightNumber to Flight
    private Map<String, Flight> flights;

    public FlightReservationSystem() {
        flights = new HashMap<>();
    }

    public void addFlight(String flightNumber, String origin, String destination, int totalSeats){
        Flight flight = new Flight(flightNumber, origin, destination, totalSeats);
        flights.put(flightNumber,flight);
    }

    public boolean bookSeat(String flightNumber, int seatNumber){
        Flight flight = flights.get(flightNumber);
        if (flight == null) {
            System.out.println("Flight not found.");
            return false;
        }
        boolean success = flight.bookSeat(seatNumber);
        if (success) {
            System.out.println("Seat " + seatNumber + " booked on flight " + flightNumber);
        } else {
            System.out.println("Seat " + seatNumber + " is already booked or invalid.");
        }
        return success;
    }

    public void displayAvailableSeats(String flightNumber) {
        Flight flight = flights.get(flightNumber);
        if (flight != null) {
            System.out.println(flight);
        } else {
            System.out.println("Flight not found.");
        }
    }

}
