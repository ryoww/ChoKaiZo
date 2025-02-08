import customtkinter as ctk
import tkinter as tk  # tkinterの変数（BooleanVar、StringVarなどに使用）
from PIL import Image  # CTkImage用（Pillowが必要）

# 外観モードとカラーテーマの設定
ctk.set_appearance_mode("dark")      # "dark"または"light"
ctk.set_default_color_theme("blue")   # テーマ例："blue", "green", "dark-blue" など

# メインウィンドウの作成
app = ctk.CTk()
app.geometry("800x600")
app.title("CustomTkinter 全メソッドデモ")

# ---------------------------
# Tabviewでタブを作成（複数のウィジェット群を配置）
# ---------------------------
tabview = ctk.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=20, pady=20)
tabview.add("Basic")
tabview.add("Interactive")
tabview.add("Advanced")

# ===========================
# 【Basicタブ】―基本ウィジェット群
# ===========================
basic_tab = tabview.tab("Basic")
basic_frame = ctk.CTkFrame(basic_tab)
basic_frame.pack(fill="both", expand=True, padx=10, pady=10)

# CTkLabelの作成とconfigureメソッドでの更新例
label = ctk.CTkLabel(basic_frame, text="これはCTkLabelです", font=("Arial", 16))
label.pack(pady=10)

# CTkButton：クリックでラベルのテキストを更新
def button_callback():
    label.configure(text="CTkButtonが押されました！")
button = ctk.CTkButton(basic_frame, text="CTkButton", command=button_callback)
button.pack(pady=10)

# CTkEntry：プレースホルダとinsert/get/deleteの使用例
entry = ctk.CTkEntry(basic_frame, placeholder_text="CTkEntryに入力")
entry.pack(pady=10)
entry.insert(0, "初期値")
print("CTkEntry内容:", entry.get())  # コンソールに現在の内容を出力
entry.delete(0, tk.END)  # 全削除

# CTkTextbox：複数行のテキストウィジェット
textbox = ctk.CTkTextbox(basic_frame, width=300, height=100)
textbox.pack(pady=10)
textbox.insert("0.0", "CTkTextboxの初期テキスト\n複数行対応です。")
# ※ 内容取得例: textbox.get("0.0", tk.END)

# ===========================
# 【Interactiveタブ】―操作型ウィジェット群
# ===========================
interactive_tab = tabview.tab("Interactive")
interactive_frame = ctk.CTkFrame(interactive_tab)
interactive_frame.pack(fill="both", expand=True, padx=10, pady=10)

# CTkSlider：スライダーの値が変わるたびにコールバックでラベルを更新
def slider_event(value):
    slider_label.configure(text=f"Slider value: {int(float(value))}")
slider = ctk.CTkSlider(interactive_frame, from_=0, to=100, command=slider_event)
slider.pack(pady=10)
slider.set(50)
slider_label = ctk.CTkLabel(interactive_frame, text="Slider value: 50")
slider_label.pack(pady=5)

# CTkCheckBox：チェック状態の変化でラベル更新
checkbox_var = tk.BooleanVar(value=False)
def checkbox_event():
    if checkbox_var.get():
        checkbox_label.configure(text="チェック済み")
    else:
        checkbox_label.configure(text="未チェック")
checkbox = ctk.CTkCheckBox(interactive_frame, text="CTkCheckBox", variable=checkbox_var, command=checkbox_event)
checkbox.pack(pady=10)
checkbox_label = ctk.CTkLabel(interactive_frame, text="未チェック")
checkbox_label.pack(pady=5)

# CTkRadioButton：複数のラジオボタンの選択でラベル更新
radio_var = tk.StringVar(value="Option 1")
def radio_event():
    radio_label.configure(text=f"選択: {radio_var.get()}")
radio1 = ctk.CTkRadioButton(interactive_frame, text="Option 1", variable=radio_var, value="Option 1", command=radio_event)
radio1.pack(pady=5)
radio2 = ctk.CTkRadioButton(interactive_frame, text="Option 2", variable=radio_var, value="Option 2", command=radio_event)
radio2.pack(pady=5)
radio_label = ctk.CTkLabel(interactive_frame, text="選択: Option 1")
radio_label.pack(pady=5)

# CTkSwitch：オン・オフの切り替えでラベル更新
def switch_event():
    if switch.get():
        switch_label.configure(text="スイッチON")
    else:
        switch_label.configure(text="スイッチOFF")
