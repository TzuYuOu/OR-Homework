# OR-Homework
利用 tabu search 去解 Single-Machine Scheduling Problem，目標函式要最小化 total weighted tardiness
	
*****
|Author|歐子毓|
|---|---
|E-mail|a1225johnny@gmail.com

### 程式主架構說明
- 在執行時，要``輸入兩個值``，第一個是iteration要跑幾次，第二個是tabu list的size
- 程式主要分成三部分，一是``變數宣告``，二是主要``tabu search``在跑的for loop，三是跑結果印出來

*****
### 第一部分
* p,d,w list的第一個元素必須設定為0，是為了方便用Task_list操作時可以比較直觀
  * 像是T[0] = 1， p[T[0]] = p[1]，就是job1的process time
* ``temp_list``是用來存每次排程內兩兩job互換後，所得到的 ``total weighted tardiness``
* ``choice_list``是用來存每次iteration中，temp_list的最佳解
* ``tabu_list``是一個二維list用來存被設為tabu的兩個job
