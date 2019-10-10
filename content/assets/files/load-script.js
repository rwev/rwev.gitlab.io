nullFunc = () => {}

function loadScript(src, onload, onerror) {
        var script = document.createElement('script');
        script.type = 'text/javascript';
        script.async = true;
        script.src = src;
        script.onload = onload || nullFunc;
        script.onerror = onerror || nullFunc;
        document.getElementsByTagName('head')[0].appendChild(script);
}

function loadStylesheet(src, onload, onerror) {
        var link = document.createElement('link');
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = src;
        link.onload = onload || nullFunc;
        link.onerror = onerror || nullFunc;
        document.getElementsByTagName('head')[0].appendChild(link);
}

function loadScriptPromise(src) {
        return new Promise(function(resolve, reject) {
                loadScript(src, resolve, reject)
        });
}


