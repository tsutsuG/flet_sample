import flet as ft
from abc import ABC, abstractmethod

class MyControl(ABC):
    def __init__(self, label:str, hint_text:str, width:int, value:int):
        self.label = label
        self.hint_text = hint_text
        self.width = width
        self.value = value
        self.control = None

    @abstractmethod
    def get_value(self) -> int:
        """コントロールの値を取得するメソッド"""
        pass
    
class MyControls:
    def __init__(self):
        self.my_controls = []
    
    def add(self, my_control:MyControl) -> None:
        self.my_controls.append(my_control)

    def get_controls(self) -> list:
        controls = []
        for my_control in self.my_controls:
            controls.append(my_control.control)
        
        return controls

class MyDropDown(MyControl):
    def __init__(self, label:str, hint_text:str, width:int, options:list[int], value:int):
        super().__init__(label, hint_text, width, value)

        # Dropdown 項目設定
        self.options = []
        for option in options:
            self.options.append(ft.dropdown.Option(str(option)))

        # Dropdown インスタンス
        self.control = ft.Dropdown(
            label=self.label,
            hint_text=self.hint_text,
            options=self.options,
            width=self.width,
            value=self.value,
            on_change=self.on_change_dropdown
        )

    def on_change_dropdown(self, e) -> None:
        print(f"{self.label}の選択: {self.control.value}")
    
    def get_value(self) -> int:
        return self.control.value

class MyTextField(MyControl):
    def __init__(self, label:str, hint_text:str, width:int, value:int):
        super().__init__(label, hint_text, width, value)

        # TextField インスタンス
        self.control = ft.TextField(
            label=self.label,
            hint_text=self.hint_text,
            width=self.width,
            value = self.value
        )

    def get_value(self) -> int:
        return self.control.value

def main(page: ft.Page):
    # 1行分のコントロール情報を登録
    text = ft.Text(value="XXX機能")
    my_controls = MyControls()
    my_controls.add(MyDropDown("プルダウン1", "項目を選択", 150, [1, 2, 3], 3))
    my_controls.add(MyDropDown("プルダウン2", "項目を選択", 150, [4, 5, 6], 4))
    my_controls.add(MyTextField("テキスト1", "値を入力", 150, 10))
    
    # コントロールを横に並べる
    row = ft.Row(
        controls=my_controls.get_controls(),
        spacing=20,  # プルダウン同士の間隔
    )

    # ページにコンポーネントを追加
    page.add(text, row)

# アプリケーションを実行
ft.app(target=main)
