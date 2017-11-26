const URL_PHOTOS = 'http://' + window.location.hostname + ':8000/photos';
const URL_THUMBNAILS = URL_PHOTOS + 'thumbnail';

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
    img.setAttribute('src', URL_THUMBNAILS + '/' + filename);

    let link = document.createElement('a');
    link.setAttribute('href', URL_PHOTOS + '/' + filename);
    link.appendChild(img);

    let main = document.querySelector('main');
    main.appendChild(link);
}

window.onload = function () {
    update();
};