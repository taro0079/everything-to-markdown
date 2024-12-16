from tkinter import Tk, ttk, filedialog, Text
from PIL import Image, ImageTk  # Pillowライブラリを使用
from markitdown import MarkItDown


def select_file(text_box):
    file_path = filedialog.askopenfilename()
    if file_path:
        text_box.delete(0, "end")
        text_box.insert(0, file_path)


def execute(text_box, text_area):
    markitdown = MarkItDown()
    result = markitdown.convert(text_box.get())
    text_area.insert("1.0", result.text_content)


root = Tk()
root.title("awesome converter to markdown")

# 画像を読み込み、小さくリサイズ
original_img = Image.open("./taro.png")
resized_img = original_img.resize((100, 100))  # 幅100px、高さ100pxにリサイズ
img = ImageTk.PhotoImage(resized_img)

# 画像をラベルとして表示（最上部）
label = ttk.Label(root, image=img)
label.grid(row=0, column=0, columnspan=3, pady=10)  # 画像は一番上、中央に配置

# ファイルパス入力ボックス
entry = ttk.Entry(root, width=40)
entry.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="ew")

# ファイル選択ボタン
file_button = ttk.Button(root, text="Select file", command=lambda: select_file(entry))
file_button.grid(row=1, column=2, padx=10, pady=10)
text_area = Text(root, wrap="word")  # テキストエリアを作成
text_area.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky="ew")

# 実行ボタン
button = ttk.Button(
    root,
    text="EXECUTE (Say thanks to awesome-taro)",
    command=lambda: execute(entry, text_area),
)
button.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky="ew")


root.mainloop()
