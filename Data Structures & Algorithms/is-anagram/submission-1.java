class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!map1.containsKey(s.charAt(i))) {
                map1.put(s.charAt(i), 0);
            } else {
                map1.put(s.charAt(i), map1.get(s.charAt(i)) + 1);
            }
        }
        for (int i = 0; i < t.length(); i++) {
            if (!map2.containsKey(t.charAt(i))) {
                map2.put(t.charAt(i), 0);
            } else {
                map2.put(t.charAt(i), map2.get(t.charAt(i)) + 1);
            }
        }
        for (char key : map1.keySet()) {
            if (!map1.get(key).equals(map2.get(key))) {
                return false;
            }
        }
        for (char key : map2.keySet()) {
            if (!map2.get(key).equals(map1.get(key))) {
                return false;
            }
        }
        return true;
    }
}
