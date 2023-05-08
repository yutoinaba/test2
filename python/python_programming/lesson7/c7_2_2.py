"""テキストファイルをテンプレートとして読み込む"""
import string

with open('design/email_template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)