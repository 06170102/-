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

# In[50]:


class Solution(object):
    def heapify(self,list, i, n):                                            # n = len(heap) i=root
        largest = i                                                          #一開始將MAX設置為i，換言之就是parent
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n and list[left_index] >list[largest]:             #n=len(list)，當L小孩比parent大，max就改為L小孩 
            largest = left_index
            
        if right_index < n and list[right_index] > list[largest]:          #n=len(list)，當R小孩比parent小，Max就改為R小孩 
            largest = right_index
        if largest != i:
            list[largest], list[i] = list[i], list[largest]               #swap
            self.heapify(list, largest, n)


    def heap_sort(self,list):                                     
        n = len(list)
    
        for i in range(n // 2 - 1, -1, -1):                    #建立MAX heap
            heapify(list, i, n)
  
        for i in range(n - 1, 0, -1):                         #將其排序
            list[0], list[i] = list[i], list[0]
            self.heapify(list, 0, i)
        return list


# In[51]:


output=Solution().heap_sort([3,2,5,0,25,6,1,55])
output


# 以下為minheap

# In[49]:


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
        min= i                                 #一開始將min設置為i，換言之就是parent
        l = self.left_child_index(i)   
        r = self.right_child_index(i)
  

        if l < n and list[i] < list[l]:       #n=len(list)，當L小孩比parent小，min就改為L小孩 
            min = l 
   
        if r < n and list[min] < list[r]:     #當R小孩比parent小，Max就改為R小孩 
            min = r 
  
        if min != i:                          #依照HEAPsort的定義，小孩不能比parent大，固有發生此情形必須換位
            self.swap(list,i,min)  
   
            self.heapify(list, n, min)        #將list依照規則由上往下掃一遍
    
    def build_minheap(self, list, n):
        
        last_index = n-1                          #對所有「具有child的node」進行heapify()
        roots = (last_index-1)//2                  #最後一個Index為n-1       
        for i in range(roots, -1, -1):    
            self.heapify(list, n, i)
    
    
    
    
    def heap_sort(self, list):             #將數列轉換成Max Heap
        
        n = len(list)                     
    
        self.build_minheap(list, n)        
    
        for i in range(1,n+1):              
            list.append(list.pop(0))       
            self.build_minheap(list, n-i)  
        
        return list
    
    
output=Solution().heap_sort([3,2,5,0,25,6,1,55])
output


# In[ ]:




