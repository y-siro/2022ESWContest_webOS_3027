
const pkgInfo = require('./package.json');
const Service = require('webos-service');
const luna = require("./luna_service");
const service = new Service(pkgInfo.name);

// register service

service.register("setService", function(message) {
    luna.initialize(service);    
    luna.createtoast("Mode Changed!");
    luna.set_camera();
});

service.register("startScreenshot", function(message){
    luna.createtoast("3초 후 카메라를 향해 수어를 인식해주세요.");
    luna.startCapture();
})

service.register("stopScreenshot", function(message){
    luna.createtoast("수어 인식이 종료되었습니다.");
    luna.stopCapture();

    // send code (ex.python or socket) pysftp
})