const pa11y = require('pa11y');
const { readFileSync } = require('fs');
const path = require('path');
const fs = require('fs');
const { assert } = require('console');

(async () => {
	const pages_path = JSON.parse(readFileSync(path.resolve(__dirname, 'pages.json'), 'utf-8'));
	const results = [];
	const pages = [];
	const logFilePath = path.resolve(__dirname, 'pa11y.accessibility.log');
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
		const result = await pa11y(pagePath);

		logToFile(`Checked: ${pagePath}`);
		const to_delete = [];
		if (result.issues.length > 0) {
			logToFile(`Violations found on ${pagePath}:`);
			const n_issues = result.issues.length;
			const filteredIssues = result.issues.filter((issue) => {
				if (issue.code === 'WCAG2AA.Principle1.Guideline1_4.1_4_3.G18.Fail') {
					logToFile('-> Contrast issues');
					return false; // Exclude contrast issue, see axe-core.test.js for the reasonning
				} else {
					logToFile(`${issue.type}: ${issue.message}\n --> at ${issue.context} (${issue.code})`);
					return true; // Include all other issues
				}
			});
			console.log(n_issues, filteredIssues.length);

			results.push({ page: pagePath, issues: filteredIssues });
		} else {
			results.push({ page: pagePath, issues: result.issues });
		}
	}

	// Fail the test if there are any issues
	const totalIssues = results.reduce((sum, r) => sum + r.issues.length, 0);
	if (totalIssues > 0) {
		console.log(`${totalIssues} errors.`);
		process.exit(1);
	} else {
		console.log('All pages passed accessibility checks!');
	}
})();
