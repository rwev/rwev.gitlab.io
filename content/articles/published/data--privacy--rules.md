Title: Rules for Online Account Security & Privacy
Category: data
Tags: code,bash,privacy,security
Status: published

Data insecurity and inadequate online security measures are as prevalent as society's reliance on the internet. Here are some layman-accessible ways to protect your data, your identity, and even your finances online.  

## Use Login-less Services.

When possible, the best way to protect your information online is to never hand it out in the first place. There may not be a login-less provider for the service your after (and never will be for some spaces, such as online banking), but it never hurts to [check](https://github.com/fiatjaf/awesome-loginless). Plus, you protect valuable real estate in your email inbox from inundation by promotions and suggestions.

## No Connected Accounts.

Linking accounts by logging in to a site with an account from another (e.g. signing into AirBnB, Zillow, or now CoD Mobile with your Google or Facebook account) has been a huge trend in recent years. 

Connected accounts may add some level of security by eliminating the need for multiple (usually reused and / or more easily guessed) passwords and thus enabling the user to focus on security / strong passwords for the central node accounts. 

However, the centralization of authorization introduces fragility: once the central node account is compromised, the whole login network is compromised. 

Using login features like this also expedites data collection and aggregation processes.
 
Instead of potentially having to piece together disparate pieces of information, or being barred from sending data to a third party, the central node services (Google / Facebook) now have access to varying degrees of personal information provided by third party services as required by the login process, like which services you use, and how often you log into them, at a minimum. 

The data sharing threat goes the other way too. Indiscriminate approval given to an overreaching account permission request from a third party can offer any data from the central node account: your friends list, social activity, call and text history, emails, contacts, calendar events, and location data. 

## No Shared Passwords.

Don't reuse passwords. 

All it takes is one hack of an imprudent site or service that mismanages customer data and stores that password in plaintext, and they have the two most critical pieces of information that identify you on the web: your email or username, which you likely also reuse. 

They just have to try that login elsewhere, and they're in and they're you.
 
Fortunately, many sites, especially financial ones, are adding device recognition with email verification into their login processes. Just don't use the same password for email service too. 

I prefer random passwords - here's the shell code I use to generate them:

<pre><code class="bash" id="bash-creds"></code></pre>

The first function <code class="bash inline">passwnorm</code> generates a 12 character alphanumeric password that suffices for most accounts, like <code class="bash inline">4dRiMxMQe3lL</code>. When heightened security is warranted, such as for financial accounts, <code class="bash inline">passwspec</code> produces passwords of 18 characters with special symbols, like <code class="bash inline">gV$4OENa_M2:Y{pt)m</code>

## Use a Password Manager

The last two points, unlinking accounts and never reusing passwords, sounds like a recipe for messy password spaghetti. 

And it is, if you don't use a password manager. 

Use one! Not only does it save strain on your memory and reduce keystrokes, but it will save your sanity and enable better online security. 

I use [Bitwarden](https://bitwarden.com) to encrypt and sync my table of passwords between devices. It auto-saves and fills passwords in the browser (with appropriate plugin) and on mobile (via native app). 

Bitwarden even offers a command-line interface which can be used to pipe credentials securely into [other terminal applications](/protonmail-mutt-secure-email-in-the-terminal.html) that require auth.

Bitwarden also provides a password generation feature that provides random string passwords similar to the above bash commands, without the necessity of access to terminal, as it is available within all clients. 

Lastly, Bitwarden is a secure, fully-encrypted repository not only for passwords, but credit card information, personal details ("identity"), or any other free-form text ("secure notes"). 

Mozilla Firefox's [Lockwise](https://www.mozilla.org/en-US/firefox/lockwise/) is another decent alternative with a narrower feature set.  

## Diversify Your Online Footprint

Transition to open-source alternatives whenever possible. Try not to remain within the product ecosystem of any one tech concern. Don't let them own, and profit from, your online life. 

It's okay to continue using selected products from major tech companies, but don't give them combined access. Distribute the dimensions of your life over multiple products and ecosystems. Do open source as much as possible. _Diversify_ and [degoogle](/how-i-degoogle.html).

## Security as a State of Mind

Putting the above rules into practice won't happen in a day. It will be gradual process. Don't attempt to make the transition over days or weeks. Unlinking accounts, transitioning to privacy-oriented open-source, and changing passwords can take months, and it never ends, as accounts are continuously created and deleted in the ever-evolving market of online services.    

Locking down your online presence to maximize security and minimize data collection is a state of mind. 

<script>
    highlightInlineCode();
   fetchAndHighlightCodeElement(
        {
            elementId: "bash-creds",
            fileUrl: "https://raw.githubusercontent.com/rwev/evix/master/.bash/functions/credentials",
            filterPrefix: "#"
        }
    );
</script>
