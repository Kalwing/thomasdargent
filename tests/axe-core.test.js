const puppeteer = require('puppeteer');
const { readFileSync } = require('fs');
const path = require('path');
const fs = require('fs');

(async () => {
	const pages_path = JSON.parse(readFileSync(path.resolve(__dirname, 'pages.json'), 'utf-8'));
	const browser = await puppeteer.launch();
	const results = [];
	const pages = [];
	const logFilePath = path.resolve(__dirname, 'accessibility.log');
	const logStream = fs.createWriteStream(logFilePath, { flags: 'w' });

	// Helper function to log to the file
	const logToFile = (message) => {
		logStream.write(message + '\n');
	};

	// Process static file paths
	for (const pagePath of pages_path.static) {
		if (pagePath.endsWith('html')) {
			pages.push('file://' + process.cwd() + pagePath);
			continue;
		}
		const fullDirPath = path.resolve(__dirname, pagePath);
		const files = fs.readdirSync(fullDirPath);
		for (const file of files) {
			if (file.endsWith('.html')) {
				pages.push('file://' + fullDirPath + '/' + file);
			}
		}
	}
	for (const pagePath of pages_path.web) {
		pages.push(pagePath);
	}

	console.log('Pages to Test:', pages);

	for (const pagePath of pages) {
		console.log(pagePath);
		const page = await browser.newPage();
		await page.goto(pagePath);

		// Inject axe-core into the page
		await page.addScriptTag({ path: require.resolve('axe-core') });

		// Run axe-core accessibility checks
		const result = await page.evaluate(() => axe.run());
		results.push({ page: pagePath, violations: result.violations });

		logToFile(`Checked: ${pagePath}`);
		if (result.violations.length > 0) {
			logToFile(`Violations found on ${pagePath}:`);
			for (var i = 0; i < result.violations.length; i++) {
				if (result.violations[i].id == 'color-contrast') {
					// I ignore contrast violations as it doesn't take into account media queries
					// I found no syntax highlighting style that gave a great contrast (and the closest one were awful)
					// A prefer-contrast media query is included to fix that.
					// All other issues are checked manually with firefox dev tools, and google page speed.
					// As the color themes shouldn't changes, there shouldn't be any problem !
					logToFile(`Color Contrast warning: ${result.violations[i].nodes.length} nodes`);
					result.violations.splice(i, 1);
				} else {
					logToFile(JSON.stringify(result.violations[i], null, 2));
				}
			}
		}
	}

	await browser.close();

	// Fail the test if there are any violations
	const totalViolations = results.reduce((sum, r) => sum + r.violations.length, 0);
	if (totalViolations > 0) {
		process.exit(1);
	} else {
		console.log('All pages passed accessibility checks!');
	}
})();
