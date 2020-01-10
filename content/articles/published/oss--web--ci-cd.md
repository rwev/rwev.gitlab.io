Title: Power of Web-Based: CI/CD
Category: oss/web
Tags: process
Status: published

Twenty years ago, Paul Graham created what some acknowledge as the first web-based application. He writes about why applications belong on the web, and how the arrangement is beneficial for the customer and in many way, the developer as well.

Without a doubt, he beat the trend, as most user-facing applications follow this model, and continuous integration / deployment (CI/CD) has become commonplace and is now considered a de-factor requirement for all software shops large and small. 

His essay on web-based applications, [The Other Road Ahead], can be found <a href="http://paulgraham.com/road.html">here</a>, and to Paul belong all further quotes. 

## The Road Ahead

In this first essay, Paul discusses a realization he had: that having software being central to the client via the standardized and universal web browser.

He offers possibly the first definition: 
> Web-based software offers the biggest opportunity since the arrival of the microcomputer... [they] are programs that run on web servers and use web pages as the user interface.

with the hypothesis that
> For the average user this new kind of software will be easier, cheaper, more mobile, more reliable, and often more powerful than desktop software.

As we will see, nearly every aspect of the web-based development and delivery model (arguably) improves the experience of both parties. The benefits delivered offer a rare case study of consumer/producer symbiosis in a competition-/efficiency-driven market.   

### Continuous Shipment

Desktop applications twenty years ago, and surely also today, simply require much more fuss of the user. The average computer owner doesn't understand how installations work, let alone how to repair or fix when something goes wrong.
> When we look back on the desktop software era, I think we’ll marvel at the inconveniences people put up with, just as we marvel now at what early car owners put up with.

Because the servers (delivering _service_) to the users are centralized and in the control of the developers, the entire application can be updated simply by restarting it server-side with updated code. The client-side application itself is reloaded with every interaction with the server (via the foundational [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) architecture of the internet) and thus the client gets all updates as they use it, with negligible downtime and no extra work to the user. This is CI/CD before it was cool.
> With web-based software, [the user] should get new releases without paying extra, or doing any work, or possibly even knowing about it. <br><br> This is in large contrast to the desktop software update process. In this case, binary code inhabits on each and every client machine. Therefore it's only practical to do a couple of updates to desktop software per year, as process is surely a hassle to users and sometimes expensive... doing a release is a huge trauma, in which the whole company sweats and strains to push out a single, giant piece of code.  

With the web-application model, the atrocities of downloads, disks, serial codes, local files, and broken installations all go away, and the user can focus on the application itself, completely isolated from managing the software themselves. All they have to think about is their identifying credentials and log in pull the latest version of the application. 
> Most users won’t have to think about anything except the applications they use. All the messy, changing stuff will be sitting on a server somewhere, maintained by the kind of people who are good at that kind of thing.

The performance of the program is also easier to control, because the driving force of the application is running on the server, which is in full control of the business.
> When you control it you can do more for users. With a desktop application, you can specify certain minimum hardware, but you can’t add more.

It's hard to deliver a more powerful application when you don't control the hardware.

### Real-Time Monitoring

While web-based development seems like a win for every angle for the customers, it is almost so for the developers. Managing a web-based application is more work for the people who develop is, because they need to manage it as well.  
> All the programmers have to be to some degree system administrators as well. When you’re hosting software, someone has to be watching the servers, and in practice the only people who can do this properly are the ones who wrote the software.

It's a never ending developing, pushing, and monitoring process, which is very hard to hire out. The developers also know the code well enough to fix it in an emergency.
> Web-based software is never going to be something you write, check in, and go home. It’s a live thing, running on your servers right now.It’s a live thing, running on your servers right now. A bad bug might not just crash one user’s process; it could crash them all. If a bug in your code corrupts some data on disk, you have to fix it.

He described this evolved culture of the next wave of companies to host their software in the cloud as a typical startup, but on steroids.
> In a startup writing web-based applications, everything you associate with startups is taken to an extreme. You can write and launch a product with even fewer people and even less money. You have to be even faster, and you can get away with being more informal.

The internet is always awake, and so are your competitors. You don't go home a winner until your competitors let you. With such fortunes at stake, concession doesn't arrive quickly.  In the words of the great General James Mattis: "no war is over until the enemy says it's over. We may think it over, we may declare it over, but in fact, the enemy gets a vote."
> Web-based software never ships. You can work 16-hour days for as long as you want to. And because you can, and your competitors can, you tend to be forced to. You can, so you must. It’s Parkinson’s Law running in reverse.

Although the server-side application model demands around-the-clock monitoring from the developer, it also makes the development process more fulfilling by shortening the feedback loop, and decreasing the pain of debugging and enabling and easing quick iteration  user-centric design, as we'll see in a later article.  