# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(s):
            str = ""
            for i in s:
                str = i+str
            return str
        s1=""
        s2=""
        cur=l1
        while(cur.next!=None):
            s1=s1+str(cur.val)
            cur=cur.next
        
        s1=s1+str(cur.val)
        s1=reverse(s1)
        cur=l2
        while(cur.next!=None):
            s2=s2+str(cur.val)
            cur=cur.next
        s2=s2+str(cur.val)
        s2=reverse(s2)
        s1=int(s1)
        s2=int(s2)
        s3=s1+s2
        print(s3)
        s3=str(s3)
        s3=reverse(s3)
        ll=ListNode(int(s3[0]))
        cur=ll
        for i in range(1,len(s3)):
            Newnode=ListNode(int(s3[i]))
            cur.next=Newnode
            cur=Newnode

        return ll