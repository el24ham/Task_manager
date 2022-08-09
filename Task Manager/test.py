from datetime import datetime
import operator

# dict1={1: ["2022/9/10", "2022/9/20", 'project', 'elham'],
#        2: ["2022/1/2", "2022/3/4", 'p2', 'elham'], 
#        3: ["2022/7/12", "2022/8/19", 'idk', 'fazel'],
#        5: ["2022/10/5", "2022/10/26", 'ttt', 'ooo'], 
#        6: ["2022/9/12","2022/10/5", 'nnn', 'fazel'],
#        8: ["2022/10/10", "2024/11/12", 'koft', 'mamad'],
#        10: ["2022/8/25", "2022/8/31", 'ooo', 'lll'], 
#        11: ["2022/8/12", "2022/8/13", 'uiui', 'zizii'], 
#        12: ["2022/9/15", "2022/9/16", 'ooo', 'mmm'], 
#        13: ["2022/8/25", "2022/8/26", 'kkk', 'jjj'], 
#        14: ["2022/8/31", "2022/9/2", 'lll', 'ffff']}

dict1={1: [datetime.date(2022, 9, 10), datetime.date(2022, 9, 20), 'project', 'elham'],
       2: [datetime.date(2022, 1, 2), datetime.date(2022, 3, 4), 'p2', 'elham'], 
       3: [datetime.date(2022, 7, 12), datetime.date(2022, 8, 19), 'idk', 'fazel'],
       5: [datetime.date(2022, 10, 5), datetime.date(2022, 10, 26), 'ttt', 'ooo'], 
       6: [datetime.date(2022, 9, 12),datetime.date(2022, 10, 5), 'nnn', 'fazel'],
       8: [datetime.date(2022, 10, 10), datetime.date(2024, 11, 12), 'koft', 'mamad'],
       10: [datetime.date(2022, 8, 25), datetime.date(2022, 8, 31), 'ooo', 'lll'], 
       11: [datetime.date(2022, 8, 12), datetime.date(2022, 8, 13), 'uiui', 'zizii'], 
       12: [datetime.date(2022, 9, 15), datetime.date(2022, 9, 16), 'ooo', 'mmm'], 
       13: [datetime.date(2022, 8, 25), datetime.date(2022, 8, 26), 'kkk', 'jjj'], 
       14: [datetime.date(2022, 8, 31), datetime.date(2022, 9, 2), 'lll', 'ffff']}
my_list = list(dict1.items())
print(my_list[0][1])
# sort_orders = sorted(dict1.items(), key=lambda item: item[1][1])
# sort_orders=sorted(dict1.items(), key=lambda item: item[1])
# print(sort_orders)