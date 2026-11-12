class Solution {
    public ListNode sortList(ListNode head) {
        if(head==null || head.next==null) return head;

        ListNode s=head, f=head.next;

        while(f!=null && f.next!=null) {
            s=s.next;
            f=f.next.next;
        }

        ListNode middle=s.next;
        s.next=null;

        ListNode first=sortList(head);
        ListNode second=sortList(middle);

        return merge(first,second);
    }

    public ListNode merge(ListNode a,ListNode b) {
        ListNode start=new ListNode(0);
        ListNode curr=start;

        while(a!=null && b!=null) {
            if(a.val<=b.val) {
                curr.next=a;
                a=a.next;
            }
            else {
                curr.next=b;
                b=b.next;
            }
            curr=curr.next;
        }

        if(a!=null) curr.next=a;
        else curr.next=b;

        return start.next;
    }
}