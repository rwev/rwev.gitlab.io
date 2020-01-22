Title: ProtonMail & Mutt: Secure Email in the Terminal
Category: oss/tui
Tags: privacy,security,bash,code
Status: published

Terminal User Interfaces (TUIs): they are fast, reliable, and proven; they've existed and their foundations perfected since the dawn of the terminal and tested real-time over decades. Their interface is timeless. TUIs provide pure interaction with data, oftentimes using the same principles of interaction and even sharing vim keybindings, and devoid of visual and aesthetic bloat. But that's for another post.  

[Mutt](http://www.mutt.org/) is one such TUI application, an email client that's  been around since at least 1995, and still in use and improved by powerusers today. Mail providers have come and gone, but Mutt continues to provide the interface to them. [ProtonMail](https://www.protonmail.com) is the latest of such providers, and as one of the few providers of fully-encrypted email and calendar services in a world of increasingly pervasive surveillance and an on-pace desire to escape it, they probably won't be going anywhere soon. 

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
