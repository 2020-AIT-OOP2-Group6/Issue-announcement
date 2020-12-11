import os
import pathlib
from flask import Flask, Blueprint, render_template, request, redirect, url_for, send_from_directory, session
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory, render_template, jsonify

import json


module_play = Blueprint('play', __name__)


@module_play.route("/play", method=['POST'])
def play():

    player_name = request.args.get('pname', None)

    # dict型のデータ
    json_dict = {"pname": p_name, "score": 0}

    with open('score.json') as fr:

        # dict型
        json_data = json.load(fr)

        # dict型のリストに追加
        json_data.append(json_dict)

        # json文字列に変換
        json_string = json.dump(json_data, indent=4)

        with open('score.json') as fw:
            fw.write(json_string)

    return jsonify({
        "message": "名前追加"
    })
