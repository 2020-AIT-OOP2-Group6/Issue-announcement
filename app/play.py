import os
import pathlib
from flask import Flask, Blueprint, render_template, request, redirect, url_for, send_from_directory, session
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory, render_template, jsonify

import json


module_api = Blueprint('play', __name__)    


@module_api.route("/play")
def play():

