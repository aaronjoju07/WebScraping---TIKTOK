import csv
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.tiktok.com/@infinityhoop?lang=en'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all div elements with class "css-x6f6za-DivContainer-StyledDivContainerV2"
    video_containers = soup.find_all('div', class_='css-x6f6za-DivContainer-StyledDivContainerV2')
    
    # Create a CSV file to store the scraped data
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Define the CSV writer
        writer = csv.writer(csvfile)
        
        # Write the header row
        writer.writerow(['Video Link', 'Video Description'])
        
        # Loop through each video container
        for container in video_containers:
            # Find the anchor tag within the container
            link_tag = container.find('a')
            if link_tag:
                # Extract the video link
                video_link = link_tag['href']
                
                # Find the span tag within the container
                description_tag = container.find('span', class_='css-j2a19r-SpanText')
                if description_tag:
                    # Extract the video description
                    video_description = description_tag.text.strip()
                    
                    # Write the data to the CSV file
                    writer.writerow([video_link, video_description])
                    
    print('Data has been successfully scraped and saved to scraped_data.csv.')
                    
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
