import os
import pathlib
from flask import Flask, Blueprint, render_template, request, redirect, url_for, send_from_directory, session
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory, render_template, jsonify
import Change
import Poker
import json
import Type_Adjust
import Compare
import pandas
import json
module_play = Blueprint('play', __name__)
# インスタンス
change_class = Change.ChangeHand()
hand_class = Poker.TrumpGame()


@module_play.route("/play", methods=['POST'])
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
