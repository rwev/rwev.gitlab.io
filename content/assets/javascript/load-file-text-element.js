
FILE_TEXT_CACHE = {};

if (typeof(String.prototype.trim) === "undefined") {
        String.prototype.trim = function() {
                        return String(this).replace(/^\s+|\s+$/g, '');
        };
}

async function loadHLJS() {
        if (typeof hljs === "undefined") {
                loadStylesheet('/assets/javascript/dependencies/nord-highlightjs.css');
                return loadScriptPromise('/assets/javascript/dependencies/highlight.pack.js');
        }
}

async function loadAsciinema() {
        if (typeof asciinema === "undefined") {
                loadStylesheet('/assets/javascript/dependencies/asciinema-player.css');
                loadStylesheet('/assets/javascript/dependencies/asciinema-theme-nord.css');
                return loadScriptPromise('/assets/javascript/dependencies/asciinema-player.js');
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
                text = text.split('\n').filter(line => line.trim().search(filterPrefix) !== 0).join('\n');

        }

        if (removeEmptyLines) {
                text = text.split('\n').filter(line => line.trim() !== "").join('\n');
        }

        el.innerText = text;
        hljs.highlightBlock(el);

}

async function fetchAsciinema({divId, castFile, startTime}) {
        
        await loadAsciinema();
        
        let castPath = `/assets/javascript/dependencies/asciicasts/${castFile}`;

        let preload = ``; // false
        let loop= ``; 
        let autoplay = ``;

        let posterStr = ``;
        
        if (startTime) {
                posterStr = `poster="npt:${startTime}"`;
        }

        let elementStr = `<asciinema-player src="${castPath}" ${autoplay} ${preload} ${loop} ${posterStr} speed="${1.25}" theme="${`nord`}" font-size="${`12px`}" cols="125"></asciinema-player>`;

        document.getElementById(divId).innerHTML = elementStr;

}
