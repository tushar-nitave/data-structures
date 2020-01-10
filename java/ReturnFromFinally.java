/*

The finally block gets executed when the try block exits. Even when we
attempt to exit within the try block (via a return statement, a continue statement, a break statement
or any exception), the finally block will still be executed.

**Note that there are some cases in which the finally block will not get executed, such as the following:
- If the virtual machine exits during try/ catch block execution.
- If the thread which is executing during the try/ catch block gets killed.

**/

public class ReturnFromFinally{
    
    public void division(double denominator){
        double output;
        try{
            if(denominator == 0){
                throw new ArithmeticException();
            }
            output = 100/denominator;
            System.out.println("Division: "+output);
            return;
        }catch(ArithmeticException e){
            System.out.println("Exception: "+e);
        }finally{
            System.out.println("Successfull");
        }
    }

    public static void main(String args[]){
        ReturnFromFinally obj = new ReturnFromFinally();
        obj.division(10);
    }
}