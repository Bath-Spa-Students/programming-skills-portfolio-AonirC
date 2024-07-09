#cities
def describe_city(city, country='Japan'):
    """City Description."""
    
    message = city.title() + " is in " + country.title() + "."
    print(message)

describe_city('osaka')
describe_city('yokohama', 'japan')
describe_city('kyoto')
