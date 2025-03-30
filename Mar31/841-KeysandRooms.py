class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = []
        n = len(rooms)
        visit = set()

        def visitRoom(roomIndex, count):

            visit.add(roomIndex)
            if n == len(visit):
                return True

            ret = False
            for room in rooms[roomIndex]:
                if room not in visit:
                    ret |= visitRoom(room, count + 1)

                    if True == ret:
                        return True
            return ret

        return visitRoom(0, 1)
