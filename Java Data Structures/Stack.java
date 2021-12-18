package stack;

public class Stack {

    public int maxSize;
    public int[] stackArray;
    public int top;

    public Stack(int maxSize) {
        this.maxSize = maxSize;
        this.stackArray = new int[maxSize];
        this.top = -1;

    }

    public void push(char j) {
        stackArray[++top] = j;
    }

    public int pop() {
        return stackArray[top--];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == maxSize;
    }

}
