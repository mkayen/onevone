from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world!")
def current_time(request):
    return HttpResponse("<html><body>It is now %s.</body></html>" % datetime.datetime.now())
def hours_ahead(request, os):
    try:
        offset = int(os)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
