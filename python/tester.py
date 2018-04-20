def getStopName(fileName, stopNo):
  fullList = open(fileName, 'r')
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
      postRouteName = stopName[0]
      postRouteName += ' ' + prepostStopName.partition(',')[0] + '\n'
      fullList.close()
      break
  return postRouteName

print getRouteNameFormatted('130-1020')

print getStopName('stops.txt', 5817)


