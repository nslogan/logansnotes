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
- [WIP] Add index page for `/notes/`
- [ ] Add "console" syntax highlighting
	+ A lot of my examples are going to involve showing shell interactions, `bash` highlighting doesn't meet my needs.
	+ GH uses [this](https://github.com/atom/language-shellscript/blob/cad2413dc1b0b61f75f49dfae9e52a39e519f43d/grammars/shell-session.cson)
	+ [Set of grammars used by Linguist](https://github.com/github/linguist/tree/master/vendor/grammars)
	+ Context is `text.shell-session`
	+ [`ShellSession`](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml#L5321)
	+ [Zola sort_by source](https://github.com/getzola/zola/blob/1ef8c85f53b4988fdafc0e6271cce590515d55aa/components/library/src/library.rs)

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