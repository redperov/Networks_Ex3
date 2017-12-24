class HttpRequest(object):
    """
    The class represents an HTTP request.
    Keeps the necessary values in an organized form.
    """

    def __init__(self, raw_request):
        """
        Constructor.
        :param raw_request: HTTP request in a string representation.
        """
        split_request = raw_request.split('\r\n')
        request_line = split_request[0].split(' ')

        # Set url value.
        self._url = request_line[1][1:]

        # Set HTTP type value.
        self._http_type = request_line[2]
        self._headers = {}

        # Save all the headers in a dictionary.
        for header in split_request[1:]:

            # Check that header
            if ':' in header:
                split_header = header.split(': ', 1)
                self._headers[split_header[0]] = split_header[1]

    def get_url(self):
        """
        Url getter.
        :return: url
        """
        return self._url

    def set_url(self, url):
        """
        Url setter.
        :param url: url
        :return: None
        """
        self._url = url

    def get_http_type(self):
        """
        HTTP type getter.
        :return: HTTP type
        """
        return self._http_type

    def get_header(self, header_name):
        """
        Header value getter.
        :param header_name: header name
        :return: header value
        """
        # Check if header exists in the dictionary.
        if header_name in self._headers:
            return self._headers[header_name]
        else:
            return None

    def is_static_request(self):
        """
        Checks if the request is static.
        :return: boolean
        """
        return self._url.startswith("Files")

    def is_dynamic_request(self):
        """
        Checks if the request is dynamic
        :return: boolean
        """
        return self._url.startswith("homepage")


class HttpResponse(object):
    def __init__(self, http_type, status_code, last_modified, data):
        self._http_type = http_type
        self._status_code = status_code
        self._last_modified = last_modified
        # self.content_type = content_type
        self._data = data

    def __str__(self):
        switcher = {
            200: "OK",
            304: "Not Modified",
            404: "Not Found"
        }
        status_text = switcher.get(self._status_code)

        if self._data is None:
            self._data = ''

        response = '{0} {1} {2}\r\nLast-Modified: {3}\r\n\r\n{4}'.format(self._http_type,
                                                                         self._status_code,
                                                                         status_text,
                                                                         self._last_modified,
                                                                         self._data)
        return response
