package binarytree;

class Node{
    int content;
    Node right;
    Node left;
    Node(int content){
        this.content = content;
        right= null;
        left = null;
    }
}
public class BinaryTree {
    Node root = null;
    public void addTree(int Element){
        Node y = null;
        Node x = root;
        Node z = new Node(Element);
        while(x != null){
            y = x;
            if(Element < x.content)
                x = x.left;
            else
                x = x.right;
        }
        if(y==null)
            root = z;
        else
            if(Element < y.content)
                y.left = z;
            else
                y.right = z;
    }
    
    public Node largestElement(Node n){
        while(n.right != null){
            n = n.right;
        }
        return n;
    }
    public Node smallestElement(Node n){
        while(n.left != null){
            n = n.left;
        }
        return n;
    }
    public boolean search(int Element){
        Node n;
        n = root;
        while(n != null){
            if(n.content == Element)
                return true;
            else
                if(n.content > Element)
                    n = n.left;
                else
                    n = n.right;
        }
        return false;
    }
    
    public void del(int Element){
        root = delete(root,Element);
    }
    
    
    public Node delete(Node root,int Element){
        if(root == null)
            return null;
        
        if(Element < root.content)
            root.left = delete(root.left,Element);
        
        else if(Element > root.content)
            root.right = delete(root.right,Element);
        
        else{
            if(root.left != null && root.right != null){
                Node maxLeft = largestElement(root.left);
                root.content = maxLeft.content;
                root.left = delete(root.left,maxLeft.content);
            }
            
            else if(root.left != null)
                root = root.left;
            
            else if(root.right != null)
                root = root.right;
            
            else
                root = null;
            
        }
        return root;
    }

    public void update(int old_value,int new_value){
        del(old_value);
        addTree(new_value);
    }

    public static void main(String[] args) {
        BinaryTree bt = new BinaryTree();
        bt.addTree(45);
        bt.addTree(23);
        bt.addTree(50);
        bt.del(23);
        bt.addTree(90);
        bt.addTree(54);
        bt.del(45);
        bt.addTree(23);
        bt.addTree(6);
    }
}