package objects;

import java.lang.Comparable;

public class ArrivingBus implements Comparable<ArrivingBus>{

    private int route;
    private int secondsLeft;
    private int fleetNo;

    public ArrivingBus(int rt, int sl, int fn ){
        route = rt;
        secondsLeft = sl;
        fleetNo = fn;
    }

    public int getRoute(){
        return route;
    }

    public int getSecondsLeft(){
        return secondsLeft;
    }

    public int getFleetNo() {
        return fleetNo;
    }

    public int getMinutesLeft() {
        return secondsLeft/60;
    }

    @Override
    public String toString(){
        return String.format("%nBus %d on route %d is currently %d minutes away", fleetNo, route, this.getMinutesLeft());
    }

    @Override
    public int compareTo(ArrivingBus a){
        int result = Integer.compare(secondsLeft, a.getSecondsLeft());
        return result;
    }
}
