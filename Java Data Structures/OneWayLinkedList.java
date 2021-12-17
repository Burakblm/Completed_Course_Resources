package onewaylinkedlist;

import java.util.Scanner;
import javafx.scene.shape.Line;

class Student{
    int number;
    String name;
    String surname;
    Student next;
    
    Student(int number,String name,String surname){
        this.number=number;
        this.name=name;
        this.surname=surname;
        next = null;//every time a new class is created the next will be null
    }
}
class LinkedList{
    Student head,end = null;//first we give null to first and last object
    public void addToHead(int number,String name,String surname){//It is used to add an element to the beginning of the list.
        Student std = new Student(number,name,surname);
        if(end == null){
            head = std;
            end = std;
        }else{
            std.next=head;
            head = std;
        }
    }
    //We add it to the end of the linked list with the addtoend method
    public void addtoEnd(int number,String name,String surname){
        Student std = new Student(number,name,surname);
        if(head == null){
            head = std;
            end = std;
        }else{
            end.next = std;
            end = std;
        }
    }
    public int numberOfStudents(){
        int num_of_std=0;
        Student temp = head;
        while(temp != null){
            temp = temp.next;
            num_of_std++;
        }
        System.out.println(num_of_std);
        return num_of_std;
    }
    void addToIndex(int number,String name,String surname,int index){
        Student std = new Student(number,name,surname);
        int num_of_stud= numberOfStudents();
        int j = 1;
        Student temp = head;
        if(index <= num_of_stud){
            while(temp != null){
                if(j==index){
                    std.next=temp.next;
                    temp.next=std;
                }
                temp = temp.next;
                j++;
            }
        }
        else{
            System.out.println("cannot be inserted");
        }
    }
    // this method prints all the elments of the linked list
    public void printToList(){
        Student temp = head;
        while(temp != null){
            System.out.println("number: "+temp.number+" Name: "+temp.name+" Surname: "+temp.surname);
            temp = temp.next;
        }
    }
    
    public void deleteHead(){// delets the first elements of the linked list
        head = head.next;
        if(head == null){
            end = null;
        }
    }
    
    public void deleteEnd(){
        Student temp,previous;
        temp = head;
        previous = null;
        while(temp != end){
            previous = temp;
            temp = temp.next;
        }
        if(previous == null){
            head = null;
            end = null;
        }else{
            previous.next = null;
            end = previous;
        }
    }
    public void deleteFromIndex(int index){
        Student previous = null;
        int num_of_std = numberOfStudents();
        int j=1;
        Student temp = head;
        if(index<num_of_std){
            while(temp != end){
                previous = temp;
                temp = temp.next;
                j++;
                if(j == index){
                    previous.next= temp.next;
                    break;
                }
            }
        }
        else{
            deleteEnd();
        }
        
    }

}
public class OneWayLinkedList {
    public static void showSelector(){
        System.out.println("0-Exit");
        System.out.println("1-add to head");
        System.out.println("2-add to end");
        System.out.println("3-add index");
        System.out.println("4-list Students");
        System.out.println("5-delete to head");
        System.out.println("6-delete to end");
        System.out.println("7-delete to index");
        System.out.println("8-number of students");
    }
    public static void main(String[] args) {
        Scanner k = new Scanner(System.in);
        boolean isItTrue= true;
        int select= -1;
        LinkedList Students = new LinkedList();
        while(isItTrue){
            showSelector();
            select = k.nextInt();
            switch(select){
                case 0:
                    isItTrue = false;
                    break;
                case 1:
                    System.out.print("enter student number:");
                    int num = k.nextInt();
                    System.out.print("enter Student name:");
                    String name = k.next();
                    System.out.print("enter Student surname:");
                    String surname = k.next();
                    Students.addToHead(num, name, surname);
                    break;
                case 2:
                    System.out.print("enter student number:");
                    int num1 = k.nextInt();
                    System.out.print("enter Student name:");
                    String name1 = k.next();
                    System.out.print("enter Student surname:");
                    String surname1 = k.next();
                    Students.addtoEnd(num1, name1, surname1);
                    break;
                case 3:
                    System.out.print("enter student number:");
                    int num2 = k.nextInt();
                    System.out.print("enter Student name:");
                    String name2 = k.next();
                    System.out.print("enter Student surname:");
                    String surname2 = k.next();
                    System.out.print("enter index:");
                    int index = k.nextInt();
                    Students.addToIndex(num2, name2, surname2,index);
                    break;
                case 4:
                    Students.printToList();
                    break;
                case 5:
                    Students.deleteHead();
                    break;
                case 6:
                    Students.deleteEnd();
                    break;
                case 7:
                    System.out.print("enter index:");
                    int index1 = k.nextInt();
                    Students.deleteFromIndex(index1);
                    break;
                case 8:
                    Students.numberOfStudents();
                    break;
                
            }
        }
        
    }

}
