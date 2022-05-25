import datetime as dt
from django.shortcuts import redirect, render
from django.http import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request, 'news/welcome.html')

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html', {"date":date,})
    
def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html', {"date": date})