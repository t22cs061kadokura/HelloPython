def quick_sort(data):

    #分割できなくなる(リスト要素が1以下)であれば，そのままデータを返す(並べ替えの必要なし)
    if len(data) <= 1:
        return data

    pivot = data.pop(0)     #リストの先頭をピボットとして取り出す

    # ピボットより小さいものでリストを作る
    left = [i for i in data if i <= pivot]
    # ピボットより大きいものでリストを作る
    right = [i for i in data if i > pivot]

    left = quick_sort(left)       #入力に対する左側リストを形成する
    right = quick_sort(right)   #入力に対する右側リストを形成する

    #########再帰しきった結果のみ，quick_sort関数の出力として返される
    #########それ以外のreturnは上のleft = quick_sort(right), left = quick_sort(right)
    return left + [pivot] + right

data = [5,10,13,2,90,4,33,25,17,16]

print(data)
print(quick_sort(data))