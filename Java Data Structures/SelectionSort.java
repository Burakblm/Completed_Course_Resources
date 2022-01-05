package bubblesort;

public class SelectionSort {

    public static void selectionSort(int[] dizi) {
        for (int i = 0; i < dizi.length - 1; i++) {
            int index = i;
            for (int j = i + 1; j < dizi.length; j++) {
                if (dizi[j] < dizi[index]) {
                    index = j;
                }
            }
            int enkucuksayi = dizi[index];
            dizi[index] = dizi[i];
            dizi[i] = enkucuksayi;
        }
    }

    public static void main(String[] args) {
        int dizi[] = {13, 602, 35, 12, 45, 32, 75};
        selectionSort(dizi);
        for (int i = 0; i < dizi.length; i++) {
            System.out.println(dizi[i]);
        }
    }
}