class UI {
    constructor() {
        this.createContainer();

        let self = this;
        setInterval(() => {
            self.getLastFilename();
        }, 3000);
    }

    static setPhotos(filenames) {
        let container = document.getElementById('photo-container');

        filenames.forEach(function (filename) {
            let img = document.createElement('img');
            img.setAttribute('src', '/photos/' + filename);
            container.appendChild(img);
        });
    }

    createContainer() {
        let container = document.createElement('div');
        container.id = 'photo-container';
        document.querySelector('body').appendChild(container);
    }

    getLastFilename() {
        fetch('/photos/last')
            .then(response => response.json())
            .then((json) => {
                let filename = json.filename;
                console.log('Latest filename: ' + filename);
                return filename;
            });
    }

    fetchPhotos() {
        fetch('/photos')
            .then(response => response.json())
            .then(json => UI.setPhotos(json.filenames));

        console.log('Photos fetched!');
    }
}

new UI();