#!/bin/bash
ps aux | grep uwsgi | grep django | awk '{print $2}'|xargs kill -9
/usr/local/bin/uwsgi -x /home/f1/django_uwsgi.xml > /home/f1/django.log 2>&1 &
