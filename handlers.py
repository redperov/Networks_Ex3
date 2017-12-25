from http_messages import HttpRequest, HttpResponse
import datetime
from articles import get_article


def get_resource(path):
    # Try reading data from the file.
    try:
        # # If content type is image.
        # if content_type == "image":
        #     reading_type = "rb"
        # else:
        #     reading_type = "r"
        with open(path, "rb") as resource:
            data = resource.read()

        return data

    except IOError:
        return None


def handle_static_request(http_request):
    # Get the path to the resource.
    path = http_request.get_url()

    # Get the resource data in a string format.
    resource = get_resource(path)

    return resource


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def get_template(path):
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
    template = get_template("Files/template.html")
    resource = ""

    for i in range(1, num_of_objects + 1):
        # Fill the template with the article's values.
        temp_template = template
        article = get_article(i)
        temp_template = temp_template.replace("Title", article["title"])
        temp_template = temp_template.replace("link", article["link"])
        temp_template = temp_template.replace('img src=""', 'img src="{0}"'.format(article["img"]))
        temp_template = temp_template.replace("Content", article["content"])

        # Add the article to the final result.
        resource += temp_template + '\n'

    return resource


def add_articles_to_file(path, articles):

    try:
        with open(path, "rb") as template_file:
            text = template_file.read()

        # Get the template
        template = get_template(path)

        # Replace the template in the text with the articles.
        resource = text.replace(template, articles)  # TODO not sure this will work

        return resource

    except IOError:
        return None


def handle_dynamic_request(http_request):
    url = http_request.get_url()
    real_path = "Files/template.html"

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

            resource = add_articles_to_file(real_path, articles)

            return resource

        except ValueError:
            return None


def handle_request(request):
    http_request = HttpRequest(request)
    resource = None
    status_code = None
    date = str(datetime.datetime.now())

    # Check if the request has an If-Modified-Since header.
    if http_request.get_header("If-Modified-Since") is not None:
        status_code = 304

    elif http_request.get_url() == "favicon.ico":  # TODO if not needed because of the last else, remove it
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
            status_code = 404

    http_response = HttpResponse(http_request.get_http_type(), status_code, date, resource)

    return str(http_response)
