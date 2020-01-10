Title: Vim and Beyond
Category: oss/tui
Tags: code,vim
Status: published

Within the first few months of using vim, I saw this [post](https://www.reddit.com/r/vim/comments/bm0ihb/evolution_of_a_vim_user/) and related comments on Reddit that I sympathized with, adapted to personal experience here.

## Journey of a _vim_ User

1. Write and save your first file with vim
2. Discover ~.vimrc and build your own frankenstein ~.vimrc from snippets on the internet, while ignoring all the nearby comments to RTFM
3. Become allured by shiny plugins and spend forty hours digging for them in Reddit threads and GitHub links and adding them to ~.vimrc
4. Look at ~.vimrc in horror, and realize that you don't actually understand vim _or_ the plugins
5. Admit that you do need to [RTFM](http://www.catb.org/jargon/html/R/RTFM.html), like people said all along
6. Realize that despite sophisticated editing mechanisms and endless customizability / extensibility, using vim is hurting productivity

> So, you switch back to zero-configuration IDE (like JetBrains' IntelliJ) to focus on automating business value instead of your development environment. You relegate vim to editing configuration files and commit messages and look back fondly on all that configuration you set up. Miss vim, but move on with life and appreciate your ability to automatically
 
 - interact with version control and databases
 - find and replace across the entire codebase
 - refactor file and symbol names across whole project, with code, string, and comment awareness 
 - manage imports, dependencies, and environments
 - integrate file-watching and build tools
 - enforce style rules with auto-fixers
 - find warnings and errors, and resolve with intelligent best-practice suggestions
 - fuzzy-find files, actions, symbols, and settings
 - debug and profile

all intuitively and _without_:

 - cryptic vim-specific commands
 - learning vimscript
 - training and ingraining non-transferable keybindings and modal editing
 - the visual constraints of the terminal
 - books, ["quickrefs"](https://vimhelp.org/quickref.txt.html#quickref), [cheat sheets](https://vim.rtorr.com/), or even [RTFM](http://www.catb.org/jargon/html/R/RTFM.html), and [guides for powerusers](https://github.com/hakluke/how-to-exit-vim/blob/master/README.md) on how to exit the program.  
 
  For these reasons, a strong argument can be made that vim does not embody [user-centric design](/grounding-user-centric-design.html); it is, in fact, very unusable according to the original definition, particularly in regards to learnability and memorability. Even the installer for git, another venerable piece of OSS software based in the terminal, offers the following warning while configuring it's default editor:
  
  > The Vim editor, while powerful, can be hard to use. Its user interface is unintuitive and its key bindings are awkward. Vim is the default editor for Git only for historical reasons, and it highly recommended to switch to a modern GUI editor instead.
 
## Age as a Factor of Interest
 
My generation grew up with GUIs: they moderated our first interactions with computers and beyond. Knowledge of the terminal came only later, when I become interested in development. GUIs, as the point of first and continuous contact, were comfortable and homey, and the terminal foreign.    

But for the older generations of technologists, it was just the opposite. They grew up with the CLI, and GUIs were something that came later. Perhaps that is why the older generation prefers vim: it is a TUI, and as such shows itself in the place they feel most familiar with: the terminal. 

For youngsters, vim is a sort of hipster, learning it a matter of paying tribute to those who have come before, a rite of passage, while the real work gets done somewhere else.  

Perhaps vim is indeed as powerful as an editor can be when caged in the terminal, but when compared absolutely to modern technology offerings, any TUI editor, including vim, falls short.  

## A Career Investment
When [grokked](http://www.catb.org/jargon/html/G/grok.html), vim competes with modern IDEs, but learning vim is a huge investment, and not one for the faint of heart. Gaining a return or reaching break-even requires a commitment on the scale of years, if not decades.
 
 The return of learning vim is more efficient text editing. However, most programmer time is spent reading, navigating, understanding, and planning. Editing itself is trivial and mechanical. Investments in efficiency are better made elsewhere. 
 
I don't even know if I'll be writing code in three years. In the meantime, I'd rather focus on my own valued-added development interests. Going further doesn't seem worth it. YMMV.

## The Reminiscence
My time with vim was ultimate an exercise in Unix and everything it stands for. Having written my first code in a full-service, integrated IDE, learning how to use and configure vim greatly increased the breadth and depth of my knowledge of programming tools and workflow and how it all comes together. Programming in vim emphasizes the [Unix philosophy](https://homepage.cs.uri.edu/~thenry/resources/unix_art/ch01s06.html): vim is one tool alongside others in the kit of "Unix as an IDE" and exists alongside other under the rules of modularity, composition, and separation. 





