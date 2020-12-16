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

import Chenge
import Poker
import json

app = Flask(__name__)

app.register_blueprint(module_api)

# インスタンス
chenge_class = Chenge.ChangeHand()
hand_class = Poker.TrumpGame()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/play', methods=['POST'])
def play():
    pname = request.form['pname']

    hand_list, Opponent_list, Decklist = hand_class.reset_draw_cards()

    handstring = [d.get('string')for d in hand_list]
    oppostring = [d.get('string')for d in Opponent_list]
    Decklist = [d.get('string')for d in Decklist]

    for index, target_list in enumerate(handstring):
        handstring[index] = 'tranp_img/'+target_list+'.png'
    for index, target_list in enumerate(oppostring):
        oppostring[index] = 'tranp_img/'+target_list+'.png'
    for index, target_list in enumerate(Decklist):
        Decklist[index] = 'tranp_img/' + target_list + '.png'

    return render_template("game.html", pname=pname, hand0=handstring[0], hand1=handstring[1], hand2=handstring[2], hand3=handstring[3], hand4=handstring[4])

if __name__ == "__main__":
    # 完成したら"debug=True"を消す
    app.run(debug=True)
