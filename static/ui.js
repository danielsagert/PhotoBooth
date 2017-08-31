class UI {
    constructor() {
        this.createContainer();
        this.fetchPhotos();
    }

    static setPhotos(container, filenames) {
        filenames.forEach(function (filename) {
            let img = document.createElement('photo-booth-image');
            img.setAttribute('filename', filename);

            container.appendChild(img);
        });
    }

    createContainer() {
        this.container = document.createElement('div');
        this.container.id = 'photo-container';
        document.querySelector('body').appendChild(this.container);
    }

    fetchPhotos() {
        fetch('/photos')
            .then(response => response.json())
            .then(json => UI.setPhotos(this.container, json.filenames));
    }
}

new UI();