from http_messages import HttpRequest, HttpResponse
import datetime


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


def handle_request(request):
    http_request = HttpRequest(request)
    resource = None
    status_code = None
    date = str(datetime.datetime.now())

    # Check if the request has an If-Modified-Since header.
    if http_request.get_header("If-Modified-Since") is not None:
        status_code = 304

    elif http_request.get_url() == "favicon.ico":  # favicon.ico request
        status_code = 404

    elif http_request.is_static_request():  # static request

        # Get the path to the resource.
        path = http_request.get_url()

        # Get the resource type.
        # content_type = http_request.get_header("Content-Type")

        # Get the resource data in a string format.
        resource = get_resource(path)

        # Check if resource was found.
        if resource is not None:
            status_code = 200
        else:
            status_code = 404

    else:  # dynamic request
        pass  # TODO implement

    http_response = HttpResponse(http_request.get_http_type(), status_code, date, resource)

    return str(http_response)
