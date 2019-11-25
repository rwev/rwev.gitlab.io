
FILE_TEXT_CACHE = {};

async function loadFileTextElement({elementId, fileUrl, startLine, endLine}) {

    if (typeof hljs === "undefined") {
        loadStylesheet('/assets/javascript/dependencies/nord-highlightjs.css');
        await loadScriptPromise('/assets/javascript/dependencies/highlight.pack.js');
    }

    let el = document.getElementById(elementId);
    el.innerText = `Loading ${fileUrl}`;

    let text = FILE_TEXT_CACHE[fileUrl];

    if (!text) {
        let res = await fetch(fileUrl);
        text = await res.text();
        FILE_TEXT_CACHE[fileUrl] = text;
    }

    if (startLine && endLine) {
        text = text.split('\n').slice(startLine, endLine).join('\n');
    }

    el.innerText = text;
    hljs.highlightBlock(el);

}
