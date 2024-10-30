import { createApp, App } from 'vue';
import DemoResult from './components/JsCodeBlock.vue';

if (module.hot) {
	module.hot.accept();
}
const demoElements = document.querySelectorAll('.vue-demo');
demoElements.forEach((el) => {
	const code = el.innerHTML.trim();
	// const f = new Function(code);
	var result = {};
	// try {
	// 	result = { value: f(), state: 'text-pacific-blue-600' };
	// } catch (e) {
	// 	result = { value: e, state: 'text-pink-600' };
	// }
	// Create and mount the Vue component, passing 'code' as a prop
	const app = createApp(DemoResult, { code });
	app.mount(el);
});
