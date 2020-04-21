Title: Built-in Vim Configuration   
Category: oss/tui
Tags: code,vim,config,nord

My first experience with vim was frustrating, as it is for many. Grown in a world of fully-featured IDEs, vim was barely usable or comprehensible, let alone productive, without any configuration.

If I had to learn it again, I would use this configuration as a starting point, and if possible, _without_ plugins. Still maintain a general understanding what each line does. 

Add plugins incrementally and on a needs basis, so as to understand what the editor itself does, and what _exactly_ plugins do to extend that functionality.

<pre><code class="bash" id="config.vim"></code></pre>

I haven't found much use for custom keybindings, and I don't picture adding many until [grokking](http://www.catb.org/jargon/html/G/grok.html) vim itself, with the exception of [plugin integration](/vim-plugin-fuzzy-finder.html).

<pre><code class="vim" id="mappings.vim"></code></pre>

All files can be found in my dotfiles repository, [evix](https://gitlab.com/rwev/evix).


<script>

    fetchAndHighlightCodeElement(
        {
            elementId: "config.vim",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.vim/config.vim",
            filterPrefix: "\""
        }
     );
     
    fetchAndHighlightCodeElement(
        {
            elementId: "mappings.vim",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.vim/mappings.vim",
            filterPrefix: "\""
        }
     );
</script>


