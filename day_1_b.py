#!/usr/bin/env python

def finding_entries(expenses, t):
    # at least one value should be lower than t/3, so let's capture that in a list.
    low_list = []
    for i in expenses:
        if i < t / 3:
            low_list.append(i)
    low_list.sort()
    low_list  # [222, 365, 473, 572, 600] 5 values for t == 2020
    lenght = len(low_list)

    # because low_list is sorted, we also know that no value higher than: t - low_list[0] - low_list[1] can be used
    # so let's create the final list that get's rid of those values that are too high as well.
    final_list = []
    for i in expenses:
        if i <= t - low_list[0] - low_list[1]:
            final_list.append(i)
    final_list.sort()  # sort the list again

    # now that we have elimanted all values that are out of the possible range we can deduct every possible
    # combination of 2 values from the list from t. if this outcome is in the final_list we have our third value
    # and we can return the product of these values to get our answer.

    for i in final_list[0:lenght]:
        for e in final_list:
            x = t - (e + i)
            if x in final_list:
                return print (f"The values are {x}, {e} and {i} and the answer is it's product {x * i * e}")



#csv_file = np.genfromtxt('expenses.csv',
                         #delimiter=',', dtype=int)
# expenses = csv_file[:].tolist()
expenses = expenses = [1914, 1931, 1892, 1584, 1546, 1988, 1494, 1709, 1624, 1755, 1849, 1430, 1890, 1675, 1604, 1580, 1500, 1277, 1729, 1456, 2002, 1075, 1512, 895, 1843, 1921, 1904, 1989, 1407, 1552, 1714, 757, 1733, 1459, 1777, 1440, 1649, 1409, 1662, 1968, 1775, 1998, 1754, 1938, 1964, 1415, 1990, 1997, 1870, 1664, 1145, 1782, 1820, 1625, 1599, 1530, 1759, 1575, 1614, 1869, 1620, 1818, 1295, 1667, 1361, 1520, 1555, 1485, 1502, 1983, 1104, 1973, 1433, 1906, 1583, 1562, 1493, 1945, 1528, 1600, 1814, 1712, 1848, 1454, 1801, 1710, 1824, 1426, 1977, 1511, 1644, 1302, 1428, 1513, 1261, 1761, 1680, 1731, 1724, 1970, 907, 600, 1613, 1091, 1571, 1418, 1806, 1542, 1909, 1445, 1344, 1937, 1450, 1865, 1561, 1962, 1637, 1803, 1889, 365, 1810, 1791, 1591, 1532, 1863, 1658, 1808, 1816, 1837, 1764, 1443, 1805, 1616, 1403, 1656, 1661, 1734, 1930, 1120, 1920, 1227, 1618, 1640, 1586, 1982, 1534, 1278, 1269, 1572, 1654, 1472, 1974, 1748, 1425, 1553, 1708, 1394, 1417, 1746, 1745, 1834, 1787, 1298, 1786, 1966, 1768, 1932, 1523, 1356, 1547, 1634, 1951, 1922, 222, 1461, 1628, 1888, 1639, 473, 1568, 1783, 572, 1522, 1934, 1629, 1283, 1550, 1859, 2007, 1996, 1822, 996, 1911, 1689, 1537, 1793, 1762, 1677, 1266, 1715]


total = 2020

finding_entries(expenses, total)