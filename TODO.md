TODO

- [ ] Primer dark theme
	+ [ ] Button to switch theme
	+ [ ] Cookie to remember this setting (gah, then I'm back to needing a cookie consent)
- [ ] Redirect dev.* HTTP to HTTPS
- [ ] Re-implement lazy-load
- [ ] Port all existing posts to zola version
- [ ] Add macros for "notice", "warning", etc. GH blocks
- [ ] Write post on port to zola
- [ ] 404 doesn't work on dev.logansnotes.com for some reason


Could probably use `{% set section = get_section(path="blog/_index.md") %}` to automatically set up menu pages if I wanted (or `{% set section = get_section(path="blog/_index.md", metadata_only=true) %}`). [ref](https://www.getzola.org/documentation/templates/overview/)

[Zola CLI](https://www.getzola.org/documentation/getting-started/cli-usage/)