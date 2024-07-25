import argparse
import requests
from bs4 import BeautifulSoup

def scrape(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extract all text from paragraphs
    paragraphs = soup.find_all('p')
    with open(output_file, 'w') as file:
        for para in paragraphs:
            file.write(para.get_text() + '\n')
    print(f"Scraping completed. Data saved to {output_file}")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Web scraping script")
    
    # Add arguments
    parser.add_argument('url', type=str, help="URL of the website to scrape")
    parser.add_argument('output_file', type=str, help="File to save the scraped data")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call the scrape function with the provided arguments
    scrape(args.url, args.output_file)

if __name__ == "__main__":
    main()
