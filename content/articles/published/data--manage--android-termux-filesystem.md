Title: Elevated Android with Termux
Category: data
Tags: security,process,android-termux
Status: published
Gallery: {photo}/termux-nord-notes

[Termux](https://termux.com/) adds a basic Linux environment to Android devices, unlocking the smartphone for what it is: a computer. 

With access to a terminal emulator, [`zsh`](/the-z-shell-made-for-mankind.html), the Unix toolkit and workflow essentials , one can interact with the phone's filesystem and basic hardware functionality similar to a full-on laptop or desktop.

Pull down your dotfiles with your shell prompt, backup or update files with a `rsync` or [`git`](/dotfiles-plaintext-data-management-with-git.html), `grep` through phone data such as texts or contacts, edit plaintext with `vim`, or write simple alert & notification routines in Python. Termux offers a familiar gateway to control the Android mobile device & data and make it serve you. 

Prior to discovering Termux, I was left to cumbersome USB transfers or creating accounts with external sync services like Dropbox.  No more searching for third-party apps requiring an account and the shipment of data in order to satisfy obscure personal requirements. 

Especially paired with interface-enhancing devices like a [compact foldable keyboard](https://www.jellycomb.com/products/b003b-foldable-bluetooth-keyboard?variant=32901876809818), Termux is the liberation of Android and further increases the capability and versatility of the device already existing within your own pocket. After my experimentation with simple scripting, possibility and potential abound. 

## Termux in Production: nord-notes

A simple use case of Termux "in production" is with the management of Markdown notes.

[`billthefarmer`](https://github.com/billthefarmer)'s [Notes](https://f-droid.org/en/packages/org.billthefarmer.notes/) application available on F-Droid provides a simple Android interface for editing, stylizing, and managing Markdown documents, and saves them in plaintext to shared storage. 

By [granting Termux permission to shared storage](https://wiki.termux.com/wiki/Termux-setup-storage), Termux can access the save location. Initializing a git repository there, checking in the files, and pushing to remote stores makes them a `git pull` away on another computer. Security, portability, data-sovereignty, and familiarity in one.
 
 Syncing with the remote can then be automated with `Termux:Boot` or `Termux:Widget`.

Install Termux from F-Droid

- [Base system](https://f-droid.org/en/packages/com.termux/)
- [Themes](https://f-droid.org/en/packages/com.termux.styling/): customized [nord](https://nordtheme.com)
- [Boot](https://f-droid.org/en/packages/com.termux.boot/): run programs at device startup
- [Widget](https://f-droid.org/en/packages/com.termux.widget/): add script shortcuts with app icons