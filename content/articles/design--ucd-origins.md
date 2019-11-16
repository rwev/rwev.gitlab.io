Title: 1984: Origins of User-Centric Design 
Category: design
Tags: ucd
Status: published

_The 1984 Olympic Message System: A Test of Behavioral Principles of System Design_ by Gould, Boies, Levy, Richards, and Schoonard delivers an ever-revered case study and analysis of system design methodology.

During the development of a groundbreaking software system that would allow Olympic athletes to communicate between themselves and also with family from around the world, the team made extensive efforts to adhere to the following pre-defined principles outlined and record the process for post-delivery analysis.

I've effectively made my own summary of this article (which is already quite summarized), and inserted my own thoughts, and versions of the authors, along the way. In total, what follows is one giant citation, thus I credit the original source completely.

## The Principles of System Design

Although many approaches to carrying out these principles are application-specific, the principles themselves are deemed "fully exportable." I've recombined, to an extent, the ideology from the implementations of the design strategy back to the design strategy itself, as it isn't always clear. These principles are fundamentally intertwined, and efforts to achieve one of them also lifts the others.

### Early Focus on Tasks and Users

This principle is two-fold.

First, the designers must understand _who_ the users will be. Before even thinking about the inner workings of a user interface system, define your users. What general cognitive abilities will they possess? How comfortable are they interacting with technology? Will their be any external forces acting on them in the interaction process?

Secondly, users should involved in the design process, and continuously consulted for feedback. What do the users find difficult and why? If they are stuck at a particular step of an interaction with your technology, discover _what they wish they knew _and also _what they wish they could do _in that very instance.

Disconnect with users breeds ambiguity and misunderstanding, and an unclear or misunderstood feature is no feature at all. In fact, a poorly implemented feature could be a detriment rather than a plus in terms of the total user experience.
<div class="quote">
    Designers often do not acknowledge the additional learning burdens that various help and error-correcting approaches place on learners... We received regular and strong emphasis to reduce function to a minimum.
    </div>

### Empirical Measurement

Run simulations early and often. And they don't require code.

Before even having a running system, run proposed implementations (in the form of documents such as prefabricated user guides or what the author calls "printed scenarios: exactly how we envisioned the user interface would look") past your users, and observe and measure their reactions to it.

<div class="quote">
    Simulations provide early tests as to whether the system actually takes care of a problem -- or introduces new problems since the user must now know how to use it.
</div>


Such documentation and example usages provide the first definition of the system. They give it existence, and although they are definitively superficial, they "powerfully determine system organization."

Writing such guides can easily commence long before the first line of code is written.

<div class="quote">
    [Our documentation and printed scenarios] allowed [our users] to see, comment, and criticize at a time when their comments would have the most impact. They gave existence to the system... the scenarios provided the opportunity to make changes to the potential user interface, and accompanying function, before any code was written...These scenarios saved time, because, on the basis of people's feedback, code was never written for functions that otherwise would have been implemented...
</div>

Writing user guides early provides a portable way to bring the essence of a new system to the attention of potential users in a form that they can react to.

When a working system is running, it's also possible to run empirical tests. It's not always arriving at what exactly can be quantitatively tested in a user interface, but a three-step process is defined:

- set some _behavioral _criteria the system should meet;
- put these criteria into specific, testable terms;
- testing against these terms using users and simulation / prototype.

### Iterative Design

This is based on the assumption that no designer or programmer can achieve a flawless outcome on the first attempt.

<div class="quote">
    There must be a cycle of design, test and measure, and redesign, repeated as often as necessary.
</div>

Iterative development is most efficient when a thorough project log ("diary") is also kept to

- "record observations and results"
- "document personal feelings"
- "retaining (and annotating) earlier revisions (and subsequent changes)"

When iterative design is combined properly with project journalism; it can "prevent well-intentioned but counter-productive changes later on." Write about what is changed and why, so you aren't tempted to erase the reasoning and coding effort invested to solve a previously encountered problem, thus resulting in the problem's reappearance.

Iterative design connects with the other principles in that simulation and resulting empirical measurement find bugs and areas of weakness, which are solved in the  iteration cycle.

#### Integrated Usability Design

<div class="quote">
    Usability factors must evolve together, and responsibility for all aspects of usability should be under one control.
</div>

Although the "major components of usability are developed sequentially, they jointly interact and affect each other." Therefore, they should be developed in parallel.

## Making It Practical

In order to make these principles useful, the whole design and development team needs to be in agreement.

Moreover, focus on usability, and further strengthened by these principles, should start at project day zero. Deny the "peanut butter" theory of usability: you _can't _just spread it on at the end.

They also followed previously defined development principles and put in the necessary work on the front end (in documentation and "printed scenarios") and throughout (constant documentation, diary keeping) of the project in order to reap benefits of this system design methodology.

The principles proved fruitful, and continue to to this very day.


