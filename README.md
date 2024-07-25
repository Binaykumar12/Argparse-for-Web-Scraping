# Web Scraping Script

## Description

This Python script allows you to scrape text from paragraphs on a webpage and save it to a file. It uses `argparse` for command-line arguments, `requests` to fetch web content, and `BeautifulSoup` for parsing HTML.

## Features

- **Command-Line Interface**: Specify the URL of the webpage and the output file for the scraped data.
- **Text Extraction**: Extracts all paragraph text from the specified webpage.
- **Easy to Use**: Run the script with straightforward arguments.

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/web-scraping-script.git
    cd web-scraping-script
    ```

2. Install the required Python packages:
    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

Run the script using the command line:

```bash
python scrape.py <URL> <output_file>
