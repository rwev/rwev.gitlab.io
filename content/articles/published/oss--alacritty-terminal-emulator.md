Title: Alacritty: Rocket to Anywhere
Category: oss
Tags: terminal,config,tmux,vim,process
Status: published

[`Alacritty`](https://github.com/alacritty/alacritty) is a cross-platform terminal emulator. 

Regardless of whether I'm on my personal laptop, a 6 year old 13-inch slim ASUS Zenbook UX305FA with a scrawny 0.8 GHz M-5Y10 processor running [elementaryOS](https://elementary.io/) or at professional work on a latest-generation MacBook Pro, a personalized terminal configuration is just a [`git pull`](https://rwev.dev/dotfiles-plaintext-data-management-with-git.html) away.

The first customization of personal importance in my [`.alacritty.yml`](https://gitlab.com/rwev/evix/-/blob/master/.alacritty.yml) is the specification of a [`nordic`](https://github.com/arcticicestudio/nord-alacritty) theme (palette):

<pre><code class="yaml" id="alacritty.nord"></code></pre>

Secondly, I standardize to a patched [Fira Code](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode) font, complete with ligatures and special characters of interest to developers and required for rending more complex visual components in the terminal, such as a [`tmux-status`](https://github.com/arcticicestudio/nord-tmux) or [`vim-airline`](https://github.com/vim-airline/vim-airline). 

First the font must be installed to the systems with <code class="bash inline">mv ~/.fonts/* .local/share/fonts && fc-cache -f -v</code>. Verify the installation with output from <code class="bash inline"> fc-list | grep "Fura Code"</code>. I keep `ttf` and `otf` font files [with my dotfiles](https://gitlab.com/rwev/evix/-/tree/master/.fonts) to save time in system setup. 

<pre><code class="yaml" id="alacritty.font"></code></pre>

The rest of the configuration is rather uninteresting.

Whenever I set up my terminal and shell on a machine, I like to also install two command-line tools: [`bat`](https://github.com/sharkdp/bat) and [`lsd`](https://github.com/Peltoche/lsd). They are drop-in replacements for the traditional Unix utilities `cat` and `ls` but with some visual sugar for the modern programmer and leveraging patched fonts. 

![bat-lsd.png]({photo}tmux/bat-lsd.png)

<script>
    highlightInlineCode();  
   
    fetchAndHighlightCodeElement(
        {
            elementId: "alacritty.nord",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.alacritty.yml",
            filterPrefix: "#",
            startLine: 26,
            endLine: 51
        }
    );

    fetchAndHighlightCodeElement(
        {
            elementId: "alacritty.font",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.alacritty.yml",
            filterPrefix: "#",
            startLine: 14,
            endLine: 18
        }
    );

</script>








