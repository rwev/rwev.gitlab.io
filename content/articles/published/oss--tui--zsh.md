Title: The Z-Shell, Made For Mankind
Category: oss/tui
Tags: code,config,bash
Status: published

When interacting with Unix machines from the command line, [zsh](http://zsh.sourceforge.net/) is the go-to shell, offering substantial practical benefits alleviating strains and monotony in the human-computer interface.  

Some of my personal delights:

- Spell correction <code class="bash inline">$ touche meta.txt <ENTER> zsh: correct 'touche' to 'touch' [nyae]? </code>
- Recursive path expansion: <code class="bash inline">$ /u/lo/b <TAB> -> /usr/local/bin</code>
- Interactive command and parameter completion <code class="bash inline">$ echo $PA <TAB> -> echo $PATH; $ git subm <TAB> -> git submodule</code> with descriptions and basic documentation
- Safety checks <code class="bash inline">$rm -rf ./* -> zsh: sure you want to delete all 100 files in /home/rwev/. [yn]? n</code>
- Multi-line command editing 
- Extensibility with plugins and themes

Furthermore, the zsh is supported by the strong [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh) user community, which continually provides Z-Shell aliases, bindings, and completions for the command-line utilities and applications, greatly reducing the complexity of utilizing unfamiliar APIs and the necessity of rote memorization and keystrokes. 

My <code class="bash inline">.zshrc</code> file is simplified by the use of <code class="bash inline">.oh-my-zsh</code>, which does the heavy lifting of loading the list of configured plugins: 

<pre><code class="bash" id=".zshrc.general"></code></pre>

The zsh is thus mostly compatible with Bash, so I load some of my <code class="bash inline">.bash_</code> configuration files into the zsh here also. Obviously, <code class="bash inline">.zsh_</code> files are zsh specific.

<pre><code class="bash" id=".zshrc.sources"></code></pre>

I use the "pretty, minimal, fast" and asynchronous [pure](https://github.com/sindresorhus/pure) for my prompt / theme. Download its sources, make sure they are on your <code class="bash inline">$fpath</code>. I put the source files in <code class="bash inline">~/.zfunctions</code> [directory](https://github.com/rwev/evix/tree/master/.zfunctions) and then load the prompt:

<pre><code class="bash" id=".zshrc.prompt"></code></pre>

All files can be found in my dotfiles repository, [evix](https://gitlab.com/rwev/evix).

And there you have it: a forgiving, efficient, and living shell that reduces keystrokes and generally alleviates the much frustration of working in the terminal, allowing the user to do more of what they do best: be human. 

<!-- TODO add FZF plugin description, TODO write FZF-specific article, consolidating vim and zsh plugins -->

<script>

    highlightInlineCode();   
    
    fetchAndHighlightCodeElement(
    {
        elementId: ".zshrc.general",
        fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.zshrc",
        startLine: 4,
        endLine: 30,
        filterPrefix: "#"
    }
    );
    fetchAndHighlightCodeElement(
     {
        elementId: ".zshrc.sources",
        fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.zshrc",
        startLine: 31,
        endLine: 37,
        filterPrefix: "#",
     }
     );
    fetchAndHighlightCodeElement(
     {
         elementId: ".zshrc.prompt",
         fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.zshrc",
         startLine: 46,
         endLine: 52,
         filterPrefix: "#"
     }
    );

</script>

 
  
