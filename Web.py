import os
import pathlib
# request フォームから送信した情報を扱うためのモジュール
# redirect  ページの移動
# url_for アドレス遷移
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory, render_template,jsonify

import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/name')
def name():
    with open('score.json') as f:
        json_data = json.load(f)

    return jsonify(json_data)

if __name__ == "__main__":
    # 完成したら"debug=True"を消す
    app.run(debug=True)
    
