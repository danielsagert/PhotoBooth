class UI {
    constructor() {
        this.createContainer();

        let self = this;
        setInterval(() => {
            self.updateContainer();
        }, 3000);
    }

    static setPhotos(filenames) {
        let container = document.getElementById('photo-container');

        filenames.forEach(function (filename) {
            let img = document.createElement('img');
            img.setAttribute('src', '/photos/' + filename);
            img.setAttribute('alt', filename);
            container.appendChild(img);
        });
    }

    createContainer() {
        this.container = document.createElement('div');
        this.container.id = 'photo-container';
        document.querySelector('body').appendChild(this.container);
    }

    updateContainer() {
        let remoteFilename = this.getLastFilename();
        let localFilename = this.container.firstChild.alt;

        if (localFilename === remoteFilename) {
            console.log('Not new file available');
        } else {
            console.log('New file available');
        }
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