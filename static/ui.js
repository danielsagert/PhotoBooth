class UI {
    constructor() {
        this.createContainer();

        let self = this;
        setInterval(() => {
            self.update();
        }, 3000);
    }

    setPhotos(filenames) {
        filenames.forEach(function (filename) {
            let img = document.createElement('img');
            img.setAttribute('src', '/photos/' + filename);
            img.setAttribute('alt', filename);
            this.container.appendChild(img);
        });
    }

    createContainer() {
        this.container = document.createElement('div');
        this.container.id = 'photo-container';
        document.querySelector('body').appendChild(this.container);
    }

    update() {
        if (!this.container.hasChildNodes()) {
            console.log("Container is empty");
            this.fetchPhotos();
            return;
        }

        fetch('/photos/last')
            .then(response => response.json())
            .then((json) => {
                let remoteFilename = json.filename;
                let localFilename = this.container.firstChild.alt;

                console.log('Local filename: ' + remoteFilename + ', remote filename: ' + remoteFilename);

                if (localFilename === remoteFilename) {
                    return;
                }

                console.log('New file available');
                this.fetchPhotos();
            });
    }

    fetchPhotos() {
        this.container.innerHTML = '';

        fetch('/photos')
            .then(response => response.json())
            .then(json => this.setPhotos(json.filenames));

        console.log('Photos fetched!');
    }
}

new UI();