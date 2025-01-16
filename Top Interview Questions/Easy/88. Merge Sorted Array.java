class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int indx1=0;
        int indx2=0;
        int[] res= new int[n+m];
        for(int i=0;i<n+m;i++){
            if(indx2>=n){
                res[i] = nums1[indx1];
                indx1++;
                continue;
            }else if(indx1>=m){
                res[i] = nums2[indx2];
                indx2++;
            }else{
            if(indx1<m&&nums1[indx1]<nums2[indx2]){
            res[i]=nums1[indx1];
            indx1++;
                }else{
                
                  res[i]=nums2[indx2];
                  indx2++;
                }
            
        }}
        for(int i=0;i<n+m;i++){
            nums1[i]=res[i];
        }
    }
}