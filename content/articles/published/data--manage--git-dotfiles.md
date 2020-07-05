Title: Dotfiles & Plaintext Data Management with Git
Category: data
Tags: config,security,process
Status: published

How I manage my dotfiles, both public and private, at very little expense with `git`. 

To store (configuration) dotfiles at `$HOME` (where they are both actively being read by programs referencing them) and simultaneously managed by `git`, I use an `ignore-all` hack <code class="bash inline">echo "*" >> .gitignore</code>. Then, specific files and directories to be tracked are explicitly pushed past the catch-all with a forced add: <code class="bash inline">git add -f track-this.txt</code>.

Before I found [the post](https://drewdevault.com/2019/12/30/dotfiles.html) that proposed this idea, my dotfiles repository was cloned to some subdirectory of `$HOME` and copied back and forth from `$HOME` with a bash function. However, the script was primitive & naive and didn't do a proper sync, and as such changes to dotfiles were accidentally overwritten in either direction (retrospectively, a mature solution like `rsync` would've been better). But with the ignore-all hack, syncing is made irrelevant: dotfiles are tracked exactly where they are used and edited, with no movement or `cp`-ing necessary.

I host my configuration dotfiles in a [public repository](https://gitlab.com/rwev/evix). What about the dotfiles containing potentially confidential, or a least personally identifiable, plaintext data information? Examples of these are [`hledgers`](https://hledger.org), [`vim-notes`](https://github.com/xolox/vim-notes), [`abooks`](http://abook.sourceforge.net/), [`newsbeuter`](https://newsbeuter.org/) RSS URLs, or [`sc-im`](https://github.com/andmarti1424/sc-im) spreadsheets that I might not want to share with everyone on the planet with access to the internet. Let's call these data-dotfiles.

There are various mechanisms would could use to encrypt sensitive files in a git repository, like [`git-crypt`](https://wTags: terminal,config,tmux,vim,process
Status: publishedww.agwa.name/projects/git-crypt/). Having attempted to use this in my daily workflow, I found it to be an overly onerous addition to the data management process. It needs to installed and configured in the terminal of any machine that wishes to access the unencrypted data; it is impossible to use a web client to gain access. Encryption keys, whether symmetric or asymmetric, need to be remembered or configured too. 

Instead, a private git repository will do. The simple protection that a private repo provides with zero overhead is more than adequate for the type of data I store with them. While it's not encrypted and plaintext is stored on gitlab's server, accessing the data would mean a hack of gitlab's infra or theft of my  credentials. For now, I trust gitlab, at least enough to store data of this type in this form.

The private git repository is also configured using the `ignore-all` hack. Because the data-dotfiles also belong at `$HOME`, `.git` metadata would conflict. To get around this, I rename the metadata directory for the data-dotfiles repo: <code class="bash inline">mv .git .git.dat</code>.

Now both dotfile repository have root at $HOME. To use them separately, an alias does the trick: <code class="bash inline">alias gitdat='git --git-dir=.git.dat'</code>. 
    
<script>
    highlightInlineCode();  
</script>

      
  




 
