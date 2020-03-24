Title: The Alacritty Terminal Emulator
Category: oss
Tags: terminal,config,tmux,vim,process

Status: published

[`Alacritty`](https://github.com/alacritty/alacritty) is a cross-platform terminal emulator.

I prefer the `Alacritty` emulator almost strictly because of its versaility. 

It runs on all major operating systems. Regardless of whether I'm on my personal laptop, a 6 year old 13-inch slim ASUS Zenbook UX305FA with only 8 gigabytes of RAM and fanless M-5Y10 processor clocking at a scrawny 0.8 GHz running elementaryOS or at professional work on a latest-generation MacBook Pro, my full terminal configuration is just a `git pull` away. 

The first major customization in my configured [`.alacritty.yml`](https://gitlab.com/rwev/evix/-/blob/master/.alacritty.yml) is the specification of a [`nordic`](https://github.com/arcticicestudio/nord-alacritty) theme (palette):

<pre><code class="yaml" id="alacritty.nord"></code></pre>

<pre><code class="yaml" id="alacritty.font"></code></pre>


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








