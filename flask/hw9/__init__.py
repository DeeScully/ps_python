from flask import Flask, render_template, request

app = Flask('hw9') #name of parent dir

from . import views
