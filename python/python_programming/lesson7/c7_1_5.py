"""ファイルを作成して書き込む"""
f = open('test.txt', 'w')
f.write('Test\n')
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()