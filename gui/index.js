const remote = require('electron').remote
// remote.getCurrentWindow().toggleDevTools();
const mainWindow = remote.getGlobal('mainWindow')
const dialog = remote.dialog
const path = require('path')
const fs = require('fs')
const async = require('async')
const gifFrames = require('gif-frames');
const streamToBuffer = require('stream-to-buffer')
// const Canvas = require('canvas')
// const Canvas_Image = Canvas.Image

const config = require('./config')
const Frame = require('./js/Frame')

let stripmaker = {
    frame_list: require('./js/Framelist')(),
    preview: require('./js/Preview')(config.preview_config),
    selected_frame: null
}
ko.track(stripmaker)

const readImageSync = (path) => {
    let bitmap = fs.readFileSync(path);
    return new Buffer(bitmap).toString('base64');
}

const openFile = () => {
    dialog.showOpenDialog(
        mainWindow, {
            title: "select an a file(gif) or a files(png, jpg)",
            filters: [{ name: 'Images', extensions: ['jpg', 'png', 'gif'] }],
            properties: ["multiSelections"]
        },
        (file_paths) => {
            stripmaker.selected_frame = null
            stripmaker.frame_list.frames = []
            async.waterfall(file_paths.map((file_path) => {
                return function (done) {
                    console.log(file_path);
                    let name = path.basename(file_path)
                    switch (path.extname(file_path)) {
                        case '.gif':
                            gifFrames({
                                url: file_path,
                                frames: 'all',
                                outputType: 'png',
                                cumulative: true
                            }, (err, gifFrameData) => {
                                if (err) {
                                    return console.error(err);
                                }
                                async.waterfall(gifFrameData.map((gifFrame, gifIndex) => {
                                    return function (gif_done) {
                                        streamToBuffer(gifFrame.getImage(), (err, buffer) => {
                                            if (err) {
                                                return gif_done(err)
                                            }
                                            let new_frame = new Frame(
                                                new Buffer(buffer, 'binary').toString('base64'),
                                                `${gifIndex}_${name}`
                                            )
                                            stripmaker.frame_list.add(new_frame)
                                            gif_done(null)
                                        })
                                    }
                                }), done)
                            })
                            break;
                        case '.png':
                        case '.jpg':
                            try {
                                let new_frame = new Frame(readImageSync(file_path), name)
                                stripmaker.frame_list.add(new_frame)
                            } catch (e) {
                                if (e) {
                                    return done(e)
                                }
                            }
                            done(null)
                            break;
                    }
                }
            }), (err, res) => {
                console.log("DONE");
                if (err) {
                    return console.error(err);
                }
                stripmaker.frame_list.loadImages()
            })
        }
    )
}

ko.bindingHandlers.canvas = {
    update: (dom, valueAccessor, allBindings, previewModel) => {
        let frame = ko.unwrap(valueAccessor());
        if (frame) {
            let frame_size = [
                frame.width * previewModel.scale,
                frame.height * previewModel.scale
            ]
            let canvas_center = [
                Math.floor(previewModel.width / 2),
                Math.floor(previewModel.height / 2)
            ]
            let image_origin = [
                canvas_center[0] - Math.floor(frame_size[0] / 2),
                canvas_center[1] - Math.floor(frame_size[1] / 2)
            ]
            let canvas_context = dom.getContext("2d")
            canvas_context.clearRect(0, 0, previewModel.width, previewModel.height);
            canvas_context.drawImage(
                frame.dom,
                image_origin[0],
                image_origin[1],
                frame_size[0],
                frame_size[1]
            )
        }
    }
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
    document.querySelector('#open_file').addEventListener('click', openFile)
    ko.applyBindings(stripmaker)
    // M.toast({html: 'I am a toast!', classes: 'toast_errored'});
});
