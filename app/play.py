# import os
# import pathlib
# from flask import Flask, Blueprint, render_template, request, redirect, url_for, send_from_directory, session
# # ファイル名をチェックする関数
# from werkzeug.utils import secure_filename
# # 画像のダウンロード
# from flask import send_from_directory, render_template, jsonify

# import json


# module_play = Blueprint('play', __name__)


# @module_play.route("/play", method=['POST'])
# def play():

#     pname = request.args.get('pname', None)


#     return render_template("game.html",pname=pname)
