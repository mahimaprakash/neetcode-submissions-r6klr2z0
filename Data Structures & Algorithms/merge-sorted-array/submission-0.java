class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = 0;
        int j = 0;
        int idx = 0;
        int[] copy = Arrays.copyOf(nums1, m);
        while (idx < m + n){
            if (j >= n || i < m && copy[i] <= nums2[j]){
                nums1[idx++] = copy[i++];
            }
            else{
                nums1[idx++] = nums2[j++];
            }
        }
    }
}