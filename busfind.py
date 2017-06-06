import urllib2
import xml.etree.ElementTree
print "MA Bus Tracker"
apikey = "apikeygoeshere"
lat = raw_input("Latitude: ")#"42.346961"
lon = raw_input("Longitude: ")#"-71.076640"
url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key="+apikey+"&lat="+str(lat)+"&lon="+str(lon)+"&format=xml"
f = urllib2.urlopen(url)
data = f.read()
e = xml.etree.ElementTree.fromstring(data)
for atype in e.findall('stop'):
    print(atype.get('stop_name') + " | " + atype.get('stop_lat')+", "+atype.get('stop_lon') + " | " + atype.get('distance')+" miles")
