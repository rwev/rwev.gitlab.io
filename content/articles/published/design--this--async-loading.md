Title: This, Designed: Async Loading
Category: design/this
Tags: code,javascript,ucd
Status: published

One of the principles honored in the development of this site is the conservation of resources, by cutting out the unnecessary and frivolous until only the essential information experience remains. 

An application of this is in the loading of code <code id="script" class="html inline"></code> or styles <code id="link" class="html inline"></code>: they should only be loaded when need is critical and immediate, when the value or functionality they add or extend is directly demanded. 

For example, the resources required for code syntax highlighting are loaded only when the user lands on a page with a code sample: not before, not when they hit site's root, but precisely when they load a page on which syntax highlighting enhances the rendition of code _information_ to the user. 

This is done with the assistance of the following functions: 

<pre><code class="javascript" id="load-script.js"></code></pre>

When a section of code depends on a certain JavaScript dependency in order to execute, it can load the dependency synchronously, in-line with <code id="script" class="javascript inline">await loadScriptPromise(src);</code>. Otherwise, <code id="script" class="javscript inline">loadScript(src, onload, onerror);</code> is asynchronous by default. Synchronous loading of styles isn't provided: styles are applied additively as they are loaded, with order of execution irrelevant.      

See post on [code syntax highlighting](/this-designed-code-syntax-highlighting.html) for usage example.  

<script>

    // html literal broken when written inline - inject as innerText
    document.getElementById("link").innerText = "<link type=\"text/css\" rel=\"stylesheet\">";
    document.getElementById("script").innerText = "<script type=\"text/javascript\"/>";
    
    highlightInlineCode();    
    
    fetchAndHighlightCodeElement(
        {
            elementId: "load-script.js",
            fileUrl: "https://raw.githubusercontent.com/rwev/rwev.gitlab.io/master/content/assets/javascript/load-script.js"
        }
    );
        
</script>


