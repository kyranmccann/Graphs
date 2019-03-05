import random
from itertools import combinations
from collections import deque


class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"self.name"

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """

        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)


    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f'User {i + 1}')
        # Create friendships
        possible_friendships = list(combinations(range(1, numUsers + 1), avgFriendships))
        random.shuffle(possible_friendships)
        total_friendships = numUsers * avgFriendships
        possible_friendships = possible_friendships[:total_friendships]
        for friendship in possible_friendships:
            self.addFriendship(friendship[0], friendship[1])
        # print(self.friendships)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        visited[userID] = [userID]
        queue = [userID]
        while len(queue) > 0:
            current = queue.pop(0)
            for user in self.friendships[current]:
                if user not in visited:
                    visited[user] = list(visited[current])
                    visited[user].append(user)
                    queue.append(user)
        return visited

    #     for friend in self.users:
    #         if not friend == userID:
    #             path = self.bfs(userID, friend)
    #             if path:
    #                 visited[friend] = path
    #     return visited
    #
    # def bfs(self, start, target):
    #     q = deque()
    #     visited = {}
    #     q.append(start)
    #
    #     while len(q) > 0:
    #         current = q.popleft()
    #         if current not in visited:
    #             visited[current] = current
    #             if current == target:
    #                 return current
    #             for friend in self.friendships[current]:
    #                 q.append(friend)
    #     return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    connections2 = sg.getAllSocialPaths(5)
    connections3 = sg.getAllSocialPaths(10)
    connections4 = sg.getAllSocialPaths(100)
    connections5 = sg.getAllSocialPaths(200)
    connections6 = sg.getAllSocialPaths(233)
    connections7 = sg.getAllSocialPaths(267)
    connections8 = sg.getAllSocialPaths(300)
    connections9 = sg.getAllSocialPaths(400)
    connections10 = sg.getAllSocialPaths(999)
    # print(connections)
    print(len(connections)/1000)
    print(len(connections2)/1000)
    print(len(connections3)/1000)
    print(len(connections4)/1000)
    print(len(connections5)/1000)
    print(len(connections6)/1000)
    print(len(connections7)/1000)
    print(len(connections8)/1000)
    print(len(connections9)/1000)
    print(len(connections10)/1000)
