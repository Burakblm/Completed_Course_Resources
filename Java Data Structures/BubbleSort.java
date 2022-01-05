package bubblesort;

public class BubbleSort {
    public static void BubbleSort(int [] dizi) { 
    int n = dizi.length;
    int temp = 0 ; 
    for(int i = 0 ; i< n ; i++) {
        for (int j = 1 ; j < (n-i); j++) {
            if(dizi[j-1] > dizi[j] ){
                temp = dizi[j-1];
                dizi[j-1] = dizi[j]; 
                dizi[j] = temp ; 
            }
            
        }
    }
    
}
    public static void main(String[] args) {
            int dizi[] = {13,602,35,12,45,32,75}; 
            System.out.println("Bubble Sort Hali : ");
                 BubbleSort(dizi);
            for (int i = 0; i < dizi.length; i++) {
                System.out.println(dizi[i] + " ");
        }
    
    }
    
}
