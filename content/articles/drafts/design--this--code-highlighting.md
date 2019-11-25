Title: This, Designed: Code Syntax Highlighting
Category: design/this
Tags: js,ui,nord

In the integration of select code samples into this site, I had a couple of requirements:

- source code samples should not be held internally. No duplication - source should be checked into exactly one repository
- scripts and styles required for highlighting should only be loaded on-demand, for preservation of resources on both the server and client side. 

I decided on _[highlight.js](https://highlightjs.org/)_ due to its simplicity and also the availability of a _[nord](https://github.com/arcticicestudio/nord-highlightjs)_ic theme. 

In order to fulfill the above requirements, I settled on a simple helper function that loads _highlight.js_ scripts and styles when highlighting is called for. Additionally, the function fetches the source code from the specified remote resource, caches the result, and optionally trims it down to a specified line range. 

All in, here's what the function looks like:

loadFileTextElement(
    {
        elementId: "config.vim",
        fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.vim/config.vim"
    }
 );


