
package bubblesort;

public class InsertionSort {
    public static void insertionSort(int dizi[]) {
        int n= dizi.length;
        for(int j=1;j<n;j++){
            int key = dizi[j];
            int i = j-1;
            while((i>-1)&&(dizi[i]>key)){
                dizi[i+1] = dizi[i];
                i--;
            }
            dizi[i+1] = key;
        }
    }
    public static void main(String[] args) {
        int dizi[] = {13,602,35,12,45,32,75};
        insertionSort(dizi);
        for(int i=0;i<dizi.length;i++){
            System.out.println(dizi[i]);
        }
    }
}
