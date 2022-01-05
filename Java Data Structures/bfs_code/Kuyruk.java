package bfs_code;

class Node{
    Node next;
    int deger;
    Node(){}
    
    Node(int deger){
        this.deger = deger;
    }
}
public class Kuyruk {
    Node root;
    void ekle(int eleman){
        if(root == null){
            root = new Node(eleman);
        }
        else{
            Node temp = root;
            while(temp.next != null){
                temp = temp.next;
            }
            temp.next = new Node(eleman);
        }
    }
    int cıkar(){
        if(root == null){
            System.out.println("kuyruk boş");
            return -1;
        }
        else{
            int eleman = root.deger;
            root = root.next;
            return eleman;
        }
        
    }
    boolean kuyrukBosMu(){
        return root == null;
    }
    void listele(){
        Node temp = root;
        while(temp != null){
            System.out.println(temp.deger);
            temp = temp.next;
        }
    }
    public static void main(String[] args) {
        Kuyruk k = new Kuyruk();
        k.ekle(0);
        k.ekle(12);
        k.ekle(65);
        k.listele();
        System.out.println("###");
        k.cıkar();
        k.listele();
        
    }
}
