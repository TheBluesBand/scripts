const puppeteer = require("puppeteer");
const XLSX = require("xlsx");

(async () => {
  try {
    const browser = await puppeteer.launch();
    console.log("Browser launched");

    const page = await browser.newPage();
    console.log("New page created");

    const allEventDetails = [];
    const MAX_PAGES = 50; // Limiting to 50 pages for performance
    const START_PAGE = 100; // Starting page

    const scrapePage = async (pageNumber) => {
      try {
        console.log(`Scraping page ${pageNumber}`);
        const url = `https://community.sydneystartuphub.com/events?filters=%7B%22startDate%22%3A%7B%22%24exists%22%3Atrue%7D%7D&page=${pageNumber}`;
        await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });

        await page.waitForSelector('div.mb-3[xs="12"]', { timeout: 30000 });
        console.log(`Page ${pageNumber} loaded`);

        const pageEventDetails = await page.evaluate(() => {
          return Array.from(document.querySelectorAll('div.mb-3[xs="12"]')).map((div) => {
            const h5 = div.querySelector("h5");
            const headerLink = h5 ? h5.querySelector("a") : null;
            const header = headerLink ? headerLink.textContent.trim() : null;
            const link = headerLink ? headerLink.href : null;

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
                const span = addressLink.querySelector("span");
                if (span && span.textContent.includes("opens in a new tab")) {
                  span.remove();
                }
                address = addressLink.innerHTML.replace(/<span.*<\/span>/, "").trim();
              } else if (addressButton) {
                address = addressButton.textContent.trim();
              }
            }

            return {
              header,
              link,
              time,
              cost,
              address,
            };
          });
        });

        for (let event of pageEventDetails) {
          if (event.link) {
            console.log(`Navigating to event link: ${event.link}`);
            await page.goto(event.link, { waitUntil: "domcontentloaded" });
            const blurb = await page.evaluate(() => {
              const blurbElement = document.querySelector("div.p-3");
              return blurbElement ? blurbElement.innerText.trim() : "No description available";
            });
            event.blurb = blurb;
            console.log(`Extracted blurb for event: ${event.header}`);
            await page.goBack({ waitUntil: "domcontentloaded" });
          }
        }

        allEventDetails.push(...pageEventDetails);

        console.log(`Scraped page ${pageNumber}. Total events: ${allEventDetails.length}`);
        return pageEventDetails.length > 0;
      } catch (error) {
        console.error(`Error scraping page ${pageNumber}:`, error);
        return false;
      }
    };

    for (let pageNum = START_PAGE; pageNum < START_PAGE + MAX_PAGES; pageNum++) {
      const continueScraping = await scrapePage(pageNum);
      if (!continueScraping) {
        break;
      }
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }

    const workbook = XLSX.utils.book_new();
    const worksheetData = [
      ["Header", "Time", "Cost", "Address", "Blurb", "Link"],
      ...allEventDetails.map((event) => [
        event.header,
        event.time,
        event.cost,
        event.address,
        event.blurb,
        event.link,
      ]),
    ];
    const worksheet = XLSX.utils.aoa_to_sheet(worksheetData);
    XLSX.utils.book_append_sheet(workbook, worksheet, "Events");

    XLSX.writeFile(workbook, "event-details-comprehensive.xlsx");
    console.log(`Event details exported. Total events scraped: ${allEventDetails.length}`);

    await browser.close();
    console.log("Browser closed");
  } catch (error) {
    console.error("Error:", error);
  }
})();
