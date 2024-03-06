# Just Eat Assignment: Restaurant Finder

Simple Python/Flask-based web interface that fetches restaurant data (from Just Eat API), filters them and displays first 10 restaurants for a given postcode, more specifically displaying restaurant name, cuisine types, rating, and address

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. **Clone the Repository**

    ```
    git clone https://github.com/lazim66/just_eat_assignment.git
    cd just_eat_assignment
    ```

2. **Set Up Virtual Environment**

    - For macOS/Linux:
      ```
      python3 -m venv venv
      source venv/bin/activate
      ```

    - For Windows:
      ```
      python -m venv venv
      venv\Scripts\activate
      ```

3. **Install Dependencies**

    ```
    pip install -r requirements.txt
    ```

## Running  Application

1. **Start the Flask Application**


    ```
    python app.py
    ```

    By default, Flask will run the application on `http://127.0.0.1:5000/`

2. **View the Web Interface**

    Open a web browser and go to `http://127.0.0.1:5000/` to view the application with restaurant data

## Assumptions Made

- "Low Delivery Fee" and "Deals" are not considered as cuisine types and should not displayed in the web interface
- Rating data shown in interface is "starRating" from response data
- Just Eat API does not require authentication and the data structure returned is consistent (speficifcally resturant data like name, cuisines, rating, and address)
- No rate limiting or request restrictions imposed by API
- The application is designed to fetch and display the first 10 restaurants from the API response for a given postcode (as apposed to the nearest 10)

## Future Improvements

- **Dynamic Postcode Input:** Allow users to input a postcode dynamically through the web interface instead of using a hardcoded value
- **API Error Handling/validation:** Implement more comprehensive error handling/validation for cases like invalid postcodes or API unavailability or rate limiting, and provide clear feedback to users when data cannot be fetched
- **Pagination:** To handle potentially large datasets, introduce pagination feature to incrementally display/load more restaurants beyond the initial 10
- **Interactive Map Integration:** Integrate an interactive map (e.g. Google Maps), showing the location of each restaurant, improving user experience
- **Advanced Filtering and Sorting:** Introduce more filtering options (e.g., by cuisine type, rating, delivery options) and sorting (e.g., by distance) to help users find restaurants that match their specific preferences
- **More modern UI/UX:** Using icons/assets, custom fonts, annimations and more advanced CSS styling to improve look/feel of web interface, improving user experience
- **Responsive Design:** Improve the web interface's responsiveness and mobile compatibility with frameworks like Bootstrap
 - **Testing:** Add comprehensive tests (unit, integration, end-to-end) to ensure application's functionality and reliability, when making changes/adding new features
- **Deployment:** Deploy the application to cloud platform like Heroku or AWS for public access
- **User Authentication for personalisation:** Add user authentication to allow users to save their favorite restaurants and view their order history
- **Caching:** Reduce the number of API requests and improve performance
- **Logging:** Track and record errors
- **Localization:** Add support for multiple languages


