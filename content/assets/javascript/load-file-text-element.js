
FILE_TEXT_CACHE = {};

async function loadHLJS() {
        if (typeof hljs === "undefined") {
                loadStylesheet('/assets/javascript/dependencies/nord-highlightjs.css');
                return loadScriptPromise('/assets/javascript/dependencies/highlight.pack.js');
        }
}


async function highlightCodeElement(elementId) {
        await loadHLJS();
        hljs.highlightBlock(document.getElementById(elementId));
}

async function highlightInlineCode() {
        await loadHLJS();
        document.querySelectorAll('code.inline').forEach((block) => {
                hljs.highlightBlock(block);
        });
}

async function fetchAndHighlightCodeElement({elementId, fileUrl, startLine, endLine, filterPrefix, removeEmptyLines}) {

        removeEmptyLines = (removeEmptyLines === undefined) ? true : removeEmptyLines;

        await loadHLJS();

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

        if (filterPrefix) {
                text = text.split('\n').filter(line => line.search(filterPrefix) !== 0).join('\n');

        }

        if (removeEmptyLines) {
                text = text.split('\n').filter(line => line !== "").join('\n');
        }

        el.innerText = text;
        hljs.highlightBlock(el);

}
