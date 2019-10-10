async function loadFileTextElement(elementId, fileUrl) {
        let el = document.getElementById(elementId);
        el.innerText = `Loading ${fileUrl}`;

        let res = await fetch(fileUrl);
        let text = await res.text();

        el.innerText = text;
        hljs.highlightBlock(el);
}
