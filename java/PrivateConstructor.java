/*
Declaring a constructor private on class A means that you can only access the (private) constructor if you
could also access A's private methods. Who, other than A, can access A's private methods and constructor?
A's inner classes can. Additionally, if A is an inner class of Q, then Q's other inner classes can.

This has direct implications for inheritance, since a subclass calls its parent's constructor. The class A can be
inherited, but only by its own or its parent's inner classes.
**/

public class PrivateConstructor{

    private static void PrivateConstructor(int radii){

        System.out.println("Radius: "+(3.14*radii*radii));
    }

    public static void main(String args[]){
        PrivateConstructor obj = new PrivateConstructor();
        obj.PrivateConstructor(10);
    }
}

// This class cannot access private constructor

// class Outside{
//     public static void calculate(int radii){
//         PrivateConstructor obj = new PrivateConstructor();
//         obj.PrivateConstructor(10);
//     }
// }