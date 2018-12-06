# OR-Homework
利用 tabu search 去解 Single-Machine Scheduling Problem，目標函式要最小化 total weighted tardiness
	
*****
|Author|歐子毓|
|---|---
|E-mail|a1225johnny@gmail.com

### 程式主架構說明
- 在執行時，要``輸入兩個值``，第一個是iteration要跑幾次，第二個是tabu list的size
- 程式主要分成三部分，一是``變數宣告``，二是主要``tabu search``在跑的for loop，三是跑結果印出來
- 其中，``choice list``是用來存``每一次iteration的最佳解``，最後再一起比較

*****
### 第一部分
* p,d,w list的``第一個元素必須設定為0``，是為了方便用Task_list操作時可以比較直觀
  * 像是T[0] = 1， p[T[0]] = p[1]，就是job1的process time
* ``temp_list``是用來存每次排程內兩兩job互換後，所得到的 ``total weighted tardiness``
* ``choice_list``是用來存每次iteration中，temp_list的最佳解
* ``tabu_list``是一個二維list用來存被設為tabu的兩個job

*****
### 第二部分
* 第一層for loop是用來跑tabu search
* 第二層for loop
    * 第一個for loop在第一次會先計算初始解存在temp[0]，之後temp[0]的值都是前一輪的最佳解，不跟當前那輪做比較
    * 第二個for loop是將目前的排班內，兩兩job做對調，遇到下個for loop是用來跟tabu list做比較，有tabu!標註起來。接著判斷如果有tabu!把temp[i](目標函數值)設很大，使他不會被考慮到;如果是沒tabu則計算他的目標函數值存在temp[i]。最後再將job換回來，才不會改到順序。
    * 再來遇到的判斷式，先看第一層for loop執行幾次。如果是第一次，要把初始解(temp[0])納入比較。第二次之後，不用考慮前一輪最佳解(temp[0])，只需比較交換job後的值。求出來``當輪最佳解``放到``choice[j]``
    * 更新tabu list，並且確認tabu list是否full
    * 把得到最佳目標函式值的兩個job互換，更新T(排班)

### 第三部分
* 比較之前每輪最佳解(choice[j])，求出最好的值(optsol)
* 印出結果和執行時間