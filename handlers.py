from http_messages import HttpRequest, HttpResponse
import datetime
from articles import get_article


def get_resource(path):
    """
    Gets the data from a static resource.
    :param path: the resource path
    :return: resource
    """
    # Try reading data from the file.
    try:
        with open(path, "rb") as resource:
            data = resource.read()

        return data

    except IOError:
        return None


def handle_static_request(http_request):
    """
    Static request handler.
    :param http_request: HTTP request
    :return: resource
    """
    # Get the path to the resource.
    path = http_request.get_url()

    # Get the resource data in a string format.
    resource = get_resource(path)

    return resource


def find_between(s, first, last):
    """
    Finds a substring between two substrings of a string.
    :param s: the main string
    :param first: the first substring
    :param last: the second substring
    :return: middle substring
    """
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]

    except ValueError:
        return ""


def get_template(path):
    """
    Gets the dynamic template data from a file.
    :param path: template file path
    :return: template
    """
    try:
        with open(path, "rb") as template_file:
            text = template_file.read()

        # Get the template container.
        template_container = find_between(text, '<section id="feature" >', '</section>')

        # Get the template.
        template = find_between(template_container, '<div class="row">', '</div><!--/.row-->')
        template = '<div class="row">' + template + '</div><!--/.row-->'
        return template

    except IOError:
        None


def get_articles(num_of_objects):
    """
    Gets articles according to the number requested.
    :param num_of_objects: number of articles
    :return: articles
    """
    template = get_template("Files/template.html")
    resource = ""

    for i in range(1, num_of_objects + 1):

        temp_template = template

        # Get article with id i
        article = get_article(i)

        # Fill the template with the article's values.
        temp_template = temp_template.replace("Title", article["title"])
        temp_template = temp_template.replace("link", article["link"])
        temp_template = temp_template.replace('img src=""', 'img src="{0}"'.format(article["img"]))
        temp_template = temp_template.replace("Content", article["content"])

        # Add the article to the final result.
        resource += temp_template + '\n'

    return resource


def add_articles_to_file(path, articles):
    """
    Fills the articles in the dynamic template.
    :param path: template file path
    :param articles: articles to insert
    :return: html file with articles
    """
    try:
        with open(path, "rb") as template_file:
            text = template_file.read()

        # Get the template
        template = get_template(path)

        # Replace the template in the text with the articles.
        resource = text.replace(template, articles)

        return resource

    except IOError:
        return None


def handle_dynamic_request(http_request):
    """
    Dynamic request handler.
    :param http_request: HTTP request
    :return: resource
    """
    url = http_request.get_url()
    real_path = "Files/template.html"

    # Check if a static homepage is requested.
    if url == "homepage":
        resource = get_resource(real_path)
        return resource
    else:
        try:
            # Get the id value which was passed as an argument.
            num_of_objects = int(url.split("id=", 1)[1])

            # Check that the number of objects is not out of bounds.
            if num_of_objects < 0 or num_of_objects > 8:
                return None

            # Get the articles.
            articles = get_articles(num_of_objects)

            # Fill the template with the articles.
            resource = add_articles_to_file(real_path, articles)

            return resource

        except ValueError:
            return None


def try_removing_url_query(url):
    """
    Removes query from the url.
    :param url: url
    :return: clean url
    """
    # Check if url contains a query.
    if '?' in url:
        clean_url = url[:url.find('?')]
        return clean_url
    else:
        return url


def handle_request(request):
    """
    User request handler.
    :param request: request
    :return: HTTP response
    """
    http_request = HttpRequest(request)
    resource = None
    status_code = None
    date = str(datetime.datetime.now())

    # Check if the request has an If-Modified-Since header.
    if http_request.get_header("If-Modified-Since") is not None:
        status_code = 304

    elif http_request.get_url() == "favicon.ico":  # if favicon.ico is requested, return 404
        status_code = 404

    elif http_request.is_static_request():  # if a static request

        # Handle static request.
        resource = handle_static_request(http_request)

        # Check if resource was found.
        if resource is not None:
            status_code = 200
        else:
            status_code = 404

    elif http_request.is_dynamic_request():  # if a dynamic request

        # Handle dynamic request.
        resource = handle_dynamic_request(http_request)

        # Check if resource was found.
        if resource is not None:
            status_code = 200
        else:
            status_code = 404

    else:  # if neither

        # Try adding Files/ at the beginning of the url, and test as a static request.
        temp_url = "Files/" + http_request.get_url()
        http_request.set_url(temp_url)

        # Handle a static request.
        resource = handle_static_request(http_request)

        # Check if resource was found.
        if resource is not None:
            status_code = 200
        else:

            # Try removing the query from the url, if it exists.
            temp_url = try_removing_url_query(http_request.get_url())
            http_request.set_url(temp_url)

            # Handle a static request.
            resource = handle_static_request(http_request)

            # Check if resource was found.
            if resource is not None:
                status_code = 200
            else:
                status_code = 404

    http_response = HttpResponse(http_request.get_http_type(), http_request.get_url(), status_code, date, resource)

    return str(http_response)
