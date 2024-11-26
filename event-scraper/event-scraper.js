const puppeteer = require("puppeteer");

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
    // Function to extract content from divs with class "mb-3" and attribute xs="12"
    const extractH5Content = () => {
      return Array.from(document.querySelectorAll('div.mb-3[xs="12"]'))
        .map((div) => {
          const h5 = div.querySelector("h5");
          return h5 ? h5.textContent.trim() : null;
        })
        .filter((content) => content !== null);
    };

    // Function to extract content from divs with class "caps-md text-secondary mb-2"
    const extractSecondaryContent = () => {
      return Array.from(
        document.querySelectorAll("div.caps-md.text-secondary.mb-2")
      )
        .map((div) => div.textContent.trim())
        .filter((content) => content !== null);
    };

    // Function to extract content from h6 elements with class "mb-0 mt-2"
    const extractCostContent = () => {
      return Array.from(document.querySelectorAll("h6.mb-0.mt-2"))
        .map((h6) => h6.textContent.trim())
        .filter((content) => content !== null);
    };

    const h5Content = extractH5Content();
    const secondaryContent = extractSecondaryContent();
    const costContent = extractCostContent();

    // Combine the extracted content into a single array of objects
    const eventDetails = h5Content.map((h5, index) => ({
      h5Content: h5,
      secondaryContent: secondaryContent[index] || "",
      costContent: costContent[index] || "",
    }));

    return eventDetails;
  });

  // Print each event's details on a single line
  eventDetails.forEach((event, index) => {
    console.log(
      `Event ${index + 1}: ${event.h5Content} | ${event.secondaryContent} | ${
        event.costContent
      }`
    );
  });

  await browser.close();
})();
