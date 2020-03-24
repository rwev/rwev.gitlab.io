Title: ProtonMail & Mutt: Secure Email in the Terminal
Category: oss/tui
Tags: privacy,security,bash,code
Status: published

Terminal user interfaces are fast, reliable, and proven; they've existed and their foundations tested and perfected over the decades since the dawn of the information age.
 
 The terminal user interface is timeless. TUIs provide pure interaction with data, oftentimes using the same principles of interaction and even sharing keybindings (like `vim`), and are devoid of visual and aesthetic bloat. But that's for another post.  

[`Mutt`](http://www.mutt.org/), like other terminal applications, is simple and thus secure. Terminal applications generally have less code & simpler design than their OS- or web-native counterparts, a large factor contributing to the tried-and-true stability of terminal tool-kits. 

As a program that interfaces with the unknown internet, `mutt` does not provide the prime breeding grounds of vulnerability and uncertainty such as a `JavaScript` runtime or a document rendering engine. `Mutt` and similar TUI applications are often written with the deterministic rigidity of C using time-tested frameworks like `curses`.  See [this article](https://www.vice.com/en_us/article/nzea38/why-security-experts-are-using-an-ancient-email-format-in-2015).

`Mutt` has been around since at least 1995, with `elm` ancestry dating to 1986, and is still in use and improved by powerusers today. Mail providers have come and gone, but Mutt continues to provide the interface to them. 

[ProtonMail](https://www.protonmail.com) is the latest of such providers, and as one of the few providers of fully-encrypted email and calendar services in a world of increasingly pervasive surveillance and an on-pace desire to escape it, they probably won't be going anywhere soon. 

The privacy and security of ProtonMail is derived from [PGP encryption](https://protonmail.com/blog/what-is-pgp-encryption/). All data is fully encrypted until it gets to the client's machine, where it is then decrypted with the password. This happens in the browser with [OpenPGPJS](https://github.com/openpgpjs/openpgpjs)
 when using the [web client](https://github.com/ProtonMail/WebClient).

Obviously the terminal doesn't follow REST or speak JavaScript so another application will have to talk to ProtonMail's Swiss servers, run the decryption locally, and provide the data for Mutt to access over IMAP and SMTP mail protocols, encryption-agnostic. That program is [hydroxide](https://github.com/emersion/hydroxide), an unofficial, "third-party, open-source ProtonMail bridge, _bridging_ the encryption process of ProtonMail with email standards.
  
  From it's <code class="bash inline">README.md</code>: 

    +-----------------+             +-------------+  ProtonMail  +--------------+
    |                 | IMAP, SMTP  |             |     API      |              |
    |  E-mail client  <------------->  hydroxide  <-------------->  ProtonMail  |
    |                 |             |             |              |              |
    +-----------------+             +-------------+              +--------------+
    
Install the bridge with <code class="bash inline">GO111MODULE=on go get github.com/emersion/hydroxide/cmd/hydroxide</code> and start it as follows: 

<pre><code class="bash" id="hydroxide-commands">
$ hydroxide auth [ProtonMail-username] [ProtonMail-password] # authenticates and decrypts your ProtonMail-box in memory, returns a password for the client "login" to the bridge
$ hydroxide imap # runs IMAP server for receiving email
$ hydroxide smtp # runs SMTP server for sending email

</code>
</pre>

Then, configure Mutt to login to the bridge, in <code class="bash inline">~/.muttrc</code>: 

<pre><code class="bash" id="muttrc-creds">
folder="imap://${1}:${bridge_pass}@127.0.0.1:1143" 
smtp_url="smtp://${1}:${bridge_pass}@127.0.0.1:1025"

</code></pre>

I've written a bash function, <code class="bash inline">protonmutt</code> to automate this, and start Mutt with the generated configuration: 

<pre><code class="bash" id="protonmutt"></code></pre>

Additionally, <code class="bash inline">washmutt</code> is a helper function that deletes sensitive information from the automatically written Mutt configuration file: 

<pre><code class="bash" id="washmutt"></code></pre>

And there you have it, fully encrypted, open-source, secure email running in a purely terminal, server-compatible environment.  

You can find my full `mutt` configuration [here on gitlab](https://gitlab.com/rwev/evix/-/tree/master/.mutt).

This post inspired by [spaceandtim.es](https://spaceandtim.es/code/protonmail_mutt/).

![protonmutt.png]({photo}tmux/protonmutt.png)

<script>
    highlightInlineCode();
    
    highlightCodeElement("muttrc-creds");
    highlightCodeElement("hydroxide-commands");
    
    fetchAndHighlightCodeElement(
        {
            elementId: "protonmutt",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.bash/functions/comms",
            startLine: 11,
            endLine: 1000,
            removeEmptyLines: false
        }
    );
    fetchAndHighlightCodeElement(
        {
            elementId: "washmutt",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.bash/functions/comms",
            startLine: 3,
            endLine: 10
        }
    );
</script>
