
class Resource(object):

    def __init__(self, title, link, image, content):
        self._title = title
        self._link = link
        self._image = image
        self._content = content

    def get_title(self):
        return self._title

    def get_link(self):
        return self._link

    def get_image(self):
        return self._image

    def get_content(self):
        return self._content

