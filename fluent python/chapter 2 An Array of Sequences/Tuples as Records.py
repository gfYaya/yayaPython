# coding = utf-8

# Example 2-7. Tuples used as records

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# for passport in sorted(traveler_ids):
#     print('%s' % passport)   # error=> TypeError: not all arguments converted during string formatting

for country, _ in traveler_ids:
    print(country)
