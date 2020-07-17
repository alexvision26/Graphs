import random
from util import Queue
import time

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        for user in range(num_users):
            self.add_user(user)

        # Add users

        # Create friendships
        friendships = []

        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users + 1):
                friendship = (user, friend)
                friendships.append(friendship)

        self.fisher_yates_shuffle(friendships)

        total_friendships = num_users * avg_friendships

        random_friendships = friendships[:total_friendships//2]

        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def linear_populate_graph(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        for user in range(num_users):
            self.add_user(user)

        target_num_friendships = num_users * avg_friendships

        friendships_created = 0

        while friendships_created < target_num_friendships:

            friend_one = random.randint(1, self.last_id)
            friend_two = random.randint(1, self.last_id)

            friendship_was_made = self.add_friendship(friend_one, friend_two)

            if friendship_was_made:
                friendships_created += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            ln = path[-1]

            if ln not in visited:
                visited[ln] = path

                for n in self.friendships[ln]:
                    new_path = list(path)
                    new_path.append(n)
                    q.enqueue(new_path)

        # print(self.friendships.values())

        return visited


if __name__ == '__main__':
    sg = SocialGraph()

    start_time = time.time()
    sg.populate_graph(1000, 2)
    end_time = time.time()

    print(f"Populate graph O_n^2): {end_time - start_time}")

    start_time = time.time()
    sg.linear_populate_graph(1000, 5)
    end_time = time.time()

    print(f"Populate graph O_n^2): {end_time - start_time}")

    print('finished again!')

    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
