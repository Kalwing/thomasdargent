const lightSwitch = document.getElementById('light-switch');
if (localStorage.getItem('dark-mode') === 'true') {
	lightSwitch.checked = true;
}
lightSwitch.addEventListener('change', () => {
	const { checked } = lightSwitch;
	lightSwitch.checked = checked;

	if (lightSwitch.checked) {
		document.documentElement.classList.add('dark');
		localStorage.setItem('dark-mode', true);
	} else {
		document.documentElement.classList.remove('dark');
		localStorage.setItem('dark-mode', false);
	}
});
