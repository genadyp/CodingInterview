
/**
Took 19 minutes
*/
class Solution {
    private boolean visit(
        List<List<Integer>> rooms, 
        Set<Integer> keys, 
        Set<Integer> visited, 
        int currentRoom) {
        
        visited.add(currentRoom);
        if (visited.size() == rooms.size()) {
            return true;
        }
        
        List<Integer> currentKeys = rooms.get(currentRoom);
        keys.addAll(currentKeys);
        for (Integer key: currentKeys) {
            if (visited.contains(key)) {
                continue;
            }
            if (visit(rooms, keys, visited, key)) {
                return true;
            }
        }
        return false;
    }
    
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        return visit(rooms, new HashSet<Integer>(), new HashSet<Integer>(), 0);
    }
}