#!/usr/bin/env python
# coding: utf-8

# 對於Heapsort的概念十分的薄弱，將上課資料看完後，觀念是理解了，但程式碼寫不出來，於是繪製了流程圖且參考了http://www.notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php 將其中的程式碼由JAVA改用PYTHON寫出來。
# 對於i層的PARENT，其Index為i，而他的小孩index=2i+1,+2
# 接著用heapify建立規則，使小孩不會大於父母親，若發生就交換
# 接著對所有有孩子的NODE Heapify，以建立MAXheap
# 最後用heapsort排序
# 把第一個node和最後一個node互換位置。
# 假裝刪除第一個最大的node，排入list之中
# 重新對第一個node進行Heapify()。
# 
# 

# In[6]:


class Solution(object):                         #將list內元素交換
    def swap(self,list, a, b) :            
      temp = list[b]
      list[b] = list[a]
      list[a] = temp

    def left_child_index(self,parent):          #left child_index =parent*2+1
        return parent * 2 + 1

    def right_child_index(self,parent):        #right child_index =parent*2+2
        return parent * 2 + 2



    def heapify(self,list, n, i):               #定義堆積
        Max = i                                 #一開始將MAX設置為i，換言之就是parent
        l = self.left_child_index(i)   
        r = self.right_child_index(i)
  

        if l < n and list[i] < list[l]:       #n=len(list)，當L小孩比parent大，Max就改為L小孩 
            Max = l 
   
        if r < n and list[Max] < list[r]:     #當R小孩比parent大，Max就改為R小孩 
            Max = r 
  
        if Max != i:                          #依照HEAPsort的定義，小孩不能比parent大，固有發生此情形必須換位
            self.swap(list,i,Max)  
   
            self.heapify(list, n, Max)        #將list依照規則由上往下掃一遍
    
    def build_Maxheap(self, list, n:int):
        
        last = n-1                          #對所有「具有child的node」進行heapify()
        parents = (last-1)//2              
        for i in range(parents, -1, -1):    
            self.heapify(list, n, i)
    
    
    
    
    def heap_sort(self, list):             #將數列轉換成Max Heap
        
        n = len(list)                     
    
        self.build_Maxheap(list, n)        
    
        for i in range(1,n+1):              
            list.append(list.pop(0))       
            self.build_Maxheap(list, n-i)  
        
        return list
    
    
output=Solution().heap_sort([3,2,5,0,25,6,1,55])
output


# In[ ]:




