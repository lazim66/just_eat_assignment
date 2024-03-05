import requests
# Basic implementation to fetch, filter and parse (first 10) restaurants data from API in desired format and display in console

# Exclusion list for non-cuisine tags that should not be displayed
EXCLUDED_CUISINES = ['Low Delivery Fee', 'Deals']

def fetch_and_display_restaurants(postcode):
    # header added to mimic a request from web browser, else request results in 403 Forbidden
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    try:
        response = requests.get(url, headers=headers)
        # Check if the response status code is 200 (OK)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occurred: {err}')
    else:
        data = response.json()

        # Get resturants object from the response
        restaurants = data.get('restaurants', [])[:10]  # Get the first 10 restaurants
        print("Restaurants List")
        print("-" * 80)
        for restaurant in restaurants:
            name = restaurant['name']
            # Filter out excluded cuisines based on their cuisine names (i.e. not actual cuisine types)
            cuisines = ', '.join([cuisine['name'] for cuisine in restaurant['cuisines'] if cuisine['name'] not in EXCLUDED_CUISINES])
            
            # Assuming we want to display starRating for rating
            rating = restaurant['rating']['starRating'] if 'rating' in restaurant and 'starRating' in restaurant['rating'] else 'N/A'
            
            # Parsing full address
            address_components = restaurant['address']
            address = f"{address_components['firstLine']}, {address_components['city']}, {address_components['postalCode']}"
            
            # Displaying desired restaurant details in console
            print(f"Name: {name}")
            print(f"Cuisines: {cuisines}")
            print(f"Rating: {rating}")
            print(f"Address: {address}")
            print("-" * 80)  # Separator line

# Replace with the postcode of choice
fetch_and_display_restaurants('IP327GH')
