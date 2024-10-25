import sys
def read_scores_from_stdin():
    lines = sys.stdin.readlines()
    par_score = list(map(int, lines[0].strip().split(',')))
    player_score = list(map(int, lines[1].strip().split(',')))
    return par_score, player_score
par_score, player_score = read_scores_from_stdin()
score_diff = [player_score[i]-v for i, v in enumerate(par_score)]
score_str = []

score_map = {
  0: "パー",
  -1: "バーディ",
  -2: "イーグル",
  -3: "アルバトロス",
  -4: "コンドル",
  1: "ボギー",
}

for i,v in enumerate(score_diff):
  if player_score[i] == 1:
    if par_score[i] == 5:
      score_str.append("コンドル")
    else:
      score_str.append("ホールインワン")
  elif v >= 2:
    score_str.append(f"{v}ボギー")
  else:
    score_str.append(score_map[v])
print(",".join(score_str))