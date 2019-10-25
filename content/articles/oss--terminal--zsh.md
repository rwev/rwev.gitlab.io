Title: Terminal Essentials: The Z-Shell 
Category: oss/vim
Tags: oss,vim,linux,config,terminal,productivity
Status: published

When interacting with Unix machines from the command line, I've found [Z shell](http://zsh.sourceforge.net/) to be essential. 

The list of advantages over the standard Bash shell is long. Some of my personal delights:

- Command completion
- Multi-line command editing 
- Spell correction
- Extensibility with plugins and themes

Furthermore, the Z Shell is supported by the strong [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh) user community, which continually integrates Z-Shell functionality with the latest in command-line tools and applications. 

My [.zshrc](https://github.com/rwev/evix/blob/master/.zshrc) file is simplified by the use of <code class="bash inline">.oh-my-zsh</code>, which does the heavy lifting of loading the list of configured plugins, enabling auto-correct, command completion, etc. for the corresponding applications.

<pre><code class="bash" id=".zshrc.general"></code></pre>

The Z Shell is thus mostly compatible with Bash, so I load some of <code class="bash inline">.bash_</code> configuration files into the Z shell here. Obviously, <code class="bash inline">.zsh_</code> files are Z Shell specific.

I use the "pretty, minimal, fast" and asynchronous [pure](https://github.com/sindresorhus/pure) for my prompt / theme. Download its sources, make sure they are on your <code class="bash inline">$fpath</code>. I put the source files in <code class="bash inline">~/.zfunctions</code> directory. 

<pre><code class="bash" id=".zshrc.zfunctions"></code></pre>

Then load the prompt with 

<pre><code class="bash" id=".zshrc.prompt"></code></pre>

And there you have it: a forgiving, efficient, and living shell that reduces keystrokes and generally alleviates the much frustration of working in the terminal, allowing the user to do more of what they do best: be human. 

<script>

    document.querySelectorAll('code').forEach((block) => {
      hljs.highlightBlock(block);
    });

    loadFileTextElement(
    {
        elementId: ".zshrc.general",
        fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.zshrc",
        startLine: 0,
        endLine: 47
    }
    );
    loadFileTextElement(
     {
         elementId: ".zshrc.zfunctions",
         fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.zshrc",
         startLine: 2,
         endLine: 3
     }
    );
    loadFileTextElement(
      {
          elementId: ".zshrc.prompt",
          fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.zshrc",
          startLine: 47,
          endLine: 49
      }
    );
</script>


 
  
