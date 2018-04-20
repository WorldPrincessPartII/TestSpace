# Faster than HL3 I did it
# Finds routes passing by a stop, then spits out details and departure times

from google.transit import gtfs_realtime_pb2
import urllib
import time

def getStopName(stopNo):
  fullList = open('stops.txt', 'r')
  postStopName = ''
  for line in fullList:
    lineSplit = line.partition(',')
    stop = lineSplit[0]
    if str(stopNo) == stop:
      preStopName = lineSplit[2]
      stopName = preStopName.partition(',')[2]
      postStopName = stopName.partition(',')[0]
      fullList.close()
      break
  return postStopName

def getRouteNameFormatted(routeNo):
  fullList = open('routes.txt', 'r')
  postRouteName = ''
  for line in fullList:
    lineSplit = line.partition(',')
    route = lineSplit[0]
    if str(routeNo) == route:
      preStopName = lineSplit[2]
      stopName = preStopName.partition(',')
      prepostStopName = stopName[2]
      postRouteName = 'Route:\n' + stopName[0]
      postRouteName += ' ' + prepostStopName.partition(',')[0] + '\n'
      fullList.close()
      break
  return postRouteName

def convertMinSec(longSec):
  minutes = longSec//60
  seconds = (longSec/60)-minutes
  seconds = (seconds*60)//1
  return '{:02.0f}:{:02.0f}'.format(minutes,seconds)
  
  

bus = raw_input("Which Brisbane Transport bus?: ")
bus = '-1366625436_' + bus
feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('https://gtfsrt.api.translink.com.au/Feed/SEQ')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
      if entity.trip_update.vehicle.id.startswith(bus):
          #print entity.trip_update.trip.trip_id
          routeStr = str(entity.trip_update.trip.route_id)
          print getRouteNameFormatted(routeStr)
          print "Stops:"
          for stopUpdate in entity.trip_update.stop_time_update:
            #print type(stopUpdate.stop_id)
            busTime = stopUpdate.departure.time
            currentTime = time.time()
            depTime = busTime - currentTime
            minutesDep = convertMinSec(depTime)
            if depTime > 0:
              print '{}, arriving in {}\n'.format(getStopName(stopUpdate.stop_id), minutesDep)
            
            # Put into array, check array length


  
      
            
