Title: The Power of Web-Based
Category: oss--development
Status: published

Twenty years ago, Paul Graham created what some acknowledge as the first web-based application. He writes about why applications belong on the web, and how the arrangement is beneficial for the customer and the developer and represents a great leap in the economic efficiency of software development.

Without a doubt, he beat the trend.

The original article, to which all further quotes belong to, can be found <a href="http://paulgraham.com/road.html">here</a>.

## The Other Road Ahead
_Web-based software offers the biggest opportunity since the arrival of the microcomputer._

In this first essay, Paul discusses a realization he had: that having software being centrally to the client via the standardized and universal web browser.

The first definition that he offers

<div class="quote">
    Web-based applications are programs that run on web servers and use web pages as the user interface.
</div>

With the hypothesis that

<div class="quote">
    For the average user this new kind of software will be easier, cheaper, more mobile, more reliable, and often more powerful than desktop software.
</div>

The amazing part is that every aspect improves the experience of the customer as well as the developer. I can't imagine a stronger win-win in a business scenario.

### The Delivery Experience
Desktop applications twenty years ago, and surely also today, simply require much more fuss of the user. The average computer owner doesn't understand how installations work, let alone how to repair or fix when something goes wrong.

<div class="quote">
    When we look back on the desktop software era, I think we’ll marvel at the inconveniences people put up with, just as we marvel now at what early car owners put up with.
</div>

The atrocities of downloads, disks, serial codes, localized files, all goes away, and the user can focus on the application itself, completely isolated from managing the software themselves. All they have to think about is their identifying credentials.

<div class="quote">
    With web-based software, most users won’t have to think about anything except the applications they use. All the messy, changing stuff will be sitting on a server somewhere, maintained by the kind of people who are good at that kind of thing.
</div>

The performance of the program is also easier to control, because the driving force of the application is running on the server, which is in full control of the business.

<div class="quote">
    When you control it you can do more for users. With a desktop application, you can specify certain minimum hardware, but you can’t add more.
</div>

It's hard to deliver a more powerful application when you don't control the hardware.

### The Portability

Web-based applications are powered by "the cloud", a concept which didn't exist. Paul recognized the power of the cloud to deliver a superior, more flexible, and more secure user experience, without calling it "the cloud."

The cloud computing trend of recent decades was called by prophesied by Paul as the shift from "your computer" to "your data."

<div class="quote">
    To use a purely web-based application, all you need is a browser connected to the Internet. So you can use a web-based application anywhere... With purely web-based software, neither your data nor the applications are kept on the client.
</div>

Thus the ability for the client to access the application to manipulate their data isn't limited to any one machine, rather a storage location somewhere in the hosting company's server farm, where it is accessible by any device that can access the web.

### Continuous Shipment
Because the servers that deliver the application service to the centralized on-site the entire application can be continuously updated buy restarting, essentially, a single process on the server machine with updated code.

Because all client devices all maintain a real-time connection to this same server, they all receive the same updates in real time, with negligible downtime and no extra work to them.

<div class="quote">
<p>
    With web-based software, [the user] should get new releases without paying extra, or doing any work, or possibly even knowing about it.With web-based applications, everyone uses the same version, and bugs can be fixed as soon as they’re discovered. So web-based software should have far fewer bugs than desktop software. You release software as a series of incremental changes instead of an occasional big explosion.
</p>
<p>
This is in large contrast to the desktop software update process. In this case, binary code inhabits on each and every client machine. Therefore it's only practical to do a couple of updates to desktop software per year, as process is surely a hassle to users and sometimes expensive. Thus bugs tends to accumulate in the time between these discrete shipping times. 
</p>
<p>
    In the desktop software business, doing a release is a huge trauma, in which the whole company sweats and strains to push out a single, giant piece of code... At best you end up with a statistical sort of correctness.
    </p>
</div>

### Improved Iterative Process

This is closely related to the previous advantage, continuous shipment.

<div class="quote">
    With server-based software, most of the change is small and incremental. That in itself is less likely to introduce bugs. It also means you know what to test most carefully when you’re about to release software: the last thing you changed. You end up with a much firmer grip on the code. As a general rule, you do know what’s happening inside it. You don’t have the source code memorized, of course, but when you read the source you do it like a pilot scanning the instrument panel, not like a detective trying to solve a mystery.

