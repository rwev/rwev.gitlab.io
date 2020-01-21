Title: Downloading Webpages
Category: oss/tui



When I plan on experimenting, developing, and thinking on the go, I like to download documentation and references in advance. Staying focused and always having the necessary resources on hand is far more productive than constantly prowling for the next WiFi connection, an often sketchy one at that, or being offline entirely.

Normally, this involves cloning a git repository or a PDF, if one as available. But many resources aren't easily accessible in that format, particularly older web documents. 

Take for example, Eric Raymond's [_The Art of Unix Programming_](https://homepage.cs.uri.edu/~thenry/resources/unix_art), written in 2003 and a future-proof work. Suppose it wasn't available in PDF form (it [is](https://www.catb.org/esr/writings/taoup/html/graphics/taoup.pdf)). How would you save it for efficient access on the go?

My solution is a recursive bash function, which takes a target directory, a web resource (presumably returning HTTP <code class="bash inline">content-type: text/html</code>) as an entry point, and a recursion depth. It relies only on <code class="bash inline">curl</code>, a Linux staple, and optionally on <code class="bash inline">lynx</code>, the terminal-based web browser, to view and navigate the downloaded documents in the terminal. 

The function does roughly the following: 

1. requests the HTML document for the entry point, 
2. saves the response as the root resource in the target directory, <code class="bash inline">${dir}/index.html</code>,
3. parses brute-force parse for links within the document in the form of <code class="html inline">href</code> attributes, 
4. repeats steps 1 - 3 for each discovered resource, building out the document tree in subdirectories.
5. opens the root resource in lynx, which renders the document sensibly in the terminal.

<pre><code class="bash" id="sitedl"></code></pre>

<script>

highlightInlineCode();

fetchAndHighlightCodeElement({
        elementId: "sitedl",
        fileUrl: "",
        startLine: 2,
        endLine: 32,
        filterPrefix: "#",
        removeEmptyLines: true
                });
                
</script>


