

scores = [{'player_name': 'suzuki tarou', 'score': 1500}, {'player_name': 'tanaka zirou',
                                                           'score': 1800}, {'player_name': 'yamaguti kakeru', 'score': 1300}]
scores_sorted = sorted(scores, key=lambda x: x['score'], reverse=True)


print(scores_sorted)
