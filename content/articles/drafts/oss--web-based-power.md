Title: The Power of Web-Based
Category: oss/development
Status: published

###  Portability

Web-based applications are powered by "the cloud", a concept which didn't exist. Paul recognized the power of this now-ubiquitous concept to deliver a superior, more flexible, and more secure user experience, without calling it "the cloud."

The cloud computing trend of recent decades was called by prophesied by Paul as the shift from "your computer" to "your data."
> To use a purely web-based application, all you need is a browser connected to the Internet. So you can use a web-based application anywhere... With purely web-based software, neither your data nor the applications are kept on the client.

Thus the ability for the client to access the application to manipulate their data isn't limited to any one machine, rather a storage location somewhere in the provider's server, where it is accessible by any device that can access the web.

### Safety
Web-based applications offer enhanced data security, on multiple grounds.

For one, and as mentioned before, data is not stored and manage by the users, instead on the servers of the company. Most standard users of most standard software products are not going to be the types who actively think about maintaining a current backup of the disk, which somewhat predictably results in lost data.
> When you use a web-based application, your data will be safer. Disk crashes on’t be a thing of the past, but users won’t hear about them anymore. They’ll happen within server farms. And companies offering web-based applications will actually do backups—not only because they’ll have real system administrators worrying about such things, but because an ASP that does lose people’s data will be in big, big trouble.

Secondly, the client must not download anything to begin using the software: not the software itself, not updates, not data. When the average user isn't downloading and running executables on their machine, the likelihood of introducing a virus is vastly reduced.
> If the client doesn’t run anything except a browser, there’s less chance of running viruses, and no data locally to damage. And a program that attacked the servers themselves should find them well defended.

### Development Flexibility
The term _software stack_ wasn't always the buzzword that it is today. In the past, no such concept existed. Code was all written in C/C++ and compiled into one big binary executable. The distribution hurdles required to deliver desktop software in higher-level languages are simply too great.

> When you’re writing desktop software, you’re practically forced to write the application in the same language as the underlying operating system—meaning C and C++.

Web-based applications often consist of more programs, which can be written in a variety of languages, assembled to form the program.

Using high-level languages is no problem, because they only need to be installed on the back-end servers, not on the client. Furthermore, languages can be selected for the tasks at which they excel.
> Because the software in a web-based application will be a collection of programs rather than a single binary, it can be written in any number of different languages.

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

all written with the preferred tools and frameworks of the _developer_. 

### Quality and the Iterative Process

This is closely related to a previous advantage, continuous shipment.

> With server-based software, most of the change is small and incremental. That in itself is less likely to introduce bugs. It also means you know what to test most carefully when you’re about to release software: the last thing you changed. 
 <br><br>
 You end up with a much firmer grip on the code. As a general rule, you do know what’s happening inside it. You don’t have the source code memorized, of course, but when you read the source you do it like a pilot scanning the instrument panel, not like a detective trying to solve a mystery. When [a bug] turns up you often know what’s wrong before you even look at the source, because you were already worrying about it subconsciously. 

Bugs tend to show themselves sooner rather than later because the whole force of users are using the latest version. Defects can be fixed much more efficiently and before they are conceal themselves in long-forgotten code, as developers maintain an up-to-date context on what has changed since the last (recent) release. 
 
> With Web-based applications, everyone uses the same version, and bugs can be fixed as soon as they're discovered. So Web-based software should have far fewer bugs than desktop software. 
 <br><br>
 [With desktop software] you end up with a statistical sort of correctness. Thus bugs tends to accumulate in the time between these discrete shipping times... Fixing a bug in something you wrote six months ago (the average case if you release once a year) is a lot more work. 

### Quick Iteration and Feedback

All of the code that powers a web-based application is running on the server, directly observable by the developers and debuggers. Instead trying to work out the bugs occurring in a remote execution environment,
> You have the users’ data right there on your disk. Web-based software gets used round the clock, so everything you do is immediately put through the wringer. Bugs turn up quickly.

