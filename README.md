使用方式：
這是一款以大學生活為背景所設計出來的狀態
一開始有四個transition 到達個別的四個state:
  1.i wanna play lol(go to state 1)
  2.i wanna dissolve Runestones(go to state 2)
  3.i wanna play a game (go to state 3)
  以上三個會自動回到user state
  4.i wanna graduate(go to state 5)
state 5開始 會先問是否真的想過關
回答home則回到user state
回答yes則繼續遊戲
state 5,6,7,8分別代表成大資工最難pass的四個科目老師的照片 並按照年級排列
回答fail則持續出現同個老師照片
回答pass則繼續往下一關前進
所有關卡都通過後會來到state 9 是一個學士帽的照片
若持續輸入pass則一直停留在學士帽
若輸入home則會回到user state
一切從頭再來一次

pic:
![Imgur](https://i.imgur.com/17jEl27.png)

執行方式：
python3 app.py
