const btn = document.getElementById('show-btn');
const menu = document.getElementById('menu');

btn.onclick = () => {
	if (menu.classList.contains('hidden')) {
		menu.classList.replace('hidden', 'block');
		btn.classList.remove('rotate-1');
		btn.classList.add('-rotate-1');
		btn.innerHTML = '↥';
	} else {
		menu.classList.replace('block', 'hidden');
		btn.innerHTML = '↧';
		btn.classList.remove('-rotate-1');
		btn.classList.add('rotate-1');
	}
};
