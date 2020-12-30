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
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, Blueprint
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory, render_template, jsonify
# インスタンス
change_class = Change.ChangeHand()
hand_class = Poker.TrumpGame()
module_title = Blueprint('title', __name__)
module_next = Blueprint('next', __name__)


@module_title.route('/title', methods=['GET'])
def title():
    pname = request.args.get("pname", None)
    score = request.args.get("result_score", None)
    json_dict = {"player_name": pname, "score": int(score)}
    # 空の辞書型のリスト
    dic = []
    with open('score.json') as f:
        json_data = json.load(f)
        json_data.append(json_dict)
        # sortする
        scores_sorted = sorted(
            json_data, key=lambda x: x['score'], reverse=True)
        if len(json_data) < 4:
            for target_list in scores_sorted:
                dic.append(target_list)
        else:
            for i, target_list in enumerate(scores_sorted):
                if i < 3:
                    dic.append(target_list)
            pass
        # dict型をjson文字列に変換
        json_string = json.dumps(dic, indent=4)
        with open('score.json', 'w') as f2:
            f2.write(json_string)
    return render_template("index.html")


@module_next.route('/next', methods=['GET'])
def next_p():
    print('reset')
    pname = request.args.get("pname", None)
    score = request.args.get("score", None)
    round_count = request.args.get("round_count", None)
    hand_list, Opponent_list, Decklist = hand_class.reset_draw_cards()
    handstring = [d.get('string')for d in hand_list]
    oppostring = [d.get('string')for d in Opponent_list]
    Decklist = [d.get('string') for d in Decklist]
    for index, target_list in enumerate(handstring):
        handstring[index] = 'tranp_img/'+target_list+'.png'
    for index, target_list in enumerate(oppostring):
        oppostring[index] = 'tranp_img/'+target_list+'.png'
    for index, target_list in enumerate(Decklist):
        Decklist[index] = 'tranp_img/' + target_list + '.png'
    return render_template("game.html", pname=pname, result_score=score, hand0=handstring[0], hand1=handstring[1], hand2=handstring[2], hand3=handstring[3], hand4=handstring[4], ophand0=oppostring[0], ophand1=oppostring[1], ophand2=oppostring[2], ophand3=oppostring[3], ophand4=oppostring[4], round_count=round_count)
