## Project: Event Details Extractor

This project uses Puppeteer to scrape event details from the Sydney Startup Hub community events page (https://community.sydneystartuphub.com/events) and exports them to an Excel file (event-details.xlsx) using XLSX.

### Requirements:

- Node.js and npm (or yarn) installed on your system. You can check by running node -v and npm -v (or yarn -v) in your terminal.
- A web browser (Chrome or Chromium is recommended for compatibility with Puppeteer).

### Setup:

1. **Clone or download the repository.**
2. **Navigate to the project directory** in your terminal.
3. **Install dependencies**: Run npm install (or yarn install) to install the required packages: Puppeteer and XLSX.

### Running the Script:

1. **Run the script**: Execute `node event-scraper.js` in your terminal.
2. **Output**: The script will create a file named `event-details.xlsx` in your project directory containing the extracted event details.

### Understanding the Script:

- **Puppeteer**: Launches a headless Chrome browser instance to interact with the website.
- **XLSX**: Provides functions to create and write Excel files.

### Customization:

- You can modify the target website URL in the page.goto line to scrape data from a different URL.
- The extraction logic (specifically the CSS selectors used) might need adjustments if the website's structure changes.
