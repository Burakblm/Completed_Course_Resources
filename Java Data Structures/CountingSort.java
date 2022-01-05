package bubblesort;

public class CountingSort {
    public static int [] countingSort(int [] dizi ) { 
        int enb  = 0  ;
        int t  ;
        for (int  i = 1 ;i < dizi.length ; i++) {
            if(dizi[i] > dizi[enb])
                enb= i ; 
        }
        int [] b = new int [dizi[enb]+1];
        int [] c = new int [dizi.length] ;
        for(int i = 0 ; i< dizi.length ; i++ ) { 
            int x=dizi[i];
            b[x] += 1 ; 
        }
      
        for (int i = 1 ; i <b.length ; i++) {
            b[i] = b [i] + b[i-1];
             }
        for(int i = (dizi.length-1); i>=0 ; i--) { 
        int k = dizi [i] ; 
        t = b[k];
        c[t -1] = dizi[i];
        }
        return c ; 
    }
    public static void main(String[] args) {
        int [] dizi = {9,1,3,2,14,21,12} ; 
       
        System.out.println("İlk hali : ");
        for(int i : dizi) { 
            System.out.println(i+" ");
        }
        System.out.println("");
        System.out.println("Counting Sort Kullanarak Son Hal : ");
        dizi = countingSort(dizi) ; 
        for(int i=0;i<dizi.length;i++) { 
            System.out.println(dizi[i]+" ");
        }
        
    }
}
