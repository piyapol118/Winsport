import googlemaps

API_KEY = "AIzaSyBNxV6a58n1dIk99fqVhjgcOmdT9PPI__U"
map_client = googlemaps.Client(API_KEY)
def cal_range():
    startdestination = [13.7294363, 100.7785291]
    enddestination = [13.7294363, 100.7785291]


    distance = map_client.directions(startdestination, enddestination)

    Kdistance = (distance[0]["legs"][0]["distance"]["text"])
    Hrsmindu = (distance[0]["legs"][0]["duration"]["text"])

    return(Kdistance, Hrsmindu)

cal_range()
