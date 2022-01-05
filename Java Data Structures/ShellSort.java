public class ShellSort {

    public static void shellsort(int dizi[]) {
        int n = dizi.length;
        for (int gap = n / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i++) {
                int key = dizi[i];
                int j = i;
                while (j >= gap && dizi[j - gap] > key) {
                    dizi[j] = dizi[j - gap];
                    j -= gap;
                }
                dizi[j] = key;
            }
        }
    }

    public static void main(String[] args) {
        int[] dizi = {9, 14, 3, 2, 43, 11, 58, 22};
        shellsort(dizi);
        System.out.println("Selection Sort Hali : ");
        for (int i = 0; i < dizi.length; i++) {
            System.out.print(dizi[i] + " ");

        }
        System.out.println("");
    }
}
