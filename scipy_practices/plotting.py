#! usr/bin/env python3
# %%
import random
import matplotlib.pyplot as plt

marks = []
ids_students = []
for i in range(30):
    marks_generated = random.normalvariate(3.25, 0.98)
    marks_generated = round(marks_generated, 2)
    added = False
    while not added:
        id_generated = random.randint(20202001, 20202999)
        id_generated = str(id_generated)
        if id_generated not in ids_students:
            marks.append(marks_generated)
            ids_students.append(id_generated)
            added = True
# %%
plt.plot(ids_students, marks)
plt.title("Marks")
plt.xlabel("Nota")
plt.ylabel("IDS de estudiantes")
plt.xticks(rotation=90)
plt.show()

# %%
plt.hist(marks, bins=4, color=['green'], edgecolor='black', linewidth=1)
plt.title("Cantidad de estudiantes por rango de nota")
plt.xlabel("Cantidad de estudiantes")
plt.ylabel("Rango de nota")
plt.show()

# %%
plt.scatter(ids_students, marks)
plt.title("Marks")
plt.xlabel("Nota")
plt.ylabel("IDS de estudiantes")
plt.xticks(rotation=90)
plt.show()
# %%
