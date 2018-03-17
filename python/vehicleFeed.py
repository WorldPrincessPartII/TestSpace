# Faster than HL3 I did it
# Finds routes passing by a stop, then spits out details and departure times

from google.transit import gtfs_realtime_pb2
import urllib
import time

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('https://gtfsrt.api.translink.com.au/Feed/SEQ')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
      if entity.trip_update.vehicle.id.startswith('-1366625436'):
          print entity.trip_update.trip.trip_id
          print entity.trip_update.trip.route_id
          fleetNo = entity.trip_update.vehicle.id.split('_')
          print '{} {}'.format('Bus number:', fleetNo[1])
          f = open("seq.txt",'a')
          f.write('{} {} \n'.format('Bus number:', fleetNo[1]))
          f.close()
          #for stopUpdate in entity.trip_update.stop_time_update:
            #print stopUpdate.stop_id
            # Put into array, check array length
          
            
