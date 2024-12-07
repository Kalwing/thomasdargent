const footnote_backs = document.querySelectorAll('.footnote-back');
console.log('aaa', footnote_backs);
for (var i = 0; i < footnote_backs.length; i++) {
	console.log('a', footnote_backs[i]);
	footnote_backs[i].addEventListener('click', process_back);
	footnote_backs[i].addEventListener('enter', process_back);
}

function process_back(evt) {
	const back_to_id = evt.target.href.match(/#.*/)[0];
	const back_to = document.querySelector(back_to_id);
	console.log(back_to);
	const viewportOffset = back_to.getBoundingClientRect();
	const x = viewportOffset.left + window.scrollX;
	const y = viewportOffset.top + window.scrollY;
	const client_height = window.innerHeight;
	console.log(x, y);

	const htop = document.getElementById('highlightTop');
	htop.style.display = 'block';
	htop.style.height = `calc(${y}px - 2rem)`;
	htop.style.opacity = 1;
	const hbot = document.getElementById('highlightBot');
	hbot.style.display = 'block';
	hbot.style.top = `calc(${y}px + 3rem)`;
	hbot.style.opacity = 1;
	hbot.style.bottom = `${document.documentElement.scrollHeight}px`;

	setTimeout(() => {
		window.scrollTo(x, y - client_height / 3);
	}, 50);
	setTimeout(() => {
		htop.style.opacity = 0;
		hbot.style.opacity = 0;
	}, 100);
	setTimeout(() => {
		htop.style.display = 'none';
		hbot.style.display = 'none';
	}, 1000);
}
