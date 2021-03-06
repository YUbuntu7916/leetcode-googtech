/*
 * @Author: Goog Tech
 * @Date: 2020-07-16 18:22:02
 * @Description: https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci/
 * @FilePath: \leetcode-googtech\面试题02\#02. 返回倒数第 k 个节点\Solution.java
 */ 

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int kthToLast(ListNode head, int k) {
        // 初始化前继节点与后继节点
        ListNode previous = head;
        ListNode laterNode = head;
        // 后移后继节点,直到与前继节点距离相差为k
        for(int i=0;i<k;i++){
            laterNode = laterNode.next;
        }
        // 同时移动前后继节点,直到后继节点值为空,此时前继节点值即为答案
        while(laterNode!=null){
            laterNode = laterNode.next;
            previous = previous.next;
        }
        return previous.val;
    }
}

/*
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
注意：本题相对原题稍作改动

示例：
输入： 1->2->3->4->5 和 k = 2
输出： 4

说明：
给定的 k 保证是有效的。
*/
