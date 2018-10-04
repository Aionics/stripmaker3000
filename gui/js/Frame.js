module.exports = (() => {
    let _Frame = function(base64, name) {
        this.base64 = base64
        this.name = name
        this.dom = new Image
        this.height = 0
        this.width = 0
    }

    _Frame.prototype.load = function() {
        console.log('kek');
        this.dom.onload = () => {
            this.height = this.dom.height
            this.width = this.dom.width
        }
        this.dom.src = `data:image/png;base64,${this.base64}`
    }

    return _Frame
})()
