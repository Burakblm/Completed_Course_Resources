
package bfs_code;

public class BFS_code {
    int[][] komsuluk = new int[6][6];
    int ziyaret[] = new int[6];
    Kuyruk k = new Kuyruk();
    
    BFS_code(){
        komsuluk[0][1] = 1;
        komsuluk[0][2] = 1;
        komsuluk[2][3] = 1;
        komsuluk[2][4] = 1;
        komsuluk[3][5] = 1;
        komsuluk[2][5] = 1;
        
    }
    
    void BFS_gez(int dugum){
        int v = dugum;
        System.out.println(v);
        ziyaret[v] = 1;
        k.ekle(v);
        while(!k.kuyrukBosMu()){
            // komşu bul
            for(int i=0;i<6;i++){
                if(komsuluk[v][i] == 1 && ziyaret[i] == 0){
                    k.ekle(i);
                    ziyaret[i] = 1;
                    System.out.println(i);
                }
            }
            v = k.cıkar();
        }
    }
    
    public static void main(String[] args) {
        BFS_code b = new BFS_code();
        b.BFS_gez(0);
    }
}
