gardes = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud_list = sorted(students) #сортируем множество имен студентов и приобразуем его в список
average_score = {stud_list[0] : sum(gardes[0]) / len(gardes[0]),
                 stud_list[1] : sum(gardes[1]) / len(gardes[1]),
                 stud_list[2] : sum(gardes[2]) / len(gardes[2]),
                 stud_list[3] : sum(gardes[3]) / len(gardes[3]),
                 stud_list[4] : sum(gardes[4]) / len(gardes[4])}
print(average_score)
