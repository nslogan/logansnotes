title: To Do
slug: todo
status: hidden

## Meta

- [ ] Prioritize this list, organize this list (e.g. "infrastructure", "content", "theme", etc.), add "done" (and eventually remove those)

## Inbox

- [ ] Migrate to [Cookie Consent self-hosted](https://github.com/osano/cookieconsent)
- [ ] Dark mode (?)
- [ ] Set Pygments highlighter to match ST3 (Monokai)
- [ ] More advanced code listing
	+ [ ] Line numbers (maybe also clickable line numbers like GH?)
	+ [ ] Select all / copy to clipboard
- [ ] Is there a way to get Pelican to generate directory listings / index, e.g. for 'drafts/posts'; useful to generate theme-matching index
- [ ] Change theme to only list the date, not the time
- [ ] Link settings (e.g. do I want to organize by date, by type (e.g. 'article'), something else?)
- [ ] `gitlfs` for images
- [ ] lazysize / lazyload images
- [ ] Minify CSS, JS assets (using 'finalized' signal, plugin)
- [ ] Move Python dependencies into a pip-virtualenv
	+ [ ] Include plugins / plugin dependencies
- [ ] Use git metadata (https://github.com/getpelican/pelican-plugins/tree/master/filetime_from_git)
- [ ] Other plugins:
	+ [ ] Review: https://github.com/getpelican/pelican-plugins
	+ [ ] 'Asset management'
- [ ] Markdown extensions:
	+ [ ] FA icons
	+ [ ] Automatic title links (e.g. click title to set bar)
	+ [ ] Table of contents generation (?)
- [ ] Look into using a [template](https://docs.getpelican.com/en/stable/settings.html#template-pages) for my about page (?)
- [ ] Add google analytics (eventually)
	+ [ ] `GOOGLE_ANALYTICS`
	+ [ ] Add cookie notice if doing this
- [ ] Think about how to organize images
- [ ] Create custom slugs for posts
- [ ] Change default page width to be slightly smaller, text slightly larger
- [ ] See how this looks on iPhone and iPad
- [ ] How do I manage images in content?
	+ [ ] Consider default size (via CSS)
	+ [ ] How do I manage lazy*
	+ [ ] https://github.com/getpelican/pelican-plugins/blob/master/liquid_tags/Readme.md
	+ [ ] Maybe: https://no-title.victordomingos.com/articles/2018/responsive_images_in_pelican/index.html
	+ [ ] Center images by default - maybe need to wrap them in something...
	+ [ ] https://bitsofco.de/responsive-design-viewport/
- [ ] Modify menu to be responsive at smaller viewport sizes (?)
	+ [ ] https://primer.style/css/utilities/layout
- [ ] Set up sass development environment
	+ [ ] Add Primer
	+ [ ] Convert `style.css` to use Primer sass components

## Done

- [x] Link to LinkedIn in menu
- [x] [Turn off directory indexing](https://security.stackexchange.com/questions/37126/how-secure-is-using-a-blank-index-html-index-php)
- [ ] <s>Use GitHub as CDN for images (?)</s>
