from flask import Flask, render_template
import requests

# Web interface implementation

app = Flask(__name__)

# Exclusion list for non-cuisine tags that should not be displayed in the web interface
EXCLUDED_CUISINES = ['Low Delivery Fee', 'Deals']

def fetch_restaurants(postcode):
    # Header added to mimic a request from web browser, else request results in 403 Forbidden
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    # The API endpoint URL with inputted postcode
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    try:
        # Get request
        response = requests.get(url, headers=headers)
        # Check if the response status code is 200 (OK), and raise an exception for 4xx or 5xx errors
        response.raise_for_status()
    except requests.RequestException as e:
        # Print the error and return an empty list if an exception occurred during the request
        print(f"Request exception: {e}")
        return []
    
    # Parse the JSON response from the API
    data = response.json()

    filtered_restaurants = []
    # Get the first 10 restaurants from the response, if available
    restaurants = data.get('restaurants', [])[:10]
    for restaurant in restaurants:
        # Extract the restaurant name
        name = restaurant['name']
        # Filter out excluded cuisines based on their cuisine names (i.e. not actual cuisine types)
        cuisines = ', '.join([cuisine['name'] for cuisine in restaurant['cuisines'] if cuisine['name'] not in EXCLUDED_CUISINES])
        # Extract the star rating, default to 'N/A' if not available (assuming we want to display starRating for rating)
        rating = restaurant['rating']['starRating'] if 'rating' in restaurant and 'starRating' in restaurant['rating'] else 'N/A'
        # Parsing full address
        address_components = restaurant['address']
        address = f"{address_components['firstLine']}, {address_components['city']}, {address_components['postalCode']}"
        
        # Append the filtered restaurant data to the list
        filtered_restaurants.append({
            'name': name,
            'cuisines': cuisines,
            'rating': rating,
            'address': address
        })

    return filtered_restaurants

@app.route('/')
def home():
    # Get restaurant data in desired format with hardcoded postcode
    # Replace 'IP327GH' with desired postcode
    postcode = 'IP327GH'
    restaurants = fetch_restaurants(postcode)
    # Render index.html template, passing in postcode and the fetched restaurant data
    return render_template('index.html', postcode=postcode, restaurants=restaurants)

if __name__ == '__main__':
    # Run the Flask app with debugging enabled
    app.run(debug=True)
