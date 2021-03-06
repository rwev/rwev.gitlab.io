Title: tmux, Skeleton of Terminal Productivity
Category: oss/tui
Tags: config,tmux,code,nord
Status: published

`tmux` overcomes some of the largest hindrances to real productivity at the terminal. 

A major obstacle is the fact that only one command can be run in the foreground. Processes can be run in parallel (e.g. with <code class="bash inline">$ bg; fg; jobs</code>) but it is cumbersome to manage, and doesn't provide reasonable and immediate transparency into the underlying process (e.g. logs). 

Terminal procedure generally envisioned by novices proceeds as follows: type an _awk_-ward command, wait for it to run (often with no output, per the [unix rule of silence](https://homepage.cs.uri.edu/~thenry/resources/unix_art/ch01s06.html#id2878450)), observe (or guess) the result, and repeat.

Enter [`tmux`](https://github.com/tmux/tmux), a "terminal multiplexer it enables a number of terminals to be created, accessed, and controlled from a single screen."

As a member of the desktop generation and a terminal amateur, `tmux` provides the view / layout flexibility we've come to expect from modernity's GUI-centric operating systems. Translating the official purpose statement at the beginning of this post to practical function, it splits a terminal screen into "panes" and "windows" (in `tmux` jargon), all of which spawn and run the users default <code class="inline bash">echo $SHELL</code>, where multiple terminal jobs can run separately, side-by-side.

`tmux` is the framework around which I've built my productivity system in the terminal. The ability to split and resize panes, close them, or start a whole new window (set of panes) for  distinct tasks enables one to build an integrated development environment, [block by block](https://homepage.cs.uri.edu/~thenry/resources/unix_art/ch01s06.html#id2877537).

Additionally, `tmux` "may be detached from a screen and continue running in the background, then later reattached." `tmux` runs as a server in its own process independent from the terminal; the terminal simply interfaces with it. Even if you accidentally kill your terminal window (e.g. with ⌘-W on macOS), the `tmux` server lives, along with the processes and layout inside: just open a new terminal window and reattach. 

Here's the configuration that I've arrived at after intermittent tinkering. It provides settings for a simple, unobtrusive header, including network status (online / offline), remaining battery power, date / time, and hostname, in a calm [nordic](https://github.com/arcticicestudio/nord-tmux) theme. 

Other (invisible) plugins provide session restoration functionality and a reasonable copy / paste interface with the host OS. And I only use small, curated and intentional subset of the plugins [out there](https://github.com/tmux-plugins).

<pre><code class="bash" id="tmux.conf"></code></pre>

Here's a screenshot of working in `tmux` to write [this article](/protonmail-mutt-secure-email-in-the-terminal.html):

![tui.png]({photo}tmux/ide.png)

<script>
    highlightInlineCode();  
   
    fetchAndHighlightCodeElement(
        {
            elementId: "tmux.conf",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.tmux.conf",
            filterPrefix: "#",
        }
    );
</script>















