public class Finalize{
      
    public void something(){
        System.out.println("Hello");
    }

    public static void main(String args[]){
        Finalize obj = new Finalize();
        obj.something();
        obj = null;
        // calling garbage collector
        System.gc();
    }

    public void finalize(){
        System.out.println("Finalize is called");
    }

}