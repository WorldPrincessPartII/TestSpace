package dataGrabbers;
import java.net.URL;

import com.google.transit.realtime.GtfsRealtime.FeedEntity;
import com.google.transit.realtime.GtfsRealtime.FeedMessage;

public class AllData {
    public static void get() throws Exception {
        URL url = new URL("https://gtfsrt.api.translink.com.au/Feed/SEQ");
        FeedMessage feed = FeedMessage.parseFrom(url.openStream());
        for (FeedEntity entity : feed.getEntityList()) {
            if (entity.hasTripUpdate()) {
                System.out.println(entity.getTripUpdate());
            }
        }
    }
}