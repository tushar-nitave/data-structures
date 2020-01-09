class InsertIntoSortedList{
    Node head;
    public static class Node{
        int data;
        Node next;
       
        public Node(int data){
            this.data = data;
            this.next = null;
        }
    }

    public  void push(int data){
        Node new_node = new Node(data);
        new_node.next = head;
        head = new_node;
    }

    public void insertSorted(int data){
        Node new_node = new Node(data);

        if(this.head == null){
            new_node.next = head;
            head = new_node;
        }

        else if(this.head.data >= new_node.data){
            new_node.next = head;
            head = new_node;
        }

        else{
            Node current = this.head;
            while (current.next != null && current.next.data < new_node.data){
                current = current.next;
            }
            new_node.next = current.next;
            current.next = new_node;
        }
    }

    public void display(){
        Node start = this.head;
        while(start != null){
            System.out.print(start.data+"->");
            start = start.next;
        }
    }

    public static void main(String args[]){
        InsertIntoSortedList obj = new InsertIntoSortedList();
        obj.push(3);
        obj.push(2);
        obj.push(1);
        obj.display();
        obj.insertSorted(4);
        System.out.println("\n");
        obj.display();
    }
}