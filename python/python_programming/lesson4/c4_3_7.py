"""辞書包括表記"""
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {x: y for x, y in zip(w, f)}

print(d)