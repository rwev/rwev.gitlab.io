

The term “UNIX” is technically and legally a trademark of The Open Group, and should formally
be used only for operating systems which are certified to have passed The Open Group’s elaborate
standards-conformance tests. In this book we use “Unix” in the looser sense widely current among
programmers, to refer to any operating system (whether formally Unix-branded or not) that is either
genetically descended from Bell Labs’s ancestral Unix code or written in close imitation of its
descendants. In particular, Linux (from which we draw most of our examples) is a Unix under
this definition

This is a book about Unix programming, but in it we’re going to toss around the words ‘culture’,
‘art’, and ‘philosophy’ a lot. If you are not a programmer, or you are a programmer who has had little
contact with the Unix world, this may seem strange. But Unix has a culture; it has a distinctive art
of programming; and it carries with it a powerful design philosophy. Understanding these traditions
will help you build better software, even if you’re developing for a non-Unix platform.

Every branch of engineering and design has technical cultures. In most kinds of engineering,
the unwritten traditions of the field are parts of a working practitioner’s education as important
as (and, as experience grows, often more important than) the official handbooks and textbooks.
Senior engineers develop huge bodies of implicit knowledge, which they pass to their juniors by (as
Zen Buddhists put it) “a special transmission, outside the scriptures”.
Software engineering is generally an exception to this rule; technology has changed so rapidly,
software environments have come and gone so quickly, that technical cultures have been weak and
ephemeral. There are, however, exceptions to this exception. A very few software technologies have
proved durable enough to evolve strong technical cultures, distinctive arts, and an associated design
philosophy transmitted across generations of engineers.
The Unix culture is one of these. The Internet culture is another — or, in the twenty-first century,
arguably the same one. The two have grown increasingly difficult to separate since the early 1980s,
and in this book we won’t try particularly hard.

The Durability of Unix
Unix was born in 1969 and has been in continuous production use ever since. Unix has supported a mind-bogglingly wide spectrum of uses. No other operating system has shone simultaneously as a research vehicle, a friendly host for technical custom applications, a platform for commercial-off-the-shelf business software, and a vital component technology of the Internet.

At least one of Unix’s central technologies — the C language — has been widely naturalized
elsewhere. Indeed it is now hard to imagine doing software engineering without C as a ubiquitous
common language of systems programming. Unix also introduced both the now-ubiquitous treeshaped file namespace with directory nodes and the pipeline for connecting programs.

Unix’s durability and adaptability have been nothing short of astonishing. Other technologies have
come and gone like mayflies. Machines have increased a thousandfold in power, languages have
mutated, industry practice has gone through multiple revolutions — and Unix hangs in there, still
producing, still paying the bills, and still commanding loyalty from many of the best and brightest
software technologists on the planet.

One of the many consequences of the exponential power-versus-time curve in computing, and the
corresponding pace of software development, is that 50% of what one knows becomes obsolete over
every 18 months. Unix does not abolish this phenomenon, but does do a good job of containing it.
There’s a bedrock of unchanging basics — languages, system calls, and tool invocations — that one
can actually keep using for years, even decades. Elsewhere it is impossible to predict what will be
stable; even entire operating systems cycle out of use. Under Unix, there is a fairly sharp distinction
between transient knowledge and lasting knowledge, and one can know ahead of time (with about
90% certainty) which category something is likely to fall in when one learns it. Thus the loyalty
Unix commands.


But perhaps the most enduring objections to Unix are consequences of a feature of its philosophy
first made explicit by the designers of the X windowing system. X strives to provide “mechanism,
not policy”, supporting an extremely general set of graphics operations and deferring decisions about
toolkits and interface look-and-feel (the policy) up to application level. Unix’s other system-level
services display similar tendencies; final choices about behavior are pushed as far toward the user
as possible. Unix users can choose among multiple shells. Unix programs normally provide many
behavior options and sport elaborate preference facilities.
This tendency reflects Unix’s heritage as an operating system designed primarily for technical users,
and a consequent belief that users know better than operating-system designers what their own needs
are.

“it is better
to solve the right problem the wrong way than the wrong problem the right way”

But the cost of the mechanism-not-policy approach is that when the user can set policy, the user
must set policy. Nontechnical end-users frequently find Unix’s profusion of options and interface
styles overwhelming and retreat to systems that at least pretend to offer them simplicity.
In the short term, Unix’s laissez-faire approach may lose it a good many nontechnical users. In the
long term, however, it may turn out that this ‘mistake’ confers a critical advantage — because policy
tends to have a short lifetime, mechanism a long one. Today’s fashion in interface look-and-feel too
often becomes tomorrow’s evolutionary dead end (as people using obsolete X toolkits will tell you
with some feeling!). So the flip side of the flip side is that the “mechanism, not policy” philosophy
may enable Unix to renew its relevance long after competitors more tied to one set of policy or
interface choices have faded from view.