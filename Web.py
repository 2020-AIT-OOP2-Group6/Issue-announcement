import pandas
import Compare
import Type_Adjust
import json
import Poker
import Change
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
from app.play import module_play
from app.card import module_change, module_battle
from app.game import module_title, module_next
# from app.play import module_play
app = Flask(__name__)
app.register_blueprint(module_api)
app.register_blueprint(module_play)
app.register_blueprint(module_change)
app.register_blueprint(module_battle)
app.register_blueprint(module_title)
app.register_blueprint(module_next)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # 完成したら"debug=True"を消す
    app.run(debug=False)
