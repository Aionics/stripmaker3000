
const remote = require('electron').remote
const mainWindow = remote.getGlobal('mainWindow')
const dialog = remote.dialog
const test = () => {
    dialog.showOpenDialog(
        mainWindow,
        {
            title: "select an a file(gif) or a files(png, jpg)",
            filters: [{name: 'Images', extensions: ['jpg', 'png', 'gif']}],
            properties: ["multiSelections"]
        },
        (filePaths) => {
            console.log(filePaths);
        }
    )
}

document.addEventListener("DOMContentLoaded", function (event) {
    document.addEventListener("keydown", function (e) {
        if (e.which === 123) {
            try {
                remote.getCurrentWindow().toggleDevTools();
            } catch (e) {
                console.error(e);
            }
        } else if (e.which === 116) {
            location.reload();
        }
    });
    document.querySelector('#test').addEventListener('click', test)
    // M.toast({html: 'I am a toast!', classes: 'toast_errored'});
});
