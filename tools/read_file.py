from tkinter import filedialog

files = filedialog.askopenfilenames()


for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.readlines()
    num = contents.index('日付\n')
    print(contents[num+1])

# コメントアウト
#! 重要なコメント
#? 質問事項
#TODO やること
#* ハイライト
