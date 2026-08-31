class Solution {
    public int calPoints(String[] operations) {
        ArrayList<Integer> score = new ArrayList<>();

        for (String op : operations){
            if (op.equals("+")){
                int last = score.get(score.size() - 1);
                int second = score.get(score.size() - 2);
                score.add(last + second);
            }
            else if (op.equals("D")){
                int last = score.get(score.size() - 1);
                score.add(last * 2);
            }
            else if (op.equals("C")){
                score.remove(score.size() - 1);
            }
            else{
                score.add(Integer.parseInt(op));
            }
        }
        int sum = 0;
        for (Integer s : score){
            sum += s;
        }
        return sum;
    }
}