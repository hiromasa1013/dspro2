import requests
from bs4 import BeautifulSoup

def get_temperature():
    # 対象のURL
    url = "https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2024&month=01&day=&view=p1"

    # URLからデータを取得
    response = requests.get(url)

    # ページのHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # 気温データが含まれているテーブルを特定
    table = soup.find('table', {'class': 'data2_s'})

    # テーブルから気温データを取得
    temperatures = []
    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        if len(columns) >= 6:  # カラムが6つ以上ある場合にのみ処理するように修正
            date = columns[0].text.strip()
            temperature = columns[6].text.strip()  # 最後の列に気温データがあると仮定
            temperatures.append((date, temperature))

    return temperatures

if __name__ == "__main__":
    temperature_data = get_temperature()
    for date, temperature in temperature_data:
        print(f"{date}: {temperature}℃")

#気温データ収集１
#ブランチ作成
#マージの確認
#コメント
        
        
        
