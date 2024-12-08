document.addEventListener('DOMContentLoaded', () => {
	const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion)').matches;

	const footnote_backs = document.querySelectorAll('.footnote-back');
	for (var i = 0; i < footnote_backs.length; i++) {
		footnote_backs[i].addEventListener('click', process_back);
		footnote_backs[i].addEventListener('enter', process_back);
	}

	// Hide all footnote marker
	const footnotes = document.querySelectorAll('.footnote');
	for (var i = 0; i < footnotes.length; i++) {
		footnotes[i].classList.add('before:hidden');
	}
	function reset_footnotes() {
		for (var i = 0; i < footnote_refs.length; i++) {
			footnotes[i].classList.add('before:hidden');
		}
	}

	// Handle the link from the footnote to the text
	// Scroll so that the ref is visible and highlight it
	function process_back(evt) {
		reset_footnotes();
		const back_to_id = evt.target.href.match(/#.*/)[0];
		const back_to = document.querySelector(back_to_id);

		const viewportOffset = back_to.getBoundingClientRect();
		const x = viewportOffset.left + window.scrollX;
		const y = viewportOffset.top + window.scrollY;
		const client_height = window.innerHeight;

		if (!prefersReducedMotion) {
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
	}

	const footnote_refs = document.querySelectorAll('.footnote-ref');
	for (var i = 0; i < footnote_refs.length; i++) {
		footnote_refs[i].addEventListener('click', process_ref);
		footnote_refs[i].addEventListener('enter', process_ref);
	}
	// Handle going from the text to the footnote
	// Display a marker on the footnote that was selected
	function process_ref(evt) {
		if (evt.target.nodeName == 'SUP') {
			// sup are included in span
			target = evt.target.parentNode.parentNode;
		} else if (evt.target.nodeName == 'SPAN') {
			// span are in a 'a'
			target = evt.target.parentNode;
		} else {
			// since the element was activated the parent must be the 'a'
			target = evt.target;
		}

		const sent_to_id = target.href.match(/#.*/)[0];
		const sent_to = document.querySelector(sent_to_id);

		reset_footnotes();
		sent_to.classList.remove('before:hidden');
	}
});
