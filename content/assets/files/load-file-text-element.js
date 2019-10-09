
async function loadFileTextElement(elementId, fileUrl) {

        responseText = await fetch(fileUrl).then(res => res.text());

        // start/end line count? sections only?
        document.getElementById(elementId).innerText = responseText;
}
