grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=list(students)
print(students)
sort_students = sorted(students)
print(sort_students)
Sr_Bal_st0 = sum(grades[0])/len(grades[0])
Sr_Bal_st1 = sum(grades[1])/len(grades[1])
Sr_Bal_st2 = sum(grades[2])/len(grades[2])
Sr_Bal_st3 = sum(grades[3])/len(grades[3])
Sr_Bal_st4 = sum(grades[4])/len(grades[4])
print(sort_students[0], Sr_Bal_st0)
print(sort_students[1], Sr_Bal_st1)
print(sort_students[2], Sr_Bal_st2)
print(sort_students[3], Sr_Bal_st3)
print(sort_students[4], Sr_Bal_st4)
slov_stud_list= ((sort_students[0], Sr_Bal_st0), (sort_students[1], Sr_Bal_st1), (sort_students[2], Sr_Bal_st2), (sort_students[3], Sr_Bal_st3), (sort_students[4], Sr_Bal_st4))
print(slov_stud_list)
slov_stud = dict(slov_stud_list)
print(slov_stud)