When it turns up you often know what’s wrong before you even look at the source, because you were already worrying about it subconsciously. Fixing a bug in something you wrote six months ago (the average case if you release once a year) is a lot more work.
</div>

### Safety

Web-based applications offer enhanced data security, on multiple grounds.

For one, and as mentioned before, data is not stored and manage by the users, instead on the servers of the company. Most standard users of most standard software products are not going to be the types who actively think about maintaining a current backup of the disk, which somewhat predictably results in lost data.

<div class="quote">
    When you use a web-based application, your data will be safer. Disk crashes on’t be a thing of the past, but users won’t hear about them anymore. They’ll happen within server farms. And companies offering web-based applications will actually do backups—not only because they’ll have real system administrators worrying about such things, but because an ASP that does lose people’s data will be in big, big trouble.
</div>

Secondly, the client must not download anything to begin using the software: not the software itself, not updates, not data. When the average user isn't downloading and running executables on their machine, the likelihood of introducing a virus is vastly reduced.

<div class="quote">
    If the client doesn’t run anything except a browser, there’s less chance of running viruses, and no data locally to damage. And a program that attacked the servers themselves should find them well defended.
</div>

### Development Flexibility

The term _software stack_ wasn't always the buzzword that it is today. In the past, no such concept existed. Code was all written in C/C++ and compiled into one big binary executable. The distribution hurdles required to deliver desktop software in higher-level languages are simply too great.

<div class="quote">
    When you’re writing desktop software, you’re practically forced to write the application in the same language as the underlying operating system—meaning C and C++.
</div>

Web-based applications often consist of more programs, which can be written in a variety of languages, assembled to form the program.

Using high-level languages is no problem, because they only need to be installed on the back-end servers, not on the client. Furthermore, languages can be selected for the tasks at which they excel.

<div class="quote">
    Because the software in a web-based application will be a collection of programs rather than a single binary, it can be written in any number of different languages.
</div>

This is not required or otherwise done out of necessity; this is done because it's powerful.

A complete application could include:

- Server itself, talking to user
- Programs used by server (database)
- Sub-programs performing specific tasks, like sending bills and processing transactions
- Programs looking for problems
- Programs that restart other programs when they break
- Programs that compile and analyze usage stats
- Simulation programs pretending to be users
- Programs that generate real-time dashboards for server management

### Quick Iteration and Feedback
All of the code that powers a web-based application is running on the server, directly observable by the developers and debuggers. Instead trying to work out the bugs occurring in a remote execution environment,

<div class="quote">
    You have the users’ data right there on your disk. Web-based software gets used round the clock, so everything you do is immediately put through the wringer. Bugs turn up quickly.
</div>

Finding bugs, or conceptualizing new features, is so much more rewarding when the fixes and functionality expansions can be delivered quickly. One can see his work make a difference -- perhaps the next day the new software can be up and running on the server. But if the next desktop release is 9 months from now, the bug list is Sisyphus' boulder.

<div class="quote">
    Being able to release software immediately is a big motivator. Often as I was walking to work I would think of some change I wanted to make to the software, and do it that day. If I’d had to wait a year for the next release, I would have shelved most of these ideas, for a while at least. The thing about ideas,though, is that they lead to more ideas.Working to implement one idea gives you more ideas. So shelving an idea costs you not only that delay in implementing it, but also all the ideas that implementing it would have led to.
</div>

He also points out a divide in a similar vein between small companies and big companies.

<div class="quote">
    What big companies do instead of implementing features is plan them.
</div>

What big companies do instead of debugging bugs is talk about them and add them to the list.

### Happy Customers, Happy Developers
With desktop applications, there is not much you can gain from the average customer who calls in to report a bug.

With the first customer who calls in, the bug will be noted and put in a queue. But the bug will sit on their machine for months until the next major release, as dozens more users eventually encounter the same bug and complain. It quicky becomes old, and as Paul puts in, the Quality-Assurance and Customer Service People become paid targets of complaints that can't actually help the customers, just apologize.

<div class="quote">
    They’re either calling you about a known bug, or they’re just doing something wrong and you have to figure out what. In either case there’s not much you can learn from them.
</div>

Again, it couldn't be more different in the web-based format. Bugs can be dealt with on the first call, empowering the customer, reducing the costs of service people, and putting the developers in closer and more positive (less draining and same-old) relationship with the users, and generally increasing the worth of the feedback system as a whole.

