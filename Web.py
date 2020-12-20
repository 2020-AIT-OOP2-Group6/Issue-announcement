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
import Type_Adjust
import Compare

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

    return render_template("game.html", pname=pname, hand0=handstring[0], hand1=handstring[1], hand2=handstring[2], hand3=handstring[3], hand4=handstring[4], ophand0=oppostring[0], ophand1=oppostring[1], ophand2=oppostring[2], ophand3=oppostring[3], ophand4=oppostring[4])


@app.route('/battle', methods=['GET'])
def battle():
    # 外部クラスのインスタンス
    coh = Compare.CompareHand()

    # 自分の手札のリスト
    hand_list = []

    hand_list.append(request.args.get('hand0', None))
    hand_list.append(request.args.get('hand1', None))
    hand_list.append(request.args.get('hand2', None))
    hand_list.append(request.args.get('hand3', None))
    hand_list.append(request.args.get('hand4', None))

    # 関数を呼び出せる形にするためのリスト
    hand_dictionary = []
    for hand in hand_list:
        hand_dictionary.append(Type_Adjust.Adjust(hand))
        pass

    print(coh.check_poker_hand(hand_dictionary))

    # 相手の手札のリスト
    ophand_list = []

    ophand_list.append(request.args.get('ophand0', None))
    ophand_list.append(request.args.get('ophand1', None))
    ophand_list.append(request.args.get('ophand2', None))
    ophand_list.append(request.args.get('ophand3', None))
    ophand_list.append(request.args.get('ophand4', None))

    ophand_dictionary = []
    for ophand in ophand_list:
        ophand_dictionary.append(Type_Adjust.Adjust(ophand))
        pass

    print(coh.check_poker_hand(ophand_dictionary))

    return 


if __name__ == "__main__":
    # 完成したら"debug=True"を消す
    app.run(debug=True)
