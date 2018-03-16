from google.transit import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('https://gtfsrt.api.translink.com.au/Feed/SEQ')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
      if entity.trip_update.trip.route_id.startswith('130'):
          print entity.trip_update.trip.trip_id
          print entity.trip_update.trip.route_id
    
    
