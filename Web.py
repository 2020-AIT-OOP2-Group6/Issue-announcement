import os
import pathlib
# request フォームから送信した情報を扱うためのモジュール
# redirect  ページの移動
# url_for アドレス遷移
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory, render_template, jsonify

# 別ファイルのimport
from app.name import module_api
# from app.play import module_play


import json

app = Flask(__name__)

app.register_blueprint(module_api)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play', methods=['POST'])
def play():
    pname = request.form['pname']
    return render_template("game.html",pname=pname)


if __name__ == "__main__":
    # 完成したら"debug=True"を消す
    app.run(debug=True)
