package bidirectionallinkedlist;

import java.util.Scanner;

class Student{
    int number;
    String name;
    String surname;
    Student next;
    Student previous;
    Student(int number,String name,String surname){
        this.number=number;
        this.name= name;
        this.surname = surname;
        next = null;
        previous = null;
    }
}
class LinkedList{
    Student head,end = null;
    
    public boolean isItEmpty(){// we check if the linked list is empty
        return head == null;
    }
    
    public void addToHead(int number,String name,String surname){
        Student std = new Student(number,name,surname);
        if(isItEmpty()){
            end = std;
        }
        else
            head.previous= std;
        std.next= head;
        head = std;
    }
    public void addToEnd(int number,String name,String surname){
        Student std = new Student(number,name,surname);
        if(isItEmpty()){
            head = std;
        }else{
            end.next = std;
            std.previous = end;
        }
        end = std;
    }
    public int numberOfStudents(){
        Student temp = head;
        int j = 1;
        while(temp != null){
            temp = temp.next;
            j++;
        }
        return j;
    }
    public void addToIndex(int number,String name,String surname,int index){
        Student std = new Student(number,name,surname);
        Student temp = head;
        int num_of_std = numberOfStudents();
        int j = 2;
        if(j<=num_of_std){
            while(temp != end){
                if(j == index){
                    std.next = temp.next;
                    temp.next.previous = temp.next;
                    std.previous = temp;
                    temp.next = std;
                    break;
                }
                temp = temp.next;
                j++;
            }
        }
        
        
    }
    public void printToList(){
        Student temp = head;
        while(temp != null){
            System.out.println("number: "+temp.number+" Name: "+temp.name+" Surname: "+temp.surname);
            temp = temp.next;
        }
    }
    public boolean search(int number){
        Student temp = head;
        boolean isitfound = false;
        while(temp != null){
            if(temp.number == number){
                isitfound = true;
                break;
            }
        }
        return isitfound;
    }
    public void deleteHead(){
        Student temp = head;
        if(head.next==null)
            end = null;
        else
            head.next.previous= null;
        head = head.next;
        
    }
    public void deleteEnd(){
        Student temp = head;
        if(head.next == null)
            head = null;
        else
            end.previous.next = null;
        end = end.previous;
        
    }
    public void deleteFromIndex(int index){
        int num_of_std = numberOfStudents();
        Student temp = head;
        int j=1;
        if(index<=num_of_std){
            while(temp != null){
                if(j == index){
                    temp.previous.next = temp.next;
                    temp.next.previous = temp.previous;
                }
                j++;
                temp = temp.next;
            }
        }
    }
}
public class BidirectionalLinkedList {
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
                    Students.addToEnd(num1, name1, surname1);
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
