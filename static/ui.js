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
                    addImage(container, filename);
                }
            }
        });
}

function addImage(container, filename) {
    console.log('Add new image to container:' + filename);

    let img = new Image();

    img.onload = function () {
        container.insertBefore(img, container.firstChild);

        while (container.children.length > 6) {
            container.removeChild(container.lastElementChild);
        }
    };

    img.setAttribute('src', urlApache + '/photos/' + filename);
    img.setAttribute('alt', filename);
}

window.onload = function () {
    loadPhotos();
    setInterval(loadPhotos, 2000);
};
//
//
// function update() {
//     let container = document.getElementById('photo-container');
//
//     if (!container.hasChildNodes()) {
//         console.log("Container is empty");
//         loadPhotos(container);
//         return;
//     }
//
//     loadNewPhotos(container);
// }
//
// function loadPhotos(container, lastPhoto) {
//     let url;
//     if (!lastPhoto) {
//         console.log('Load all photos');
//         container.innerHTML = '';
//         url = 'photos';
//     } else {
//         console.log('Load all photos until ' + lastPhoto);
//         url = urlFlask + '/photos?lastphoto=' + lastPhoto;
//     }
//
//     fetch(url)
//         .then(response => response.json())
//         .then((json) => {
//             for (const filename of json.filenames) {
//                 let img = new Image();
//
//                 img.onload = function () {
//                     if (lastPhoto) {
//                         container.insertBefore(img, container.firstChild);
//                     } else {
//                         container.appendChild(img);
//                     }
//
//                     while (container.children.length > 6) {
//                         container.removeChild(container.lastElementChild);
//                     }
//                 };
//
//                 img.setAttribute('src', urlApache + '/photos/' + filename);
//                 img.setAttribute('alt', filename);
//             }
//
//             console.log('All photos loaded');
//         });
// }
//
// function loadNewPhotos(container) {
//     fetch(urlFlask + '/photos/last')
//         .then(response => response.json())
//         .then((json) => {
//             let remoteFilename = json.filename;
//             let localFilename = container.firstChild.alt;
//
//             if (localFilename === remoteFilename) {
//                 console.log("No new file available");
//                 return;
//             }
//
//             loadPhotos(container, localFilename);
//         });
// }
//
// window.onload = function () {
//     update();
//     setInterval(update, 1000);
// };