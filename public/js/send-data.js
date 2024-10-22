bodyHeight = document.body.scrollHeight;
data = {
    'height': bodyHeight
}

window.addEventListener(
    "message",
    (event) => {
        if (event.origin !== "http://127.0.0.1:5500") {
            return;
        }
        // Received a message with the id of the IFrame in the parent document
        data["id"] = JSON.parse(event.data).id
        // Send it back with relevant informations
        window.parent.postMessage(JSON.stringify(data), "http://127.0.0.1:5500");
    }
);