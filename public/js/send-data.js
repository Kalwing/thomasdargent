bodyHeight = document.body.scrollHeight;
data = {
	height: bodyHeight,
};

window.addEventListener('message', (event) => {
	if (event.origin !== 'https://thomasdargent.com') {
		return;
	}
	// Received a message with the id of the IFrame in the parent document
	data['id'] = JSON.parse(event.data).id;
	// Send it back with relevant informations
	window.parent.postMessage(JSON.stringify(data), 'https://thomasdargent.com');
});
