class Element{
    int data;
    public Element(int data){
        this.data = data;
    }
}
public class ArrayQueue {
    Element[] array;
    public static int Front;
    public static int Rear;
    int N;
    
    public ArrayQueue(int N){
        array = new Element[N];
        this.N = N;
        Front = 0;
        Rear = 0;
    }
    public boolean queueFull(){
        return (Front == (Rear+1)%N);
    }
    public boolean queueEmpty(){
        return (Front == Rear);
    }
    public void addQueue(Element e){
        if(!queueFull()){
            array[Rear] = e;
            Rear = (Rear+1) % N;
        }
    }
    public Element delQueue(){
        Element result;
        if(!queueEmpty()){
            result = array[Front];
            Front = (Front+1)%N;
            return result;
        }
        return null;
    }
    public static void main(String[] args) {
        ArrayQueue que = new ArrayQueue(6);
        que.addQueue(new Element(1));
        que.delQueue();
        que.addQueue(new Element(3));
        que.delQueue();
        que.addQueue(new Element(4));
        que.addQueue(new Element(5));
        que.delQueue();
        
        for (int i = que.Front; i < que.Rear; i++) {
            System.out.println(que.array[i].data);
        }
        
    }
}

