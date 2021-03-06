# Faster than HL3 I did it
# Finds routes passing by a stop, then spits out details and departure times

from google.transit import gtfs_realtime_pb2
import urllib
import time
from operator import itemgetter

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('https://gtfsrt.api.translink.com.au/Feed/SEQ')
feed.ParseFromString(response.read())

arrivalList = []

for entity in feed.entity:
  if entity.HasField('trip_update'):
    for stopUpdate in entity.trip_update.stop_time_update:
      if stopUpdate.stop_id == '5817': ## stop number here
          #print entity.trip_update.trip.trip_id
          timeCurrent = int(time.time())
          timeArrival = stopUpdate.arrival.time
          timeGap = timeArrival-timeCurrent
          if timeGap >= 0:
            print entity.trip_update.trip.route_id
            fleetNo = entity.trip_update.vehicle.id.split('_')
            print '{} {}'.format('Bus number:', fleetNo[1])
            stopNo = stopUpdate.stop_id
            print '{} {} {}'.format(timeGap/60, 'minutes to stop', stopNo)

            route = (str(fleetNo[1]), int(timeGap/60))
            arrivalList.append(route)

sorted(arrivalList,key=itemgetter(1))

for i in arrivalList:
  print i

          #print stopUpdate.stop_id
    
##      if entity.trip_update.trip.route_id.startswith('130'):
##          print entity.trip_update.trip.trip_id
##          print entity.trip_update.trip.route_id
##          print entity.trip_update.vehicle.id
##          print entity.trip_update.stop_time_update[0].stop_id
          
            
