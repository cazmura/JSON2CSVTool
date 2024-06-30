import requests
import pandas as pd

# JSONPlaceholder からサンプルのデータを取得する
url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)

# レスポンスのステータスコードをチェック
if response.status_code == 200:
    data = response.json() # JSON データを取得
    print("データを取得しました")

    # JSON データを pandas の DataFrame に変換
    df = pd.DataFrame(data)

    # データの確認※無くてもいい
    print("データのプレビュー")
    print(df.head())

    # DataFrame を CSV 形式で保存
    csv_file_path = 'todos.csv'
    df.to_csv(csv_file_path, index=False)
    print(f"データをCSV形式で{csv_file_path}に保存しました。")

else:
    print("データの取得に失敗しました。ステータスコード:", response.status_code)

# JSONデータを pandas の DataFrame に変換


