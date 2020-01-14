Title: This, Designed: Code Syntax Highlighting
Category: design/this
Tags: javascript,ui,ucd,nord,code
Status: published

In the integration of select code samples into this site, I had a couple of requirements:

1. Source code should be fetched from an external source. Code samples should not be held internally. No duplication - source should be checked into exactly one repository.
2. Scripts and styles required for highlighting should only be loaded on-demand, for preservation of resources on both the server and client side.
3. Code highlighting should happen locally, not globally (i.e. on an element instead of document level) to allow for the above in the case of multiple different samples on the same page. 

I decided on [highlight.js](https://highlightjs.org/) due to its simplicity and also the availability of a [nordic](https://github.com/arcticicestudio/nord-highlightjs) theme. 

In order to fulfill the above requirements, I wrote the following helper function that when called: 

 1. loads _highlight.js_ scripts and styles, only if they aren't already
 2. [fetches](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) the source code from the specified remote resource 
 3. caches the result, and optionally trims it down to a specified line range 
 4. injects the text into the specified element
 5. executes block-level highlighting with _highlight.js_.

All in, here's what the function looks like:

<pre><code class="javascript" id="load-file-text-element.js"></code></pre>

Boom! That code sample just loaded itself. 

Loading code from it's living source leads and pulling the latest version is great benefit. However, if <code id="script" class="javascript inline">startLine</code> and <code id="script" class="javascript inline">endLine</code> are specified and the file's source is updated (and thus line numbers changed), those parameters must be updated. Something to remember.

Other optional parameters, <code id="script" class="javascript inline">filterPrefix</code> and <code id="script" class="javascript inline">removeEmptyLines</code> enable clean and concise presentation of the underlying executable source, and removes the clutter of note-taking and screen-eating line spacing.

<script>
    highlightInlineCode();  
   
    fetchAndHighlightCodeElement(
        {
            elementId: "load-file-text-element.js",
            fileUrl: "https://raw.githubusercontent.com/rwev/rwev.gitlab.io/master/content/assets/javascript/load-file-text-element.js"
        }
    );
</script>


