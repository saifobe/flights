# flights

# Event Weather and Flight API

### This project is a Python Django API that provides information about events, weather, and flights. 
### It consumes external 3rd party APIs to list events in a country, retrieve the current weather at the event location, and provide a list of flights to attend those events based on the user's airport code.
<br>

#### Note: This project was developed as part of an interview application for PwC.


<br>

---
<br>

### Installation
#### To run this project locally, follow these steps:
<br>

- Clone the repository:
    ```
    git clone git@github.com:Esmail-Jawabreh/PWC-API-Task.git
    ```

<br>

- Create a virtual environment: 
    ```
    python -m venv venv
    ```

<br>

- Activate the virtual environment:

<br>

- Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

<br>

- Apply the database migrations:
    ```
    python manage.py migrate
    ```

<br>

### Usage
#### To use the API, follow these steps:

- Start the Django development server:
    ```
    python manage.py runserver
    ```

<br>

- Access the API endpoints using a tool like cURL, Postman, or any HTTP client of your choice.

    - To retrieve a list of events in a specific country, make a GET request to http://localhost:8000/events/ with the country parameter set to the desired country code.

    - To get the current weather for a specific event, make a GET request to http://localhost:8000/weather/ with the id parameter set to the desired event ID.

    - To get a list of flights for a specific event and airport, make a GET request to http://localhost:8000/flights/ with the event_id and airport_code parameters set to the desired values.

- Inspect the responses from the API to get the requested information.


<br>

### API Endpoints
<br>

- events/
    - Description: Retrieve a list of events in a specific country.
    - Method: GET
    - Parameters:
        - country: The country code (e.g., "US", "GB").
    - Response: JSON object containing a list of events.

<br>

- weather/
    - Description: Retrieve weather information for a specific event.
    - Method: GET
    - Parameters        
        - id: The ID of the event.
    - Response: JSON object containing weather information.

<br>

- flights/
    - Description: Retrieve a list of flights for a specific event and airport.
    - Method: GET
    - Parameters:
        - event_id: The ID of the event.
        - airport_code: The airport code.
    - Response: JSON object containing a list of flights.

<br>


### Technologies Used

#### The project uses the following technologies and libraries:

- Python
- Django
- SQLite
- Django REST Framework
- Requests (for making HTTP requests to 3rd party APIs)

<br>

---
<br>

### License
#### This project is licensed under the MIT License. 

<br>

#### Feel free to modify and adapt this project according to your needs.

#### Please let me know if you have any further questions or need assistance with anything else!

<br>

---

<br>

**- Saif Obeidat**