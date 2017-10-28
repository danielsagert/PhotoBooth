function createContainer() {
    let container = document.createElement('div');
    container.id = 'photo-container';
    document.querySelector('body').appendChild(container);
    return container;
}

function getContainer() {
    let container = document.document.getElementById('photo-container');

    if (container) {
        return container;
    }

    return createContainer();
}

function update() {
    let container = getContainer();

    if (!container.hasChildNodes()) {
        console.log("Container is empty");
        this.fetchPhotos();
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
            this.fetchPhotos(container);
        });
}

function fetchPhotos(container) {
    container.innerHTML = '';

    fetch('/photos')
        .then(response => response.json())
        .then(json => this.setPhotos(container, json.filenames));
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

setInterval(function () {
    update()
}, 3000);