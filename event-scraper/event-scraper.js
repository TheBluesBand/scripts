const puppeteer = require("puppeteer");
const XLSX = require("xlsx");

(async () => {
  // Initiate the browser
  const browser = await puppeteer.launch();

  // Create a new page in headless Chrome
  const page = await browser.newPage();

  // Go to the target website
  await page.goto("https://community.sydneystartuphub.com/events", {
    // Wait for content to load
    waitUntil: "networkidle0",
  });

  // Evaluate functions in the page context
  const eventDetails = await page.evaluate(() => {
    // Function to extract event details from divs with class "mb-3" and attribute xs="12"
    const extractEventDetails = () => {
      return Array.from(document.querySelectorAll('div.mb-3[xs="12"]'))
        .map((div) => {
          const h5 = div.querySelector("h5");
          const header = h5 ? h5.textContent.trim() : null;

          const timeDiv = div.querySelector("div.caps-md.text-secondary.mb-2");
          const time = timeDiv ? timeDiv.textContent.trim() : null;

          const costH6 = div.querySelector("h6.mb-0.mt-2");
          const cost = costH6 ? costH6.textContent.trim() : null;

          const addressDiv = div.querySelector("div.small.text-muted.mb-2");
          let address = null;
          if (addressDiv) {
            const addressLink = addressDiv.querySelector("a");
            const addressButton = addressDiv.querySelector("button");
            if (addressLink) {
              // Remove the span that says "(opens in a new tab)"
              const span = addressLink.querySelector("span");
              if (span && span.textContent.includes("opens in a new tab")) {
                span.remove();
              }
              // Get the cleaned address text
              address = addressLink.innerHTML
                .replace(/<span.*<\/span>/, "")
                .trim();
            } else if (addressButton) {
              address = addressButton.textContent.trim();
            }
          }

          return {
            header,
            time,
            cost,
            address,
          };
        })
        .filter((event) => event.header !== null);
    };

    return extractEventDetails();
  });

  // Print each event's details on a single line
  eventDetails.forEach((event, index) => {
    console.log(
      `Event ${index + 1}: ${event.header} | ${event.time} | ${event.cost} | ${
        event.address
      }`
    );
  });

  await browser.close();
})();
