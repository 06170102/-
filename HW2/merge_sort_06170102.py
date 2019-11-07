#!/usr/bin/env python
# coding: utf-8

# 參考:https://www.c-programming-simple-steps.com/merge-sort.html 由裡面的觀念得知mergesort有兩大步驟
# 1.將List按照中位數切成兩半，分為left跟right，並持續遞迴下去直到len(list)=1，每個list裡只有一個元素。
# 2.接著將各個list連起來，並排出大小。我設立了一個名為result的空list，並將左右的值進行比較，當右邊的值較小，便將其裝入result，右邊的index也延續至下一位，再次比大小，直到兩邊都沒有元素時，便完成merge_sort。
# 分割list的觀念:https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-c15425c12009 從網站複習了一遍LIST，得知python裡
# list[:2] 表示index0-1 list [2:] 表示index2-最後，且不包括結尾。

# In[1]:


class Solution(object):
    def merge(self,left,right):
        result = []
        while len(left) > 0 or len(right) > 0:       #當左list或右list裡面還有元素時，開始以下關係 
            if len(left) > 0 and len(right) > 0:     #當兩邊還有元素進行比較
                if left[0] <= right[0]:              #當左邊的第一位比右邊小，將他排入result，且刪除，遞補下一位
                    result.append(left.pop(0))       #反之
                else:
                    result.append(right.pop(0))      
            elif len(left) > 0:                     #當一邊沒元素，直接裝入result
                result.append(left.pop(0))
            elif len(right) > 0:
                result.append(right.pop(0))
        return result

    def merge_sort(self,list):
        if len(list) <= 1:
            return list
        else:
            N = len(list)//2               #中位數
            left = Solution().merge_sort(list[:N])     #將list由中位數分割為left,right，且遞迴下去
            right = Solution().merge_sort(list[N:])
            return Solution().merge(left, right)



# In[5]:


output= Solution().merge_sort([9,8,1,10,-5,3,2])
output


# In[4]:





# 以下為學習歷程:

# In[72]:


a=[9,5,1,3,2]
print(a[:2],a[2:])
n=len(a)//2
print(a[:n],a[n:])

def cut(list):
        if len(list) <= 1:
            return list
        else:
            N = len(list)//2               
            left = cut(list[:N])    
            right = cut(list[N:])
            return (left, right)

print(cut(a))


# In[75]:


l=[1,5,4,3]
r = [9,8,5,3,4]
final=[]
if l[0]<r[0]:
    final.append(l[0])
else:
    final.append(r[0])
print(final)


# In[ ]:




