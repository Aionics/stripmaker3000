const { app, BrowserWindow } = require('electron')
function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        resizable: false
    })
    mainWindow.setMenu(null)
    mainWindow.loadFile('gui/index.html')

    mainWindow.on('closed', function () {
        mainWindow = null
    })
    global.mainWindow = mainWindow
}
app.on('ready', createWindow)
app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

// MAC OS reactivate
app.on('activate', function () {
    if (mainWindow === null) {
        createWindow()
    }
})
