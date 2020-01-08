class cal_cost():
    def __init__(self, length_f, breadth_f):
        self.length_f = length_f
        self.breadth_f = breadth_f

    def cost(self, len_t, bre_f, price):
        total_floor = self.breadth_f * self.length_f
        total_tile = len_t * bre_f
        number_tiles = total_floor / total_tile
        return number_tiles * price


i_cal_cost = cal_cost(20, 20)
print (i_cal_cost.cost(4, 4, 40))
