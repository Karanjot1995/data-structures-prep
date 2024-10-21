package LLD.FlightReservation;

import java.util.HashSet;
import java.util.Set;

public class Flight {
    private String flightNumber;
    private String origin;
    private String destination;
    private int totalSeats;
    private Set<Integer> availableSeats;

    public Flight(String flightNumber,String origin, String destination, int totalSeats){
        this.flightNumber = flightNumber;
        this.origin = origin;
        this.destination = destination;
        this.totalSeats = totalSeats;
        this.availableSeats = new HashSet<>();
        for(int i =1;i<=totalSeats;i++){
            availableSeats.add(i);
        }
    }

    public String getFlightNumber(){
        return flightNumber;
    }

    public boolean isSeatAvailable(int seatNumber){
        return availableSeats.contains(seatNumber);
    }

    public boolean bookSeat(int seatNumber){
        if(isSeatAvailable(seatNumber)){
            availableSeats.remove(seatNumber);
            return true;
        }else{
            return false;
        }
    }

    public Set<Integer> getAvailableSeats(){
        return availableSeats;
    }

    @Override
    public String toString() {
        return "Flight " + flightNumber + " from " + origin + " to " + destination + ". Available seats: " + availableSeats;
    }
}
