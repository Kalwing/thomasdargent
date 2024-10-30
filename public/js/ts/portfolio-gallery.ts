import { createApp, App } from 'vue';
import Portfolio from './components/Portfolio.vue';

if (module.hot) {
	module.hot.accept();
}

// Importing the portfolio project description files
import cardiac_project from '../../portfolio-projects/cardiac';

// Adding the portfolio to the DOM
const project_list = [cardiac_project];
const gallery = document.querySelector('#portfolioGallery');
const app = createApp(Portfolio, { project_list });
app.mount(gallery);

// Preloading images
function preloadImages(imageUrls: string[]) {
	imageUrls.forEach((url) => {
		const img = new Image();
		img.src = url;
	});
}

console.log(cardiac_project[0].image);
const imageUrls: string[] = cardiac_project.map((slide) => slide.image.href);
preloadImages(imageUrls);
