from flask import Flask, render_template, request

app = Flask('portfolio') #name of parent dir

from . import views
