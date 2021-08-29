import csv

class Hospital:

    @staticmethod
    def update_data(hos_id, a1, a2, b1, b2, ab1, ab2, o1, o2):
        f = open('hospital_blood_data.csv')
        a = csv.reader(f)
        b = list(a)
        for i in range(len(b)):
            if b[i][0] == hos_id:
                b[i] = [hos_id, a1, a2, b1, b2, ab1, ab2, o1, o2]
                break
        f.close()

        f = open('hospital_blood_data.csv', 'a', newline='')
        a = csv.writer(f)
        a.writerows(b)
        f.close()

    @staticmethod
    def view_data(hos_id):
        f = open('hospital_data.csv')
        a = csv.reader(f)
        for i in a:
            if i[0] == hos_id:
                print(f"""Hospital Name: {i[1]}\n
                Hospital id: {i[0]}\n
                Pin code: {i[2]}\n
                Address: {i[3]}\n
                Contact: {i[4]}\n
                Email: {i[5]}\n
                """)
                break
        f.close()

        f = open('hospital_blood_data.csv')
        a = csv.reader(f)
        for i in a:
            if i[0] == hos_id:
                print(f"""Blood available:\n
                a+:{i[1]}, a-:{i[2]}, b+:{i[3]}, b-:{i[4]},\n
                ab+:{i[5]}, ab-:{i[6]}, o+:{i[7]}, o-:{i[8]}""")
                break
        f.close()

    @staticmethod
    def request_blood(hos_id, bg):
        f = open('users_data.csv')
        a = csv.reader(f)
        b = list(a)
        f2 = open('blood_requests.csv')
        a21 = csv.reader(f2)
        b21 = list(a21)
        print(b21)

        for i in range(len(b)):
            if (b[i][5] == bg) and b[i][9]:
                b21[i].append(hos_id)
                b21[i].append(-1)
        f.close()
        f2.close()

        f1 = open('blood_requests.csv', 'w+', newline='')
        a1 = csv.writer(f1)
        f1.truncate()
        a1.writerows(b21)
        f1.close()


while True:
    print("1.Login\n2.Exit\n")
    t = int(input())
    if t == 1:
        hospital = Hospital()
        hos_id = input("Enter hospital id: ")
        while True:
            print("1.Update data\n2.View data\n3.Request blood\n4. Exit")
            t2 = int(input())
            if t2 == 1:
                print("Enter units of blood of each type in blood bank")
                a1 = int(input("A+: "))
                a2 = int(input("A-: "))
                b1 = int(input("B+: "))
                b2 = int(input("B-: "))
                ab1 = int(input("AB+: "))
                ab2 = int(input("AB-: "))
                o1 = int(input("O+: "))
                o2 = int(input("O-: "))

                hospital.update_data(hos_id, a1, a2, b1, b2, ab1, ab2, o1, o2)

            elif t2 == 2:
                hospital.view_data(hos_id)

            elif t2 == 3:
                print("Enter the blood group required: ")
                bg = input()
                hospital.request_blood(hos_id, bg)

            else:
                break

    else:
        break
