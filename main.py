import json
import requests
import httplib2

GOOGLE_API_KEY = ''
FOURSQUARE_CLIENT_ID = ''
FOURSQUARE_CLIENT_SECRET = ''


def get_geo_location(place_name):
    """
    This function return coordinates of the place using google API
    :param place_name: Name of the place
    :return: A list with latitude and longitude

    """

    query_name = place_name.replace(' ', '+')
    url = 'https://maps.googleapis.com/maps/api/geocode/json?' \
          'address={}&key={}'.format(query_name, GOOGLE_API_KEY)
    http = httplib2.Http()
    response, result = http.request(url, 'GET')
    content = json.loads(result.decode())
    return [str(content['results'][0]['geometry'][
          'location']['lat']), str(content[
                                 'results'][0]['geometry']['location']['lng'])]


def nearby_finder(find, coordinates):
    """
    This function finds nearby places via coordinates giving in parameters using
    FourSquare API (max 10 places)
    :param find: Type of place you want to search ex restaurant, petrol pumps
    :param coordinates: coordinates of the location
    :return: return a list of search  results given by four square
    """

    url = 'https://api.foursquare.com/v2/venues/explore'

    params = dict(
        client_id=FOURSQUARE_CLIENT_ID,
        client_secret=FOURSQUARE_CLIENT_SECRET,
        v='20170801',
        ll=(coordinates[0]+","+coordinates[1]),
        query=find,
        limit=10
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    return data['response']['groups'][0]['items']


def find_nearby(find, place_name):
    """
    This function make use of above functions to make above process user
    friendly
    :param find: Type of place you want to find ex restaurant
    :param place_name: Name of the place
    :return: list of result obj in format {name:name of place , contact: contact
    details, address: address of place}
    """
    find = find.replace(" ", "+")
    coordinates = get_geo_location(place_name)
    nearby_list = nearby_finder(find, coordinates)
    nearby_result = []
    for nearby in nearby_list:
        nearby_result.append({
            'name': nearby['venue']['name'],
            'contact': nearby['venue']['contact'].get('phone', 'N/A'),
            'address': nearby['venue']['location'].get('address', 'N/A')
        })
    return nearby_result


if __name__ == '__main__':
    place = input('enter name of the place: ')
    search = input('enter what do you want to search nearby: ')
    for nearby in find_nearby(find=search, place_name=place):
        print('name: ' + nearby['name'])
        print('contact:' + nearby['contact'])
        print('address: ' + nearby['address'])
        print('------------------------------------------------\n ')
