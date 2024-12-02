import { createApp, App } from 'vue';
import Portfolio from './components/Portfolio.vue';

// Importing the portfolio project description files
import cardiac_project from '../../portfolio-projects/cardiac';
import coordconv_project from '../../portfolio-projects/coordconv';

// Adding the portfolio to the DOM
const project_list = [cardiac_project, coordconv_project];
const gallery = document.getElementById('portfolioGallery');
const app = createApp(Portfolio, { project_list });
app.mount(gallery);

// Preloading images
function preloadImages(imageUrls: string[]) {
	imageUrls.forEach((url) => {
		const img = new Image();
		img.src = url;
	});
}

const imageUrls: string[] = cardiac_project.map((slide) => slide.image.href);
preloadImages(imageUrls);
