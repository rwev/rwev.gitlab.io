Title: Back to Basics with the Python and Curses
Category: oss/tui
Tags: contribution,python,code
Status: published

An experiment with the `curses` terminal application framework. 

[`Curses`](https://en.wikipedia.org/wiki/Curses_%28programming_library%29) is a "a terminal-independent screen-painting and keyboard-handling facility for text-based terminals" as written in the [documentation](https://docs.python.org/3/howto/curses.html) for the Python `curses` module, which provides a wrapper to C library. 

In the age of modern graphics and over-styled and over-stimulating web pages, the purity of [TUI](https://en.wikipedia.org/wiki/Text-based_user_interface) applications is refreshing. 

Because of the limitations inherent to the terminal environment, where an array printed characters composes the view of the application and key-presses the main source of interaction events, the designer must reckon with the essential and the extraneous, the meat and the gristle, and, in accepted software terms, the [KISS](https://en.wikipedia.org/wiki/KISS_principle) principle.

> This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface. <p class="annotation"><a href="http://catb.org/~esr/writings/taoup/html/ch01s06.html#id2878022">Doug McIlroy</a></p>

The constraints of the terminal add value by subtraction, _via negativa_, a concept not entirely foreign to design or life philosophy. Software build for it often provides exceedingly succinct interaction with data, instead of an overbuilt, bells-and-whistles UI detracting from it. 

Perhaps because of the maturity of the "terminal platform", many TUIs (also built with `curses`) provide the same modes and mechanisms of interface, gaining in portability and usability, with [learnability and memorability](/grounding-user-centric-design.html) coming nearly by default in many cases.

An example and personal favorite used in routine workflow is [`ranger`](https://github.com/ranger/ranger), a terminal-based file manager, also built with `curses` and Python, implementing `vim` keybindings, and designed with Unix principle in mind: "small but useful, with smooth integration into the shell."

The [`bible`](https://gitlab.com/rwev/bibt) project was an experiment with the framework, and an exercise in Python and user interface design. Its three-panel interface was inspired by that of `ranger`, and future `TODOs` include adding `vim`-like controls and `fzf` search: 

![bible.png]({photo}bible.png)

<!-- <div id="bible.cast"></div> --> 

<script>
        // fetchAsciinema({castFile: "bible.cast", divId: "bible.cast"});
</script>
