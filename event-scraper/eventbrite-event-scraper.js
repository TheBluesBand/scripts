const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  const url =
    "https://www.eventbrite.com.au/d/australia--wollongong/startup/?page=1";

  await page.goto(url, { waitUntil: "domcontentloaded" });
  console.log("Page rendered.");

  const organizerUrls = await page.evaluate(() => {
    const organizers = [];
    const eventCardList = document.querySelectorAll(
      "div.SearchResultPanelContentEventCardList-module__map_experiment_event_card___vyRC3"
    );
    eventCardList.forEach((card) => {
      const organizerElement = card.querySelector(
        'div.Stack_root__1ksk7[style="--Space:4px"] a'
      );
      console.log("Organizer Element:", organizerElement);
      if (organizerElement) {
        const organizerUrl = organizerElement.href;
        organizers.push(organizerUrl);
        console.log("Organizer URL grabbed:", organizerUrl);
      }
    });
    return organizers;
  });

  const organizerProfileUrls = [];

  for (const organizerUrl of organizerUrls) {
    console.log(`Visiting organizer URL: ${organizerUrl}`);
    await page.goto(organizerUrl, { waitUntil: "domcontentloaded" });

    const profileUrl = await page.evaluate(() => {
      const profileElement = document.querySelector(
        'div.descriptive-organizer-info-mobile__name[data-testid="organizer-name"] a'
      );
      return profileElement ? profileElement.href : null;
    });

    if (profileUrl) {
      organizerProfileUrls.push(profileUrl);
      console.log("Organizer profile URL grabbed:", profileUrl);
    }
  }

  console.log("All Organizer Profile URLs:", organizerProfileUrls);

  const pastEventUrls = [];

  for (const profileUrl of organizerProfileUrls) {
    console.log(`Visiting organizer profile URL: ${profileUrl}`);
    await page.goto(profileUrl, { waitUntil: "domcontentloaded" });

    // Click the button that contains the text "Past"
    await page.evaluate(() => {
      const buttons = Array.from(
        document.querySelectorAll(
          "section.organizer-events__event-controls button"
        )
      );
      const pastButton = buttons.find((button) =>
        button.textContent.includes("Past")
      );
      if (pastButton) {
        pastButton.click();
        console.log("Clicked the Past button.");
      }
    });

    // Wait for the past events to load
    await page.waitForSelector("section.organizer-events__event-controls");

    // Extract all <a> href attributes
    const eventUrls = await page.evaluate(() => {
      const links = document.querySelectorAll("a.event-card-link");
      return Array.from(links).map((link) => link.href);
    });

    pastEventUrls.push(...eventUrls);
  }

  console.log("All Past Event URLs:", pastEventUrls);

  await browser.close();
})();
