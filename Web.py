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

import Change
import Poker
import json
import Type_Adjust
import Compare
import pandas

app = Flask(__name__)

app.register_blueprint(module_api)

# インスタンス
change_class = Change.ChangeHand()
hand_class = Poker.TrumpGame()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/title', methods=['GET'])
def title():

    pname = request.args.get("pname", None)
    score = request.args.get("result_score", None)

    return render_template("index.html")


@app.route('/play', methods=['POST'])
def play():

    pname = request.form['pname']
    count = 1

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

    return render_template("game.html", pname=pname, hand0=handstring[0], hand1=handstring[1], hand2=handstring[2], hand3=handstring[3], hand4=handstring[4], ophand0=oppostring[0], ophand1=oppostring[1], ophand2=oppostring[2], ophand3=oppostring[3], ophand4=oppostring[4], result_score=0, round_count=1)


@app.route('/next', methods=['GET'])
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

    # print(f'hand:{hand_list}')
    # 関数を呼び出せる形にするためのリスト
    hand_dictionary = []
    for hand in hand_list:
        hand_dictionary.append(Type_Adjust.Adjust(hand))
        pass
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

    pname = request.args.get('pname', None)

    # 勝敗判断
    judge, hand_score = coh.judge_card(hand_dictionary, ophand_dictionary)
    print(judge,hand_score)
    if (judge == 'player'):
        ophand_score = 0
        return jsonify({"hand_score": hand_score}, {"ophand_score": ophand_score}, {"c0": ophand_list[0]}, {"c1": ophand_list[1]}, {"c2": ophand_list[2]}, {"c3": ophand_list[3]}, {"c4": ophand_list[4]}, {"pname": pname})

    else:
        ophand_score = hand_score
        hand_score = 0
        return jsonify({"hand_score": hand_score}, {"ophand_score": ophand_score}, {"c0": ophand_list[0]}, {"c1": ophand_list[1]}, {"c2": ophand_list[2]}, {"c3": ophand_list[3]}, {"c4": ophand_list[4]}, {"pname": pname})


@app.route('/change', methods=['GET'])
def change():
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

    print('hello0')

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

    print('hello1')

    change_card_list = []
    change_card_list.append(request.args.get('num1', None))
    change_card_list.append(request.args.get('num2', None))
    change_card_list.append(request.args.get('num3', None))

    print(change_card_list)

    print('hello2')
    for i, card in enumerate(change_card_list):
        if card == 'null':
            change_card_list[i] = None
        else:
            change_card_list[i] = int(change_card_list[i])

    print('hello3')
    print(change_card_list)

    hand_list, Opponent_list = change_class.change_cards(
        hand_dictionary, ophand_dictionary, change_card_list[0], change_card_list[1], change_card_list[2])
    print('hello4')

    handstring = [d.get('string')for d in hand_list]
    oppostring = [d.get('string')for d in Opponent_list]

    for index, target_list in enumerate(handstring):
        handstring[index] = 'tranp_img/'+target_list+'.png'
    for index, target_list in enumerate(oppostring):
        oppostring[index] = 'tranp_img/'+target_list+'.png'

    return jsonify({"hand00": handstring[0]}, {"hand01": handstring[1]}, {"hand02": handstring[2]}, {"hand03": handstring[3]}, {"hand04": handstring[4]}, {"ophand00": oppostring[0]}, {"ophand01": oppostring[1]}, {"ophand02": oppostring[2]}, {"ophand03": oppostring[3]}, {"ophand04": oppostring[4]})


if __name__ == "__main__":
    # 完成したら"debug=True"を消す
    app.run(debug=False)