<div class="quote">
    But with web-based, because we wanted to hear from customers. If someone had a problem, we wanted to know about it right away so we could reproduce the error and release a fix. Our approach to support made everyone happier. The customers were delighted.... the customer support people liked it because it meant they could help the users, instead of reading scripts at them. And the programmers liked it because they could reproduce bugs instead of just hearing vague second-hand reports about them.
</div>

### User-Centered Design, Out of the Box

Web-based applications foster the conditions necessary for <a href="http://taw.life/2017/10/22/user-centered-design-the-standards/">proper user-centered design</a>.

One of the most important of such conditions is the ability to test the software with actual users to reveal how and when users encounter difficulty in their interaction with the application.

For desktop applications, the developing company must commit considerable man-hours to this endeavor: recruit testers, hire people to administer and report on the testing, and so on. But with web-based applications, this is built-in. Every click made, when, and in what order is registered on the server asking to be logged.

<div class="quote">
    Software should do what users think it will. Server-based software gives you unprecedented information about their behavior. You can see every click made by every user. With server-based software, you can watch actual users.
</div>

And this is something that all Software companies should embrace emphatically.

<div class="quote">
    Software companies are sometimes accused of letting the users debug their software. And that is just what I’m advocating. When it turns up you often know what’s wrong before you even look at the source, because you were already worrying about it subconsciously. Fixing a bug in something you wrote six months ago (the average case if you release once a year) is a lot more work.
</div>

### As a Business
Software companies are still business and have to manage their finances properly to survive. Web-based design aids in this pursuit as the nature of the service is suited to the subscription basis.

<div class="quote">
    For companies, web-based applications are an ideal source of revenue. Instead of starting each quarter with a blank slate, you have a recurring revenue stream. Because your software evolves gradually, you don’t have to worry that a new model will flop.
</div>

Essentially, web-based software products are a source of revenue dampen the volatility on the income statement.

### The Possible Downside...
While web-based development seems like a win for every angle for the customers, it is almost so for the developers.

Managing a web-based application is more work for the people who develop is, because they need to manage it as well.

<div class="quote">
    All the programmers have to be to some degree system administrators as well. When you’re hosting software, someone has to be watching the servers, and in practice the only people who can do this properly are the ones who wrote the software.
</div>

It's a never ending developing, pushing, and monitoring process, which is very hard to hire out. The developers also know the code well enough to fix it in an emergency.

<div class="quote">
    Web-based software is never going to be something you write, check in, and go home. It’s a live thing, running on your servers right now.It’s a live thing, running on your servers right now. A bad bug might not just crash one user’s process; it could crash them all. If a bug in your code corrupts some data on disk, you have to fix it.
</div>

He described this evolved culture of the next wave of companies to host their software in the cloud as a typical startup, but on steroids.

<div class="quote">
    In a startup writing web-based applications, everything you associate with startups is taken to an extreme. You can write and launch a product with even fewer people and even less money. You have to be even faster, and you can get away with being more informal.
</div>

The internet is always awake, and so are your competitors. You don't go home a winner until your competitors let you. With such fortunes at stake, concession doesn't arrive quickly.  In the words of the great General James Mattis: "no war is over until the enemy says it's over. We may think it over, we may declare it over, but in fact, the enemy gets a vote."

<div class="quote">
    Web-based software never ships. You can work 16-hour days for as long as you want to. And because you can, and your competitors can, you tend to be forced to. You can, so you must. It’s Parkinson’s Law running in reverse.
</div>

### In Summary

The argument for web-based applications ultimately can be boiled down to raw economics.

<div class="quote">
    Most people, most of the time, will take whatever choice requires least work. If web-based software wins, it will be because it’s more convenient. And it looks as if it will be, for users and developers both.
</div>

As mentioned it's not a pure win for both producers and consumers.

<div class="quote">
    Desktop software forces users to become system administrators. Web-based software forces programmers to. There is less stress in total, but more for the programmers.
</div>

Lastly, just as hosted software empowers the user, it also empowers small business over big business.

<div class="quote">
    You don’t have to ask anyone’s permission to develop web-based applications. You don’t have to do licensing deals, or get shelf space in retail stores, or grovel to have your application bundled with the OS. You can deliver software right to the browser, and no one can get between you and potential users without preventing them from browsing the Web.
</div>




