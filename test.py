import tkinter as tk  # Tkinterモジュールのインポート

# メインウィンドウの作成
root = tk.Tk()
root.title("簡単なTkinterアプリ")  # ウィンドウのタイトル設定

# ラベルウィジェットを作成してウィンドウに配置
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# イベントループの開始
root.mainloop()
