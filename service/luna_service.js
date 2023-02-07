
let ls2;
let handle;

// initialize

function initialize(service) {
    ls2 = service;
}


// set func

function createtoast(msg) {
    let params = {
        message: msg,
        persistent: true
    };
    let callback = (m) => { console.log(msg); }
    ls2.call("luna://com.webos.notification/createToast", params, callback);
}

function cameraOpen() {
    return new Promise((resolve, reject) => {
        ls2.call("luna://com.webos.service.camera2/open", { "id": "camera1" }, (msg) => {
            if (msg.payload.returnValue) {
                resolve(msg.payload.handle);
            } else {
                console.log("error - <cameraOpen>");
                reject("cameraOpen " + JSON.stringify(msg.payload));
            }
        });
    });
}

function cameraFormat() {
    return new Promise((resolve, reject) => {
        ls2.call("luna://com.webos.service.camera2/setFormat", {
            "handle": handle,
            "params": {
                "width": 370,
                "height": 366,
                "format": "JPEG",
                "fps": 30
            }
        }, (msg) => {
            if (msg.payload.returnValue) {
                resolve(JSON.stringify(msg.payload.returnValue));
            }
            else {
                console.log("error - <cameraFormat>")
                reject("CameraFormat " + JSON.stringify(msg.payload))
            }
        })
    });
}

function cameraPreviewStart() {
    return new Promise((resolve, reject) => {
        ls2.call("luna://com.webos.service.camera2/startPreview", {
            "handle": handle,
            "params": {
                "type": "sharedmemory",
                "source": "0"
            }
        }, (msg) => {
            if (msg.payload.returnValue) {
                resolve(JSON.stringify(msg.payload.key));
            }
            else {
                console.log("error - <cameraPreviewStart>")
                reject("camerPreviewStart " + JSON.stringify(msg.payload))
            }
        })
    });
}

function startCapture() {
    console.log("__in startCapture()__");
    return new Promise((resolve, reject) => {
        console.log("__int startCapture()__.promise()");
        ls2.call("luna://com.webos.service.camera2/startCapture", {
            "handle": handle,
            "params": {
                "width": 370,
                "height": 366,
                "format": "JPEG",
                "mode": "MODE_CONTINUOUS"
            }
        }, (msg) => {
            console.log("__int startCapture(), call__");
            if (msg.payload.returnValue) {
                resolve(msg.payload.returnValue);
            }
            else {
                console.log("error - <startCapture>")
                reject("startCapture " + JSON.stringify(msg.payload))
            }
        })
    });
}

function stopCapture() {
    return new Promise((resolve, reject) => {
        ls2.call("luna://com.webos.service.camera2/stopCapture", {
            "handle": handle
        }, (msg) => {
            if (msg.payload.returnValue) {
                resolve(JSON.stringify(msg.payload.key));
            }
            else {
                console.log("error - <stopcap>")
                reject("[stop Capture] " + JSON.stringify(msg.payload))
            }
        })
    });
}

async function set_camera() {
    let open = await cameraOpen().then((result) => { handle = result }).catch((error) => { console.log(error) });
    let format = await cameraFormat(handle).then((result) => { check = result }).catch((error) => { console.log(error) });
    let privew = await cameraPreviewStart(handle).then((result) => { key = result }).catch((error) => { console.log(error) });
}

// end set func


// set exports

module.exports.initialize = initialize;
module.exports.createtoast = createtoast;
module.exports.set_camera = set_camera;
module.exports.startCapture = startCapture;
module.exports.stopCapture = stopCapture;

// end set exports