const URL_PHOTOS = 'http://' + window.location.hostname + ':8000/photos';

function update() {
    fetch(URL_PHOTOS)
        .then(response => response.json())
        .then((json) => {
            for (let i = 0; i < json.filenames.length; i++) {
                addImage(json.filenames[i]);
            }
        });
}

function addImage(filename) {
    let img = new Image();
    img.setAttribute('alt', filename);
    img.setAttribute('src', URL_PHOTOS + '/' + filename);

    let link = document.createElement('a');
    link.setAttribute('href', img.src);
    link.appendChild(img);

    let container = document.getElementById('photo-container');
    container.appendChild(link);
}

window.onload = function () {
    update();
};