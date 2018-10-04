const FrameList = (() => {
    let _FrameList = function () {
        this.frames = []
        ko.track(this)
    }

    _FrameList.prototype.add = function (frame) {
        this.frames.push(frame)
    }
    _FrameList.prototype.loadImages = function () {
        for (frame of this.frames) {
            frame.load()
        }
        setTimeout(()=>{stripmaker.selected_frame = this.frames[0]}, 100)
    }
    _FrameList.prototype.refresh = function () {
        let array = this.frames.slice(0);
        this.frames = [];
        this.frames = array;
    }
    _FrameList.prototype.moveFrame = function (direction) {
        let current_id = this.frames.indexOf(stripmaker.selected_frame)
        let next_id = current_id + direction
        if (next_id == this.frames.length) { next_id = 0 }
        if (next_id == -1) { next_id = this.frames.length - 1 }
        let shifted_frame = this.frames[next_id]
        this.frames[current_id] = shifted_frame
        this.frames[next_id] = stripmaker.selected_frame
        this.refresh()
    }
    _FrameList.prototype.selectNext = function () {
        let current_id = this.frames.indexOf(stripmaker.selected_frame)
        let next_id = current_id + 1
        if (next_id == this.frames.length) { next_id = 0 }
        stripmaker.selected_frame = this.frames[next_id]
        this.refresh()
    }

    return _FrameList
})()

module.exports = () => {
    return new FrameList()
}
