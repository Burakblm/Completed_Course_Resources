package dfs_code;

public class DFS_code {
    int[][] komsuluk = new int[6][6];
    int[] ziyaret = new int [6];
    Yigit y = new Yigit();
    DFS_code(){
        komsuluk[0][1] = 1;
        komsuluk[0][2] = 1;
        komsuluk[0][3] = 1;
        komsuluk[2][4] = 1;
        komsuluk[3][5] = 1;
        komsuluk[5][2] = 1;
    }
    public void DFS_gez(int dugum){
        int v = dugum;
        System.out.println(v);
        ziyaret[v] = 1;
        
        while(komsuBul(v) != -1 ||  !y.bosMu()){
            if(komsuBul(v) != -1){
                y.push(v);
                v = komsuBul(v);
                ziyaret[v] =1;
                System.out.println(v);
            }else{
                v = y.pop();
            }
                
        }
    }
    public int komsuBul(int dugum){
        for(int i=0;i<6;i++){
            if(komsuluk[dugum][i] != 0 && ziyaret[i] == 0){
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        DFS_code dfs = new DFS_code();
        dfs.DFS_gez(0);
    }
}
