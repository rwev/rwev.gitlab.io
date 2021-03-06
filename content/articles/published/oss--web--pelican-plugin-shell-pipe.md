Title: Pelican Plugin: Shell Pipe
Category: oss/web
Tags: python,contribution,code
Status: published

[`shell_pipe`](https://gitlab.com/rwev/shell_pipe) is a plugin for the Pelican static site generator (SSG) for piping shell output into site content, unlocking the versatility and flexibility of the shell for automated content generation and updates, closing the gap between the Unix shell and the web (browser). 

The plugin hooks into the <code class="python inline">pelican.signals.all_generators_finalized</code> signal, which is emitted after all content is transpiled from markdown / rich text into HTML documents. Then, the plugin searches the HTML documents for the <code class="python inline">('SHELL_BEGIN','SHELL_END')</code> flags, parses a command string from between them, and executes the string through the host machine's shell with <code class="python inline">subprocess.check_output(code_str, shell=True).decode('utf-8')</code> Lastly, the flags are replaced with the output of the command wrapped in some HTML to assist in stylization of the final web document. 

All of this, in code: 

<pre><code id="shell-pipe-py" class="python"></code></pre>

I've implemented a profitable use case of the plugin on my other blog, [coyote.life](https://coyote.life/skoolie-budget). As you can see, the financial balance sheet generated by [`hledger`](https://hledger.org) is embedded in the article, with the command used to generate it listed above. 

Since I already use `hledger` to track finances from the command line, I didn't need to do any additional work (other than write this plugin) to get its output onto the web. Simply writing those commands into the [plain text](https://gitlab.com/rwev/coyote.life/-/raw/master/content/articles/published/skoolie--budget.md) of the site sources is enough. Additionally, site compilation and deployment is triggered on each commit with [`.gitlab-ci`](https://gitlab.com/rwev/coyote.life/-/blob/master/.gitlab-ci.yml), so the entire site is regularly regenerated to include up-to-date `shell_pipe` output. 

See the full [`README`](https://github.com/rwev/shell_pipe/blob/master/README.md).

<script>
    highlightInlineCode();  
   
    fetchAndHighlightCodeElement(
        {
            elementId: "shell-pipe-py",
            fileUrl: "https://raw.githubusercontent.com/rwev/shell_pipe/master/shell_pipe.py",
            removeEmptyLines: false,
            startLine: 21,
            endLine: 50
        }
    );

</script>






