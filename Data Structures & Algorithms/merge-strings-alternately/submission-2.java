class Solution {
    public String mergeAlternately(String word1, String word2) {
        int p1 = 0;
        int p2 = 0;
        int x = word1.length();
        int y = word2.length();
        StringBuilder res = new StringBuilder();

        while (p1 < x && p2 < y){
            res.append(word1.charAt(p1));
            res.append(word2.charAt(p2));
            p1++;
            p2++;
        }
        while (p1 < x){
            res.append(word1.charAt(p1));
            p1++;
        }

        while (p2 < y){
            res.append(word2.charAt(p2));
            p2++;
        }
        return res.toString();        
    }
}