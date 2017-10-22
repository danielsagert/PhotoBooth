class UI {
    constructor() {
        this.createContainer();
        setInterval(this.fetchPhotos(this.container), 1000);
    }

    static setPhotos(container, filenames) {
        filenames.forEach(function (filename) {
            let img = document.createElement('img');
            img.setAttribute('src', '/photos/' + filename);
            container.appendChild(img);
        });
    }

    createContainer() {
        this.container = document.createElement('div');
        this.container.id = 'photo-container';
        document.querySelector('body').appendChild(self.container);
    }

    fetchPhotos(container) {
        console.log('Fetch photos...');

        fetch('/photos')
            .then(response => response.json())
            .then(json => UI.setPhotos(container, json.filenames));

        console.log('Photos fetched!');
    }
}

new UI();