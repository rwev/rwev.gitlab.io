Title: tmux, Skeleton of Terminal Productivity
Category: oss/tui
Tags: config,tmux,code

[tmux](https://github.com/tmux/tmux) is a "terminal multiplexer it enables a number of terminals to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattached."


tmux allows to user to overcome what is probably seen (especially by new users) the largest hindrance to real productivity at the terminal: only one command can be run in the foreground at once. 

There are, of course, way to run processes in the background with <code class="bash inline">$ bg; fg; jobs</code> but it is cumbersome to manage, and doesn't provide reasonable and immediate transparency to the underlying process (e.g. logs)

But generally, the process envisioned by novices: type an _awk_-ward command, wait for it to run (often with no output, by design: the [Unix Rule of Silence](https://homepage.cs.uri.edu/~thenry/resources/unix_art/ch01s06.html#id2878450)), observe (or guess at) the result, and repeat.

As a member of the desktop generation and an aforementioned terminal novice, tmux does what we've come to expect from modern GUI-centric operating systems, and ironically enough, what Microsoft's Windows is named for. Translating the official purpose statement at the beginning of this post to practical function, it enables, effectively, splitting the screen into "panes", and even having multiple "windows", all of which spawn and run the users default <code class="inline bash">echo $SHELL</code>

tmux is the framework around which I've built my productivity system in the terminal. The ability to split and resize panes, close them, and open a whole new window for a different task enables one to build an integrated development environment, [block by block](https://homepage.cs.uri.edu/~thenry/resources/unix_art/ch01s06.html#id2877537).

Here's the configuration that I've arrived at after hours of tinkering. It provides simple, unobstructive visual settings, including network status (online / offline), remaining battery power, date / time, and a soothing, uniform [nordic](https://github.com/arcticicestudio/nord-tmux) experience. 

Other invisible plugins provide session restoration functionality and reasonable copy / paste interface with the host OS. (a subset of the plugins out [there](https://github.com/tmux-plugins)).
<pre><code class="bash" id="tmux.conf"></code></pre>

<script>
    highlightInlineCode();  
   
    loadFileTextElement(
        {
            elementId: "tmux.conf",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.tmux.conf",
            filterPrefix: "#"
        }
    );
</script>















