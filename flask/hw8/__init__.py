from flask import Flask, render_template, request

app = Flask('hw8') #name of parent dir

from . import views
