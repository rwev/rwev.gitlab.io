
FILE_TEXT_CACHE = {};

async function loadFileTextElement({elementId, fileUrl, startLine, endLine}) {

    if (hljs === undefined) {
        await loadScript('/assets/javascript/dependencies/highlight.pack.js');
        await loadStylesheet('/assets/javascript/dependencies/nord-highlightjs.css');
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
