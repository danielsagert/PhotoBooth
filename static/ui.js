class UI {
    constructor() {
        this.container = document.createElement('div');
        this.container.id = 'photo-container';
        document.querySelector('body').appendChild(this.container);
    }

    setPhotos(self, filenames) {
        filenames.forEach(function (filename) {
            let img = document.createElement('img');
            img.setAttribute('src', '/photos/' + filename);
            img.setAttribute('alt', filename);
            self.container.appendChild(img);
        });

        console.log('Photos loaded');
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

                if (localFilename === remoteFilename) {
                    console.log("No new file available");
                    return;
                }

                console.log('New file available: ' + remoteFilename);
                this.fetchPhotos();
            });
    }

    fetchPhotos() {
        this.container.innerHTML = '';

        fetch('/photos')
            .then(response => response.json())
            .then(json => this.setPhotos(this, json.filenames));
    }
}

let ui = new UI();

setInterval(() => {
    ui.update();
}, 3000);