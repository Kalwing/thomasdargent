/*
    Iframe height resizing
*/
function set_demo_height(data) {
	// Set the element identified by data.id to it's inner scrollHeight
	childPayload = JSON.parse(data);
	demo = document.getElementById(childPayload.id);
	demo.style.height = childPayload.height + 10 + 'px';
}

function send_id(demo) {
	// Send their id to each Iframe so they can send data back
	parentPayload = JSON.stringify({ id: demo.id });
	demo.contentWindow.postMessage(parentPayload, 'https://thomasdargent.com');
}

window.addEventListener('message', (event) => {
	if (event.origin !== 'https://thomasdargent.com') {
		return;
	}
	// We got data from the IFrames, we can set their height appropriately
	set_demo_height(event.data);
});

window.addEventListener('load', () => {
	demos = document.getElementsByClassName('demo');
	/*
        - Iframe Communication -
        The process is as follow :
            1. Send their id to the iframe
            2. They send data back with their id so they can be identified
            3. Act on the data
    */
	for (let i = 0; i < demos.length; i++) {
		send_id(demos[i]);
	}
});

/*
    Iframe width dynamic resizing
*/
window.addEventListener('load', () => {
	/*
        Add resizable bar
    */
	demoContainer = document.getElementsByClassName('demo-container');
	for (let i = 0; i < demoContainer.length; i++) {
		let resizer = demoContainer[i].getElementsByClassName('resizer')[0]; // Only one resizer per demo
		if (resizer) {
			og_width = resizer.clientWidth;
			resizer.addEventListener('mousedown', (event) => {
				console.log(event);
				event.target.style.width = '100px'; // Increase the size of the resizer so it overlap over the frame
				window.addEventListener('mousemove', resize);

				window.addEventListener('mouseup', stopResize);
			});
			function resize(e) {
				if (e.target == resizer || e.target.localName == 'section') {
					// position of the mouse - x position of the box
					demoContainer[i].style.width =
						Math.max(e.pageX - demoContainer[i].getBoundingClientRect().left, 128) + 'px';
				}
			}
			function stopResize(event) {
				resizer.style.width = og_width + 'px'; // set the size back
				window.removeEventListener('mousemove', resize);
			}
		}
	}
});
