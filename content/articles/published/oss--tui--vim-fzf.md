Title: Vim & FZF, Versatility For Value  
Category: oss/tui
Tags: code,vim,config
Status: published

Aside from becoming familiar with the [out-of-the-box](/vim-configuration-built-in.html) capabilities of `vim`, I've settled on a few plugins that make using `vim` realistic for a "modern" workflow.

Although I use more plugins in my [`plugins.vim`](https://github.com/rwev/evix/blob/master/.vim/plugins.vim) configuration file, most of which offer very specialized or specific extension of functionality, I will present the most useful and most versatile plugin in the arsenal, and by far my top choice: [`fzf.vim`](https://github.com/junegunn/fzf.vim). 

This configuration integrates a code search tool and the command-line fuzzy-finder [`fzf`](https://github.com/junegunn/fzf) into `vim` to accelerate human-friendly navigation between files, content in the current directory or `git` repo, symbolic indexed code tags, `vim` actions, and so on. 

The code searcher used by the plugin is configurable: I use silversearcher [`ag`](https://github.com/ggreer/the_silver_searcher), but one could also use `ripgrep` [`rg`](https://github.com/BurntSushi/ripgrep). I've installed `fzf` with [`vim-plug`](https://github.com/junegunn/vim-plug) and configured it so:

<pre><code class="bash" id="fzf.vim"></code></pre>

Search files with the following mapping:
 
<pre><code class="bash" id="fzf.vim.files"></code></pre>
 
or all file contents: 
  
<pre><code class="bash" id="fzf.vim.contents"></code></pre>

This plugin alone offers significant productivity boosts with minimal complication and maximal versatility. 

Reading code and understanding larger project structure  constitute a majority of the time one spends programming. Jumping around in un/familiar documents or code becomes an frictionless with `fzf` , freeing more of one's attention from menial computer operation and diverting it to being fully present in the construct at hand.  

Furthermore, fuzzy-finding reduces keystrokes across the board. One must only enter the character sequence most unique to what are looking for, instead of a sequential exact match. 

Its benefits extend beyond the technical domain: it has also proved beneficial in the searching human-lingual documents and content, and even locating specific sentences.  
 
The following [`asciicast`](https://asciinema.org) offers a demonstration:
 
<div id="fzf.vim.cast"></div>
 
<script>

    fetchAndHighlightCodeElement(
        {
            elementId: "fzf.vim",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.vim/plugins.vim",
            startLine: 14, 
            endLine: 17,
            filterPrefix: "\""
        }
     );
     
    fetchAndHighlightCodeElement(
     {
         elementId: "fzf.vim.files",
         fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.vim/plugins.vim",
         startLine: 18, 
         endLine: 19,
         filterPrefix: "\""
     }
    );
    
    fetchAndHighlightCodeElement(
       {
           elementId: "fzf.vim.contents",
           fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.vim/plugins.vim",
           startLine: 19, 
           endLine: 20,
           filterPrefix: "\""
       }
    );


    fetchAsciinema({castFile: "fzf.vim.cast", divId: "fzf.vim.cast", startTime: "0:08"});

</script>
