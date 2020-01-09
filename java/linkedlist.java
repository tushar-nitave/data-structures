import java.util.LinkedList;
import java.util.Iterator;

public class linkedlist{
    public static void main(String args[]){
        LinkedList<String> ll =  new LinkedList<String>();
        ll.add("First");
        ll.addFirst("Second");
        ll.add("Third");

        Iterator<String> iter = ll.iterator();

        while(iter.hasNext()){
            System.out.println(iter.next());
        }

    }
}