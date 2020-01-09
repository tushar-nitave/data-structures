class Animals { 
    // private methods are not overridden 
    public void signature() 
    { 
        System.out.println("I am animal."); 
    } 
  
} 
  
class Dog extends Animals { 
    public void signature() 
    { 
        System.out.println("I am dog."); 
    } 
} 

class Cat extends Animals { 
   
} 
  
// Driver class 
class OverRidding { 
    public static void main(String[] args) 
    { 
        Animals[] animals = new Animals[2];
        Dog dog = new Dog();
        Cat cat = new Cat();
        
        animals[0] = dog;
        animals[1] = cat;

        for(Animals animal: animals){
            animal.signature();
        }
    } 
} 