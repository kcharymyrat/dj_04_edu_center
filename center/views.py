from django.shortcuts import render

from .models import (
    Category,
    Course,
    NewsFeed,
    Announcement,
)


def home_view(request, *args, **kwargs):
    qs = Course.actives.all()
    return render(request, "center/index.html", {"qs": qs})
