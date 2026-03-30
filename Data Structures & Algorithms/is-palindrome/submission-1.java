class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        char[] str = s.toLowerCase().toCharArray();
        while (left < right){
            while (left < right && !Character.isLetterOrDigit(str[left])){
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(str[right])){
                right--;
            }
            if (str[left] != str[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
