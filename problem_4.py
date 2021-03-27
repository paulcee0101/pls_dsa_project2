class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user): # represented as string ids 
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against

    """
    if user is None or group is None:
        print(
"""Please input valid user or group
NOTE: Program is Terminating..\n"""
        )
        return

    def _user_lookup(user, group, groups):
        if user in group.get_users():
            return True

        else:
            if len(groups) == 0:
                return False

            else:
                first_group = groups[0]
                result = _user_lookup(user, first_group, first_group.get_groups())
                if result is True:
                    return True

                remaining_index = slice(1, None)
                remaining_groups = groups[remaining_index]

                return _user_lookup(user, group, remaining_groups)
                
    return _user_lookup(user, group, group.get_groups())
        
if __name__ == "__main__":
    # Test Case 1
    print("-----------------------------------------TEST CASE 1-----------------------------------------")

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(None, parent)) # returns None
    print(is_user_in_group(sub_child_user, None)) # returns None

    # Test Case 2
    print("-----------------------------------------TEST CASE 2-----------------------------------------")

    super_user = Group("super_user")
    moderators = Group("moderators")
    admins = Group("admins")
    empty1 = Group("empty1")
    empty2 = Group("empty2")

    super_user.add_group(moderators)
    super_user.add_group(admins)

    super_user.add_user("Jane")
    super_user.add_user("John")

    moderators.add_group(empty1)
    moderators.add_group(empty2)

    moderators.add_user("Bob")
    moderators.add_user("Alice")

    admins.add_user("Jack")

    print(is_user_in_group("Jack", super_user)) # returns True

    # Test Case 3
    print("-----------------------------------------TEST CASE 3-----------------------------------------")

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, parent)) # returns True
