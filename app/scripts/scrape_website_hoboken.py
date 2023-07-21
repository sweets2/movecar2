import requests
from bs4 import BeautifulSoup

# IMPORTANT: installation on PythonAnywhere may require this command:
# sudo apt-get install python3-bs4

def create_hoboken_street_cleaning_schedule_file():
    """Use beautifulsoup to scrape the Hoboken municipal website showing
    their street cleaning schedule. This data should not change often, 
    but in case it does run this script every few months to pull new data.
    Be sure to carefully check new rules against the old ones."""
    url = "https://www.hobokennj.gov/resources/street-cleaning-schedule"

    try:
        # Make a request to the website
        response = requests.get(url, timeout=10)  # timeout after 10 seconds

        # Check if request was successful
        response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # An  HTTP error

    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting: {conn_err}")  # A network problem

    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")  # The request timed out

    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")  # Other type of error
    
    else:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the unique container that contains 'table-content'
        container = soup.find_all('div', class_='table-content')

        # Find the divs that contain the table data needed
        table = []
        for div in container:
            links_in_div = div.find_all('div')
            if links_in_div:
                for link in links_in_div:
                    table.append(link.text)

        with open('app/data/rawdata/output.txt', 'w') as f:
            for div in table:
                f.write(div + '\n')

    # Add more functionality to check the output differs from
    # the raw_hoboken_rules.txt file
create_hoboken_street_cleaning_schedule_file()