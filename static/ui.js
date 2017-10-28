function update() {
    let container = document.getElementById('photo-container');

    if (!container.hasChildNodes()) {
        console.log("Container is empty");
        fetchPhotos(container);
        return;
    }

    fetch('/photos/last')
        .then(response => response.json())
        .then((json) => {
            let remoteFilename = json.filename;
            let localFilename = container.firstChild.alt;

            if (localFilename === remoteFilename) {
                console.log("No new file available");
                return;
            }

            console.log('New file available: ' + remoteFilename);
            fetchPhotos(container);
        });
}

function fetchPhotos(container) {
    container.innerHTML = '';

    fetch('/photos')
        .then(response => response.json())
        .then(json => setPhotos(container, json.filenames));
}

function setPhotos(container, filenames) {
    filenames.forEach(function (filename) {
        let img = document.createElement('img');
        img.setAttribute('src', '/static/photos/' + filename);
        img.setAttribute('alt', filename);
        container.appendChild(img);
    });

    console.log('Photos loaded');
}

window.onload = function () {
    update();
    setInterval(update, 3000);
};