class Solution {
    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        int flag = 0;
        while (left < right){
            if (s.charAt(left) != s.charAt(right) && flag==0){
                flag++;
            }
            else if (s.charAt(left) != s.charAt(right) && flag==1){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}