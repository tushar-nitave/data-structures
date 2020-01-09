import java.util.Vector;

// Vector is similar to ArrayList but it is synchronized.

public class vector{
    public static void main(String args[]){
        Vector<String> vector = new Vector<String>();
        vector.add("Tushar");
        vector.add("Nitave");
        System.out.println(vector.get(0)+" "+vector.get(1));
    }
}