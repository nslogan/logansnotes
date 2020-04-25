

# NOTE: I'm not sure if the best place to do this is here or in the python-markdown extension space.

from pelican import signals

from bs4 import BeautifulSoup

def update_img_tag(p_data):
	# Skip non-text content (e.g. images)
	if p_data._content is None:
		return

	content = p_data._content

	soup = BeautifulSoup(content, "lxml")

	for img in soup.find_all('img'):
		# Add "lazyload" class
		img['class'] = img.get('class', []) + ['lazyload']

		# Convert "src" to "data-src"
		img['data-src'] = img['src']
		del img['src']

	p_data._content = soup.decode()

def register():
	signals.content_object_init.connect(update_img_tag)
