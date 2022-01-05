
package dfs_code;

public class Yigit {
    int[] yigit = new int[10];
    int top = -1;
    
    int pop(){
        if(!bosMu()){
            return yigit[top--];
        }
        else{
            System.out.println("yigit bos");
            return -1;
        }
    }
    void push(int eleman){
        if(!doluMu()){
            yigit[++top] = eleman;
        }
        else{
            System.out.println("yigit dolu");
        }
    }
    
    boolean bosMu(){
        return top == -1;
    }
    
    boolean doluMu(){
        return top == 9;
    }
}
