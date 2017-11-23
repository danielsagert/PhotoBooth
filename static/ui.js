const hostname = window.location.hostname;
const urlPhotos = 'http://' + hostname + ':8000/photos';
const lastFilenames = [];

function update() {
    fetch(urlPhotos)
        .then(response => response.json())
        .then((json) => {
            for (let i = json.filenames.length - 1; i >= 0; i--) {
                let filename = json.filenames[i];

                // Check if image was already added
                if (!lastFilenames.includes(filename)) {
                    // Place new image at first position and add DOM element
                    lastFilenames.splice(0, 0, filename);
                    lastFilenames.splice(6);
                    addImage(filename);
                }
            }
        });
}

function addImage(filename) {
    console.log('Add new image: ' + filename);

    let img = new Image();

    img.onload = function () {
        let container = document.getElementById('photo-container');
        container.insertBefore(img, container.firstChild);

        // Only keep 6 images
        while (container.children.length > 6) {
            container.removeChild(container.lastElementChild);
        }
    };

    img.setAttribute('src', urlPhotos + '/' + filename);
    img.setAttribute('alt', filename);
}

window.onload = function () {
    update();
    setInterval(update, 1000);
};