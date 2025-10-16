lst_score = [9, 10, 8, 9, 10, 7, 6, 8, 7, 8]
maxi, mini = max(lst_score), min(lst_score)
# (a)
lst_score.remove(maxi)
# (b)
lst_score.remove(mini)
# (c)
ave = sum(lst_score) / len(lst_score)
print(f'Average score: {ave}')
