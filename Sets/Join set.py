# union() or instead of |
fruits_set ={'apple','bananas','cheery'}
cars_set ={'Ford','Toyota','Mercedes','apple'}
mix_set = fruits_set.union(cars_set)
print(mix_set)
vegetables_set = {'Ash gourd','Capsicum','Turnip','Broccoli','Cucumber'}
mix_diff_set =mix_set|vegetables_set
print(mix_diff_set)

#join multiple set
all_join_set = fruits_set.union(cars_set,mix_set,vegetables_set)
print(all_join_set)
set_1 ={'a','b','c',2}
set_2 ={2,3,4}
set_3 = {True,False,True}
total_set = set_1 | set_2 | set_3
print(total_set)
# join a set and a tuple
name_set ={'Wasel','Mamun','Masum'}
age_tupel =(10,23,4,5)
mix_set_tuple = name_set.union(age_tupel)
print(mix_set_tuple)
# update()
name_set.update(age_tupel)
print(name_set)
# intersection in two set
set_one ={'apple','microsoft','google'}
set_two ={'alibaba','apple','google'}
new_set = set_one.intersection(set_two)
print(new_set)
new_set_two =set_one & set_two
print(new_set_two)

# intersection_update()
set_one.intersection_update(set_two)
print(set_one)
mix_set_one = {'apple','bananas',False,0,1}
mix_set_two = {'google','microsoft',True,1,2,}
mix_new_set = mix_set_one.intersection(mix_set_two)
print(mix_new_set)
# differenet() used
mix_new_set_two =mix_set_one.difference(mix_set_two)
print(mix_new_set_two)
# used - difference symbol
mix_new_set_three =fruits_set.difference(cars_set)
print(mix_new_set_three)
# difference_update() method
print(set_one,set_two)
diff_new_set = set_one.difference_update(set_two)
print(diff_new_set)
# symmetric difference
sym_diff_set = set_one.symmetric_difference(set_two)
print(sym_diff_set)
# symmetric difference symbol
print(set_1,set_2)
sym_diff_two = set_1.symmetric_difference(set_2)
print(sym_diff_two)
# symmetric difference update
print(fruits_set,cars_set)
fruits_set.symmetric_difference_update(cars_set)
print(fruits_set)
fruits_set.add("fahad")
print(fruits_set)