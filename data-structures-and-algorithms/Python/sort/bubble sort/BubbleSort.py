'''
@Author: Goog Tech
@Date: 2020-07-13 14:54:48
@Description: bubble sort
@FilePath: algorithm.show\leetcode-googtech\data-structures-and-algorithms\Python\sort\bubble sort\BubbleSort.py
'''
class BubbleSort:
    
    '''
    @description: 冒泡排序
    @param {alist} 
    @return: 
    '''
    def bubbleSort(self,alist):
        for passnum in range(len(alist)-1,0,-1): # range(start, stop[, step])
            for i in range(passnum):
                if alist[i]  > alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
        print(alist)


    '''
    @description: 短冒泡排序，可判断出是否为有序列表
    @param {type} 
    @return: 
    '''    
    def shortBubbleSort(self,alist):
        exchanges = True
        passnum = len(alist) - 1
        while passnum > 0 and exchanges:
            exchanges = False
            for i in range(passnum):
                if alist[i] > alist[i+1]:
                    exchanges = True
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
            passnum = passnum - 1
        print(alist)


b = BubbleSort()
# [1, 2, 3, 4, 5, 6]
b.bubbleSort([6,5,4,3,2,1])
b.shortBubbleSort([6,5,4,3,2,1])
