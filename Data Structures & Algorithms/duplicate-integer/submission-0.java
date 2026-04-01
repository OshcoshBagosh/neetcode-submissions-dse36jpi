class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> ht = new HashSet<Integer>();

        for(int i = 0; i < nums.length; i++){
            if (ht.contains(nums[i])){
                return true;
            }
            else{
                ht.add(nums[i]);
            }
        }
        return false;
    }
}
