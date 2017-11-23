const URL_PHOTOS = 'http://' + window.location.hostname + ':8000/photos';
const MAX_IMAGES = 6;
const LAST_FILENAMES = [];

function update() {
    let url = URL_PHOTOS + '?limit=' + MAX_IMAGES;

    fetch(url)
        .then(response => response.json())
        .then((json) => {
            for (let i = json.filenames.length - 1; i >= 0; i--) {
                let filename = json.filenames[i];

                // Check if image was already added
                if (!LAST_FILENAMES.includes(filename)) {
                    // Place new image at first position and add DOM element
                    LAST_FILENAMES.splice(0, 0, filename);
                    LAST_FILENAMES.splice(MAX_IMAGES);
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
        container.insertBefore(this, container.firstChild);

        // Only keep x images
        while (container.children.length > MAX_IMAGES) {
            container.removeChild(container.lastElementChild);
        }
    };

    img.setAttribute('alt', filename);
    img.setAttribute('src', URL_PHOTOS + '/' + filename);
}

window.onload = function () {
    update();
    setInterval(update, 1000);
};