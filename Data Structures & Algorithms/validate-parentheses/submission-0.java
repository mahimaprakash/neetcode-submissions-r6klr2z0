class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put(']', '[');
        mapping.put('}', '{');

        for (char c: s.toCharArray()){
            if (mapping.containsKey(c)){
                if (!stack.empty() && stack.peek() == mapping.get(c)){
                    stack.pop();
                }
                else{
                    return false;
                }

            }
            else{
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
