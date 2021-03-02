TODO

- [ ] Rename templates - `page.html` should be something to do with blogs, maybe `post.html`; `static.html` -> `page.html`
- [ ] Primer dark theme
	+ [ ] Button to switch theme
	+ [ ] Cookie to remember this setting (gah, then I'm back to needing a cookie consent)
- [ ] Redirect dev.* HTTP to HTTPS
- [ ] Re-implement lazy-load
- [ ] Port all existing posts to zola version
- [ ] Add macros for "notice", "warning", etc. GH blocks
- [ ] Write post on port to zola
- [ ] 404 doesn't work on dev.logansnotes.com for some reason
- [ ] Update copyright to include oldest post to 2021
- [ ] Remove origin/dev/zola-migration
- [ ] Start using GH PR (will automate branch removal, tie it to the dev.logansnotes.com deploy action TBD)
- [ ] Handle redirecting `<year>/` URL to home (or make years taxonomy entries?)
- [ ] Add index page for `/notes/`


Could probably use `{% set section = get_section(path="blog/_index.md") %}` to automatically set up menu pages if I wanted (or `{% set section = get_section(path="blog/_index.md", metadata_only=true) %}`). [ref](https://www.getzola.org/documentation/templates/overview/)

[Zola CLI](https://www.getzola.org/documentation/getting-started/cli-usage/)


Potential pages:

- GNU linker
- GCC
- u-boot
- SWD
- Bare metal
	+ AM335
	+ Cortex M
- Kconfig
- GDB
- Device tree
- Meson
- ufw
- tmux
- bash
	+ Basics
	+ Scripting
	+ Customization (prompt, bashrc, etc.)
- sysadmin
	+ netplan
	+ Unifi / EdgeOS / AirOS


Old styles / scripts from when I was working on WaveDrom / supported LazyLoad (LL will eventually be added back).

```
	<!-- WaveDrom -->
	{# <script src="https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.3.2/skins/default.js" type="text/javascript"></script> #}
	{# <script src="https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.3.2/wavedrom.min.js" type="text/javascript"></script> #}

	<!-- LazyLoad -->
	{# <script src="https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.2.0/lazysizes.min.js" integrity="sha256-h2tMEmhemR2IN4wbbdNjj9LaDIjzwk2hralQwfJmBOE=" crossorigin="anonymous"></script> #}
```