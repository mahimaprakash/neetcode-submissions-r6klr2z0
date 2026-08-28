class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        HashMap<Character, Integer> hashS = new HashMap<>();
        HashMap<Character, Integer> hashT = new HashMap<>();

        for (int i=0; i < s.length(); i++){
            hashS.put(s.charAt(i), 1 + hashS.getOrDefault(s.charAt(i), 0));
            hashT.put(t.charAt(i), 1 + hashT.getOrDefault(t.charAt(i), 0));
        }
        // for (int i=0; i < s.length(); i++){
        //     if (hashS.get(s.charAt(i)) != hashT.get(s.charAt(i))){
        //         return false;
        //     }
        // }
        // return true;

        return (hashS.equals(hashT));
    }
}
