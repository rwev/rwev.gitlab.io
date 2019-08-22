function loadScript(src, onLoad) {
        var script = document.createElement('script'); 
        script.type = 'text/javascript';
        script.async = true;
        script.src = src;
        script.onload = onLoad
        var s = document.getElementsByTagName('script')[0]; 
        s.parentElement.insertBefore(script, s);
}

function loadStylesheet(src, onLoad) {
        var link = document.createElement('link');
        link.rel = 'stylesheet';
        link.type = 'text/css';
        link.href = src;
        var l = document.getElementsByTagName('link')[0]; 
        l.parentElement.insertBefore(link, l);
}
