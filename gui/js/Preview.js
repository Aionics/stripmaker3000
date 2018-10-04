const Preview = (() => {
    let _Preview = function (params) {
        this.width = params.widhth || 580
        this.height = params.height || 500
        this.selected_frame = null
        this.scale = 1
        this.fps = ko.observable(6)
        this.timerId = null
        this.timer = () => {
            if (this.animated && this.fps) {
                stripmaker.frame_list.selectNext()
                this.timerId = setTimeout(this.timer, 1000 / this.fps)
            } else {
                this.animated = false
            }
        }
        this.animated = ko.observable(false)
        this.animated.subscribe((new_value) => {
            if (new_value) {
                this.timer()
            } else {
                clearTimeout(this.timerId);
            }
        })
        this.fps.subscribe((new_val) => {
            if (new_val>99) {
                this.fps = 6
            };
        })

        ko.track(this)
    }

    _Preview.prototype.zoom = function (direction) {
        this.scale = direction ? this.scale + 0.2 : Math.max(this.scale - 0.2, 0.2)
    }

    return _Preview
})()

module.exports = (params) => {
    return new Preview(params)
}
