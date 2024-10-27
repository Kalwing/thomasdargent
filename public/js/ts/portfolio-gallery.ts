import { createApp, App } from 'vue';
import Portfolio from './components/Portfolio.vue';

if (module.hot) {
	module.hot.accept();
}

// Importing the portfolio project description files
import cardiac_project from '../../portfolio-projects/cardiac';

const project_list = [cardiac_project];
const gallery = document.querySelector('#portfolioGallery');
const app = createApp(Portfolio, { project_list });
app.mount(gallery);
