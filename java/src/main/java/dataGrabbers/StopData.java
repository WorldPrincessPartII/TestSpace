package dataGrabbers;

import com.google.transit.realtime.GtfsRealtime;
import objects.ArrivingBus;

import java.net.URL;
import java.util.ArrayList;
import java.util.Collections;

public class StopData {
    public static void get(String stop) throws Exception {

        ArrayList<ArrivingBus> arrivalList = new ArrayList<ArrivingBus>();

        URL url = new URL("https://gtfsrt.api.translink.com.au/Feed/SEQ");
        GtfsRealtime.FeedMessage feed = GtfsRealtime.FeedMessage.parseFrom(url.openStream());
        for (GtfsRealtime.FeedEntity entity : feed.getEntityList()) {
            if (entity.hasTripUpdate()) {
            ArrayList<GtfsRealtime.FeedEntity> stopList = new ArrayList<GtfsRealtime.FeedEntity>();
            for (int i=0; i < entity.getTripUpdate().getStopTimeUpdateList().size(); i++) {
                GtfsRealtime.TripUpdate.StopTimeUpdate stopUpdate = entity.getTripUpdate().getStopTimeUpdate(i);
                if (stopUpdate.getStopId().equals(stop)) {
                    long timeCurrent = System.currentTimeMillis() / 1000;
                    long timeArrival = stopUpdate.getDeparture().getTime();

                    int timeGap = (int) (timeArrival - timeCurrent);

                    if (timeGap >= 0){
                        String rawVehicle = entity.getTripUpdate().getVehicle().getId().split("_")[1];

                        int fleetNo = Integer.parseInt(rawVehicle);

                        String routeSt = entity.getTripUpdate().getTrip().getRouteId().split("-")[0];

                        int route = Integer.parseInt(routeSt);


                        ArrivingBus bus = new ArrivingBus(route, timeGap, fleetNo);
                        arrivalList.add(bus);
                    }


                }

            }
            }
        }
        Collections.sort(arrivalList);
        System.out.println(arrivalList);
    }


}