Finding bugs, or conceptualizing new features, is so much more rewarding when the fixes and functionality expansions can be delivered quickly. One can see his work make a difference -- perhaps the next day the new software can be up and running on the server. But if the next desktop release is 9 months from now, the bug list is Sisyphus' boulder.
> Being able to release software immediately is a big motivator. Often as I was walking to work I would think of some change I wanted to make to the software, and do it that day. If I’d had to wait a year for the next release, I would have shelved most of these ideas, for a while at least. The thing about ideas,though, is that they lead to more ideas.Working to implement one idea gives you more ideas. So shelving an idea costs you not only that delay in implementing it, but also all the ideas that implementing it would have led to.

He also points out a divide in a similar vein between small companies and big companies.
> What big companies do instead of implementing features is plan them.

What big companies do instead of debugging bugs is talk about them and add them to the list.

### Happy Customers, Happy Developers
With desktop applications, there is not much you can gain from the average customer who calls in to report a bug.

> With the first customer who calls in, the bug will be noted and put in a queue. But the bug will sit on their machine for months until the next major release, as dozens more users eventually encounter the same bug and complain. It quicky becomes old, and as Paul puts in, the Quality-Assurance and Customer Service People become paid targets of complaints that can't actually help the customers, just apologize.

> They’re either calling you about a known bug, or they’re just doing something wrong and you have to figure out what. In either case there’s not much you can learn from them.

Again, it couldn't be more different in the web-based format. Bugs can be dealt with on the first call, empowering the customer, reducing the costs of service people, and putting the developers in closer and more positive (less draining and same-old) relationship with the users, and generally increasing the worth of the feedback system as a whole.

> But with web-based, because we wanted to hear from customers. If someone had a problem, we wanted to know about it right away so we could reproduce the error and release a fix. Our approach to support made everyone happier. The customers were delighted.... the customer support people liked it because it meant they could help the users, instead of reading scripts at them. And the programmers liked it because they could reproduce bugs instead of just hearing vague second-hand reports about them.

### User-Centered Design, Out of the Box

Web-based applications foster the conditions necessary for <a href="http://taw.life/2017/10/22/user-centered-design-the-standards/">proper user-centered design</a>.

One of the most important of such conditions is the ability to test the software with actual users to reveal how and when users encounter difficulty in their interaction with the application.

For desktop applications, the developing company must commit considerable man-hours to this endeavor: recruit testers, hire people to administer and report on the testing, and so on. But with web-based applications, this is built-in. Every click made, when, and in what order is registered on the server asking to be logged.

> Software should do what users think it will. Server-based software gives you unprecedented information about their behavior. You can see every click made by every user. With server-based software, you can watch actual users.

And this is something that all Software companies should embrace emphatically.

> Software companies are sometimes accused of letting the users debug their software. And that is just what I’m advocating. When it turns up you often know what’s wrong before you even look at the source, because you were already worrying about it subconsciously. Fixing a bug in something you wrote six months ago (the average case if you release once a year) is a lot more work.

### As a Business
Software companies are still business and have to manage their finances properly to survive. Web-based design aids in this pursuit as the nature of the service is suited to the subscription basis.

> For companies, web-based applications are an ideal source of revenue. Instead of starting each quarter with a blank slate, you have a recurring revenue stream. Because your software evolves gradually, you don’t have to worry that a new model will flop.

Essentially, web-based software products are a source of revenue dampen the volatility on the income statement.


### In Summary
The argument for web-based applications ultimately can be boiled down to raw economics.
> Most people, most of the time, will take whatever choice requires least work. If web-based software wins, it will be because it’s more convenient. And it looks as if it will be, for users and developers both.

As mentioned it's not a pure win for both producers and consumers.
> Desktop software forces users to become system administrators. Web-based software forces programmers to. There is less stress in total, but more for the programmers.

Lastly, just as hosted software empowers the user, it also empowers small business over big business.
> You don’t have to ask anyone’s permission to develop web-based applications. You don’t have to do licensing deals, or get shelf space in retail stores, or grovel to have your application bundled with the OS. You can deliver software right to the browser, and no one can get between you and potential users without preventing them from browsing the Web.




