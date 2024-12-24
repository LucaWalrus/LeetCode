class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)

        list = []

        for char in x:
            list.append(char)

        inizio = 0
        fine = -1
        true_count = 0
        for item in list:
            if list[inizio] == list[fine]:
                true_count += 1
            inizio += 1
            fine -= 1
        if true_count == len(list):
            return True
        else:
            return False
