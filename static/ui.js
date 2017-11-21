const hostname = window.location.hostname;
const urlFlask = 'http://' + hostname + ':8000';
const urlApache = 'http://' + hostname + ':80';
const lastFilenames = [];

function loadPhotos() {
    let container = document.getElementById('photo-container');
    let url = urlFlask + '/photos';

    fetch(url)
        .then(response => response.json())
        .then((json) => {
            for (let i = json.filenames.length - 1; i >= 0; i--) {
                let filename = json.filenames[i];

                if (!lastFilenames.includes(filename)) {
                    lastFilenames.splice(0, 0, filename);
                    lastFilenames.splice(6);
                    console.log('Last filenames: ' + lastFilenames);

                    addImage(container, filename);
                }
            }
        });
}

function addImage(container, filename) {
    console.log('Add new image to container:' + filename);

    let img = new Image();
    img.setAttribute('src', urlApache + '/photos/' + filename);
    img.setAttribute('alt', filename);

    // img.onload = function () {
    container.insertBefore(img, container.firstChild);

    while (container.children.length > 6) {
        container.removeChild(container.lastElementChild);
    }
    // };
}

window.onload = function () {
    loadPhotos();
    setInterval(loadPhotos, 1000);
};