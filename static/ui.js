function update() {
    let container = document.getElementById('photo-container');

    if (!container.hasChildNodes()) {
        console.log("Container is empty");
        loadPhotos(container);
        return;
    }

    loadNewPhotos(container);
}

function loadPhotos(container, lastPhoto) {
    let url;
    if (!lastPhoto) {
        console.log('Load all photos');
        container.innerHTML = '';
        url = 'photos';
    } else {
        console.log('Load all photos until ' + lastPhoto);
        url = 'http://localhost:8000/photos?lastphoto=' + lastPhoto;
    }

    fetch(url)
        .then(response => response.json())
        .then((json) => {
            for (const filename of json.filenames) {
                let img = new Image();
                img.setAttribute('src', 'http://localhost:80/photos/' + filename);
                img.setAttribute('alt', filename);

                if (lastPhoto) {
                    container.insertBefore(img, container.firstChild);
                } else {
                    container.appendChild(img);
                }
            }

            console.log('All photos loaded');
        });
}

function loadNewPhotos(container) {
    fetch('http://localhost:8000/photos/last')
        .then(response => response.json())
        .then((json) => {
            let remoteFilename = json.filename;
            let localFilename = container.firstChild.alt;

            if (localFilename === remoteFilename) {
                console.log("No new file available");
                return;
            }

            loadPhotos(container, localFilename);
        });
}

window.onload = function () {
    update();
    setInterval(update, 3000);
};