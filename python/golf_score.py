import sys
def read_scores_from_stdin():
    lines = sys.stdin.readlines()
    par_score = list(map(int, lines[0].strip().split(',')))
    player_score = list(map(int, lines[1].strip().split(',')))
    return par_score, player_score
par_score, player_score = read_scores_from_stdin()
score_diff = [player_score[i]-v for i, v in enumerate(par_score)]
score_str = []
# print(score_diff)
for i,v in enumerate(score_diff):
  if player_score[i] == 1:
    if par_score[i] == 5:
      score_str.append("コンドル")
    else:
      score_str.append("ホールインワン")
  elif v == 0:
    score_str.append("パー")
  elif v == -1:
    score_str.append("バーディ")
  elif v == -2:
    score_str.append("イーグル")
  elif v == -3:
    score_str.append("アルバトロス")
  elif v == 1:
    score_str.append("ボギー")
  elif v >= 2:
    score_str.append(f"{v}ボギー")
  else:
    score_str.append(v)
print(",".join(score_str))