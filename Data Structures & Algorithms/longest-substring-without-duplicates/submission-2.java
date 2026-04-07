class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> window = new HashSet<>();
        int L = 0;
        int res = 0;

        for (int R = 0; R < s.length(); R++){
            while (window.contains(s.charAt(R))){
                window.remove(s.charAt(L));
                L++;
            }
            window.add(s.charAt(R));
            res = Math.max(res, R - L + 1);
        }
        return res;
    }
}
