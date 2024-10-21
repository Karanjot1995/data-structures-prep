package LLD.FlightReservation;

import java.util.Set;

public class Passenger {
    private String name;
    private String passportNumber;

    public Passenger(String name, String passportNumber){
        this.name = name;
        this.passportNumber = passportNumber;
    }
    public String getName() {
        return name;
    }
    public String getPassportNumber() {
        return passportNumber;
    }
}
