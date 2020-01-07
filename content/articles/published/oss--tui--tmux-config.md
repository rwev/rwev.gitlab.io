Title: tmux, Skeleton of Terminal Productivity
Category: oss/tui
Tags: config,tmux,code
Status: published

[tmux](https://github.com/tmux/tmux) is a "terminal multiplexer it enables a number of terminals to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattached."

tmux allows to user to overcome what is probably seen (especially by new users) the largest hindrance to real productivity at the terminal: only one command can be run in the foreground at once. There are, of course, way to run processes in the background with <code class="bash inline">$ bg; fg; jobs</code> but it is cumbersome to manage, and doesn't provide reasonable and immediate transparency into the underlying process (e.g. logs). Terminal procedure generally envisioned by novices proceeds as follows: type an _awk_-ward command, wait for it to run (often with no output, by design: the [Unix Rule of Silence](https://homepage.cs.uri.edu/~thenry/resources/unix_art/ch01s06.html#id2878450)), observe (or guess at) the result, and repeat.

As a member of the desktop generation and a terminal amateur, tmux provides the view / layout flexibility we've come to expect from modern GUI-centric operating systems. Translating the official purpose statement at the beginning of this post to practical function, it splits a terminal screen into "panes" and "windows" (in tmux jargon), all of which spawn and run the users default <code class="inline bash">echo $SHELL</code>, where multiple terminal jobs can run separately, side-by-side.

tmux is the framework around which I've built my productivity system in the terminal. The ability to split and resize panes, close them, or start a whole new window (set of panes) for  distinct tasks enables one to build an integrated development environment, [block by block](https://homepage.cs.uri.edu/~thenry/resources/unix_art/ch01s06.html#id2877537).

Here's the configuration that I've arrived at after intermittent hours of tinkering. It provides settings for a simple, unobtrusive header, including network status (online / offline), remaining battery power, date / time, hostname, in a soothing, uniform, [nordic](https://github.com/arcticicestudio/nord-tmux) theme. 

Other (invisible) plugins provide session restoration functionality and reasonable copy / paste interface with the host OS. And I only use small, curated and intentional subset of the plugins out [there](https://github.com/tmux-plugins).

<pre><code class="bash" id="tmux.conf"></code></pre>

<script>
    highlightInlineCode();  
   
    loadFileTextElement(
        {
            elementId: "tmux.conf",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.tmux.conf",
            filterPrefix: "#",
        }
    );
</script>















