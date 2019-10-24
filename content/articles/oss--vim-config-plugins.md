Title: Vim Plugin: Fuzzy-finder
Category: oss/vim
Tags: oss,vim,,linux,write,code,config,tui,productivity
Status: published

Aside from becoming familiar with the [out-of-the-box](/vim-configuration-built-in.html) capabilities of vim, I've settled on a few plugins that make using vim realistic for a "modern" workflow.

Although I use more plugins in my [plugins.vim](https://github.com/rwev/evix/blob/master/.vim/plugins.vim) configuration file, most of which offer very specialized / specific extension of functionality, I will present the most useful and most versatile plugin in the arsenal: [fzf.vim](https://github.com/junegunn/fzf.vim). 

This configuration integrates a code search tool and the command-line fuzzy-finder [fzf](https://github.com/junegunn/fzf) into vim to accelerate navigation between files or content in the current directory. The code searcher used by the plugin is configurable: I use silversearcher [ag](https://github.com/ggreer/the_silver_searcher), but one could also use ripgrep [rg](silver-searcher).

<pre><code class="bash" id="fzf.vim"></code></pre>

Search files with the following mapping:
 
<pre><code class="bash" id="fzf.vim.files"></code></pre>
 
or all file contents: 
  
<pre><code class="bash" id="fzf.vim.contents"></code></pre>

This plugin alone offers one _significant_ productivity boosts, as reading code and understanding larger project structure and principles constitute a majority of the time one spends programming. It's benefits extend beyond the technical domain: it has also proved beneficial in the searching human-lingual documents and content, and even locating specific sentences. Fuzzy-finding is a powerful formula.   
 
<script>

    loadFileTextElement(
        {
            elementId: "fzf.vim",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.vim/plugins.vim",
            startLine: 14, 
            endLine: 17
        }
     );
     
    loadFileTextElement(
     {
         elementId: "fzf.vim.files",
         fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.vim/plugins.vim",
         startLine: 18, 
         endLine: 19
     }
    );
    
    loadFileTextElement(
       {
           elementId: "fzf.vim.contents",
           fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.vim/plugins.vim",
           startLine: 19, 
           endLine: 20
       }
    );
          
</script>


