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
        self.url = request_line[1][1:]

        # Set HTTP type value.
        self.http_type = request_line[2]
        self.headers = {}

        # Save all the headers in a dictionary.
        for header in split_request[1:]:

            # Check that header
            if ':' in header:
                split_header = header.split(': ', 1)
                self.headers[split_header[0]] = split_header[1]

    def get_url(self):
        """
        Url getter.
        :return: url
        """
        return self.url

    def get_http_type(self):
        """
        HTTP type getter.
        :return: HTTP type
        """
        return self.http_type

    def get_header(self, header_name):
        """
        Header value getter.
        :param header_name: header name
        :return: header value
        """
        # Check if header exists in the dictionary.
        if header_name in self.headers:
            return self.headers[header_name]
        else:
            return None

    def is_static_request(self):
        """
        Checks if the request static.
        :return: boolean
        """
        return self.url.startswith("Files")


class HttpResponse(object):
    def __init__(self, http_type, status_code, last_modified, data):
        self.http_type = http_type
        self.status_code = status_code
        self.last_modified = last_modified
        # self.content_type = content_type
        self.data = data

    def __str__(self):
        switcher = {
            200: "OK",
            304: "Not Modified",
            404: "Not Found"
        }
        status_text = switcher.get(self.status_code)

        if self.data is None:
            self.data = ''

        response = '{0} {1} {2}\r\nLast-Modified: {3}\r\n\r\n{4}'.format(self.http_type,
                                                                         self.status_code,
                                                                         status_text,
                                                                         self.last_modified,
                                                                         self.data)
        return response