switch = ctk.CTkSwitch(interactive_frame, text="CTkSwitch", command=switch_event)
switch.pack(pady=10)
switch_label = ctk.CTkLabel(interactive_frame, text="スイッチOFF")
switch_label.pack(pady=5)

# CTkProgressBar：進捗状況を更新（afterメソッドを利用）
progressbar = ctk.CTkProgressBar(interactive_frame)
progressbar.pack(pady=10)
progress_value = 0.0  # 進捗値（0.0〜1.0）
def update_progress():
    global progress_value
    progress_value += 0.01
    if progress_value > 1.0:
        progress_value = 0.0
    progressbar.set(progress_value)  # set()で進捗を更新
    app.after(50, update_progress)
app.after(100, update_progress)

# ===========================
# 【Advancedタブ】―その他・複合ウィジェット群
# ===========================
advanced_tab = tabview.tab("Advanced")
advanced_frame = ctk.CTkFrame(advanced_tab)
advanced_frame.pack(fill="both", expand=True, padx=10, pady=10)

# CTkComboBox：選択肢からの選択でラベル更新
def combobox_callback(choice):
    combo_label.configure(text=f"選択: {choice}")
combobox = ctk.CTkComboBox(advanced_frame, values=["選択肢1", "選択肢2", "選択肢3"], command=combobox_callback)
combobox.pack(pady=10)
combo_label = ctk.CTkLabel(advanced_frame, text="選択: 選択肢1")
combo_label.pack(pady=5)

# CTkOptionMenu：プルダウンメニューからの選択でラベル更新
def optionmenu_callback(choice):
    option_label.configure(text=f"オプション: {choice}")
option_menu = ctk.CTkOptionMenu(advanced_frame, values=["オプション1", "オプション2", "オプション3"], command=optionmenu_callback)
option_menu.pack(pady=10)
option_label = ctk.CTkLabel(advanced_frame, text="オプション: オプション1")
option_label.pack(pady=5)

# CTkScrollableFrame：スクロール可能なフレーム内に多数のウィジェットを配置
scrollable_frame = ctk.CTkScrollableFrame(advanced_frame, width=300, height=150)
scrollable_frame.pack(pady=10)
for i in range(20):
    item_label = ctk.CTkLabel(scrollable_frame, text=f"スクロールアイテム {i+1}")
    item_label.pack(pady=2)

# イベントバインディング：ラベルをクリックしたときの処理
def on_label_click(event):
    advanced_click_label.configure(text="ラベルがクリックされました")
advanced_click_label = ctk.CTkLabel(advanced_frame, text="クリックしてみてください")
advanced_click_label.pack(pady=10)
advanced_click_label.bind("<Button-1>", on_label_click)

# Nested（入れ子）Tabview：Advancedタブ内にさらにタブを配置
nested_tabview = ctk.CTkTabview(advanced_frame, width=300, height=150)
nested_tabview.pack(pady=10)
nested_tabview.add("Tab A")
nested_tabview.add("Tab B")
nested_label_a = ctk.CTkLabel(nested_tabview.tab("Tab A"), text="Nested Tab A の内容")
nested_label_a.pack(pady=10)
nested_label_b = ctk.CTkLabel(nested_tabview.tab("Tab B"), text="Nested Tab B の内容")
nested_label_b.pack(pady=10)

# CTkToplevel：新しいウィンドウを作成する例
def open_new_window():
    new_window = ctk.CTkToplevel(app)
    new_window.geometry("300x200")
    new_window.title("新しいウィンドウ")
    new_label = ctk.CTkLabel(new_window, text="これはCTkToplevelウィンドウです")
    new_label.pack(pady=20)
    close_button = ctk.CTkButton(new_window, text="閉じる", command=new_window.destroy)
    close_button.pack(pady=10)
new_window_button = ctk.CTkButton(advanced_frame, text="新しいウィンドウを開く", command=open_new_window)
new_window_button.pack(pady=10)

# CTkImage：Pillowで作成した画像をウィジェットに設定
try:
    # Pillowで赤い四角形の画像を作成
    img = Image.new("RGB", (100, 100), color="red")
    # CTkImageはlight_image/dark_imageとサイズを指定して作成
    ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(100, 100))
    image_label = ctk.CTkLabel(advanced_frame, image=ctk_image, text="")
    image_label.pack(pady=10)
except Exception as e:
    print("CTkImage作成失敗:", e)

# ---------------------------
# メインループ開始
# ---------------------------
app.mainloop()
