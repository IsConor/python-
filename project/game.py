'''
 2048 游戏核心算法
'''

class game:
    def __init__(self,map):
        self.map = map
    def print_list(self):
        for item in range(len(self.map)):
            print(self.map[item], end="\n")
        print()
    def zero_to_end(self,list_test):
        '''
                将数字左移，0放到末尾
            :param list_test:
            :return:
            '''
        for item in range(-1, -len(list_test) - 1, -1):
            if list_test[item] == 0:
                del list_test[item]
                list_test.append(0)
        return list_test

    def add_node(self,list_test):
        '''
            将列表相邻的相同元素做加法，将0移到末尾
        :param list_test:
        :return:
        '''
        list_test = self.zero_to_end(list_test)
        for item in range(len(list_test) - 1):
            if list_test[item] == list_test[item + 1]:
                list_test[item] += list_test[item + 1]
                del list_test[item + 1]
                list_test.append(0)
        return list_test

    def move_left(self):
        '''
            左移
        :return:
        '''
        for item in self.map:
            self.add_node(item)

    def move_right(self):
        '''
            右移
        :return:
        '''
        for line in self.map[::-1]:
            line[::-1] = self.add_node(line)

    def chang_list(self,list_demo):
        for row in range(1, len(list_demo)):
            for col in range(row, len(list_demo[row])):
                list_demo[row - 1][col], list_demo[col][row - 1] = list_demo[col][row - 1], list_demo[row - 1][col]

    def move_up(self):
        self.chang_list(self.map)
        self.move_left()
        self.chang_list(self.map)

    def move_down(self):
        self.chang_list(self.map)
        self.move_right()
        self.chang_list(self.map)

list01 = [
    [2,0,0,2],    #2,4,2,0     2,4,2,0
    [4,4,2,2],    #0,4,4,0     8,0,0,0
    [2,4,0,4],    #0,2,0,2     4,0,0,0
    [0,0,2,2]     #2,2,4,2     4,4,2,0
]

game01 = game(list01)
game01.move_left()
game01.print_list()











#
#
# move_left()
# move_right()
# move_up()
# move_down()