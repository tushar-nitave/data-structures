class OverLoading{
    public static void Sum(int a, int b){
        System.out.println("Sum of 2 numbers is: "+(a+b));
    }

    public static void Sum(int a, int b, int c){
        System.out.println("Sum of 3 numbers is: "+(a+b+c));
    }

    public static void main(String args[]){
        Sum(2, 3);
        Sum(1, 2, 3);
    }
}