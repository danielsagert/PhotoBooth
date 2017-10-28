function update() {
    let container = document.getElementById('photo-container');

    if (!container.hasChildNodes()) {
        console.log("Container is empty");
        loadAllPhotos(container);
        return;
    }

    loadNewPhotos(container);
}

function loadAllPhotos(container) {
    console.log('Load all photos');
    container.innerHTML = '';

    fetch('/photos')
        .then(response => response.json())
        .then((json) => {
            for (const filename of json.filenames) {
                let img = document.createElement('img');
                img.setAttribute('src', '/static/photos/' + filename);
                img.setAttribute('alt', filename);
                container.appendChild(img);
            }

            console.log('All photos loaded');
        });
}

function loadNewPhotos(container) {
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
            loadAllPhotos(container);
        });
}

window.onload = function () {
    update();
    setInterval(update, 3000);
};