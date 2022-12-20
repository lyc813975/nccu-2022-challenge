## 2022 政大電物競賽
---
### 題目說明
給定N個學生之間的磨合指標，分成兩班使得整體的滿意度(E值)盡可能的大。

- [詳細說明](2022_challenge.pdf)
  - [範例題目](w4.txt)
  - [範例班級答案](101_sol_class.txt)
  - [範例E值答案](101_sol_E.txt)
  - [實際題目](w101.txt)

### 解法說明
先從一個初始的分班方法，計算當前分班方式的滿意度，每一回合找出對滿意度貢獻最少的學生轉班，若轉班後的滿意度比轉班前的滿意度，代表抵達local optimum。根據該分班作調整，試著跳脫該local optimum，以抵達global optimum。
- [詳細報告](solution.pdf)
  - [code](solve.py)
  - [輸出班級答案](101_sol_class.txt)
  - [輸出E值答案](101_sol_E.txt)
