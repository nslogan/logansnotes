+++
title = "Migrating to Zola"
date = 2021-02-19
+++

Hello, Internet, it's been a while. In fact, it's been so long that I forgot most of what I learned about Pelican 9 months ago, which gave me the perfect excuse to switch static site generators. When I was initially setting my site up last year I picked Pelican after googling "static site generator markdown." Somewhere along the line I came across [Matthias Endler's blog](https://endler.dev/) (which I suggest reading, great stuff) and discovered he was using [Zola](https://www.getzola.org/).

At the time, I thought to myself "this is great, but I just spent a bunch of time making Pelican work for me, I'm not going to rip it up and start over." I abandoned web dev many moons ago, so the prospect of spending more time working on my site infrastructure instead of writing content was not appealing. However, Zola stayed in the back of my mind because it seemed to promise alleviating some of the awkwardness I was experiencing with Pelican.

Now, obviously my dreams of writing content didn't materialize. I was hired on at [Planet](https://www.planet.com/), I moved, and I have been setting up a shop in the garage space I'm renting. However, my Pelican pains had not alleviated. While I hadn't generated any new content, I had attempted to migrate the old content from my WordPress blog at [logansmith.org](logansmith.org). What I ran into was an organization problem. I wanted to put the images that go with each post in the same folder as the markdown document. With Pelican, this was not super easy. With Zola, very easy.

So, a few weeks ago, I finally sat down with the intent of adding some new content to my site and decided to make the switch. It was much less painful than I anticipated. Zola uses [`tera`](https://tera.netlify.app/) as a template engine, which was inspired in part by Jinja2 which is the template engine Pelican uses. So, my HTML templates required minimal refactoring to support `tera`. Most of the changes came about from Zola's section / page representation and directory layout. Instead of storing information in Python files like Pelican (`pelicanconf.py`), Zola uses a TOML document (`config.toml`). Instead of implicit page metadata, Zola uses TOML front matter.

On the tooling front, using Zola is easy. I pulled down the provided docker container, `balthek/zola:0.13.0`, and set up a makefile with targets for `serve` and `build`. I plan to spin my own container for use with GitHub actions which I'll use to commonize my build and deploy infrastructure, but that can come later. One benefit of Zola is that it's a single executable, no Python needed. While I love Python, this fact made it simple to get everything running quickly and simplified by GitHub actions pipeline.

On the content front - there will be more of it! I'm finally getting around to the original intent of this site: publishing my notes. It's still very much a work in progress but there will start to be pages published under `/notes`, for example, [`/notes/sysadmin`](@/notes/sysadmin/index.md). These "notes" pages will be very informal and are likely to change (add / remove content). I have an idea of a "man" page equivalent for each page that is more stable, organized, and well thought out. That will probably be a while, I want to stick with "notes" while I get my thoughts organized and collect the extensive amount of documentation I've built up over the years.

<!-- TODO: Replace with shortcode -->
<div class="flash mt-3">
	<i class="octicon fas fa-exclamation-triangle mr-2"></i>The postings on this site are my own and do not represent Planet Labs Inc’s positions, policies, strategies or opinions. 
</div>
