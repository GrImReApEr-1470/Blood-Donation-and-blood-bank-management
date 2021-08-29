import sys
import csv


class User:

    @staticmethod
    def add_user(name, uid, contact, email, pin_code, bg, age, sex, address, don):
        f = open('users_data.csv', 'a', newline='')
        a = csv.writer(f)
        a.writerow([uid, name, contact, email, pin_code, bg, age, sex, address, don])
        f.close()

        f = open('users_data.csv')
        a = csv.reader(f)
        f1 = open('blood_requests.csv', 'a', newline='')         # new user added to blood_requests file.
        a1 = csv.writer(f1)
        for i in a:
            a1.writerow([i[0]])
        f.close()
        f1.close()

    @staticmethod
    def view_profile(uid):
        f = open('users_data.csv')
        a = csv.reader(f)
        for i in a:
            if i[0] == uid:
                print(f"""Name: {i[1]}\n
                User id: {i[0]}\n
                Contact: {i[2]}\n
                Email: {i[3]}\n
                Pin code: {i[4]}\n
                Blood Group: {i[5]}\n
                Age: {i[6]}\n
                Sex: {i[7]}\n
                Address: {i[8]}\n
                Allow blood requests (become a donor): {i[9]}\n
                """)
                break
        f.close()

    @staticmethod
    def donate_blood(uid, pin_code, hos_id):
        f = open('hospital_data.csv')
        a = csv.reader(f)
        for i in a:
            if(pin_code == i[2] or pin_code == -1) and (hos_id == i[0] or hos_id == -1):
                print(f"""Hospital Name: {i[1]}\n
                                Hospital id: {i[0]}\n
                                Pin code: {i[2]}\n
                                Address: {i[3]}\n
                                Contact: {i[4]}\n
                                Email: {i[5]}\n
                                """)
        f.close()

    @staticmethod
    def view_hospitals(hos_id, pin_code):
        f = open('hospital_data.csv')
        a = csv.reader(f)
        for i in a:
            if (i[0] == hos_id or hos_id == -1) and (i[2] == pin_code or pin_code == -1):
                print(f"""Hospital name: {i[1]}\n
                    Hospital id: {i[0]}\n
                    Pin code: {i[2]}\n
                    Address: {i[3]}\n
                    Contact: {i[4]}\n
                    Email: {i[5]}\n
                    """)

    @staticmethod
    def request_blood(uid, hos_id):
        f = open('users_data.csv')
        a = csv.reader(f)
        for i in a:
            if i[0] == uid:
                bg = i[5]
                break
        x = 1 if bg == 'a1' else 2 if bg == 'a2' else 3 if bg == 'b1' else 4 if bg == 'b2' else 5 if bg == 'ab1'\
            else 6 if bg == 'ab2'else 7 if bg == 'o1' else 8
        f.close()
        f1 = open('hospital_blood_data.csv')
        a1 = csv.reader(f1)
        f2 = open('users_data.csv')
        a2 = csv.reader(f2)
        b2 = list(a2)
        f3 = open('blood_requests.csv')
        a3 = csv.reader(f3)
        b3 = list(a3)
        for i in a1:
            if i[0] == hos_id:
                if int(i[x]) > 0:
                    print('The mentioned hospital already has the required blood type in it\'s blood bank.')
                    print('Blood request terminated.')
                else:
                    c = []
                    for j in range(len(b2)):
                        if (b2[j][5] == bg) and b2[j][9]:
                            x = b3[j]
                            x.append(hos_id)
                            x.append(uid)
                            b3[j] = x
                            # b3[j].append([hos_id, uid])
                            # b3[j] = x
                break
        f1.close()
        f2.close()
        f3.close()
        f = open('blood_requests.csv', 'w+', newline='')
        a = csv.writer(f)
        f.truncate()
        a.writerows(b3)

    @staticmethod
    def view_requests(uid):
        f = open('blood_requests.csv')
        a = csv.reader(f)
        f1 = open('hospital_data.csv')
        a1 = csv.reader(f1)
        f2 = open('users_data.csv')
        a2 = csv.reader(f2)
        for i in a:
            if i[0] == uid:
                x = len(i)
                if x == 1:
                    print('You have no requests.')
                else:
                    for j in range(1, x, 2):
                        for k in a1:
                            if k[0] == i[j]:
                                hospital_name = k[1]
                        if i[j+1] == -1:
                            recipient = -1
                        else:
                            for k in a2:
                                if k[0] == i[j+1]:
                                    recipient = k[1]
                        print(f"""There is a request made through\nHospital name: {hospital_name}\n
                        Hospital id: {i[j]}""")
                        if recipient == -1:
                            print("The request was made by the hospital itself.")
                        else:
                            print(f"The request was made by {recipient}, id: {i[j+1]}\n")
        f.close()
        f1.close()
        f2.close()

    @staticmethod
    def accept_requests(uid):
        f = open('blood_requests.csv')
        a = csv.reader(f)
        b = list(a)
        f1 = open('hospital_data.csv')
        a1 = csv.reader(f1)
        b1 = list(a1)
        f2 = open('users_data.csv')
        a2 = csv.reader(f2)
        f3 = open('blood_requests.csv', 'w+', newline='')
        a3 = csv.writer(f3)
        c = []
        for i in range(len(b)):
            if b[i][0] == uid:
                c.append([b[i][0]])
                # x = b[i][0]
                # b[i] = [x]
            else:
                c.append(b[i])
        for i in range(len(b)):
            if b[i][0] == uid:
                x = len(b[i])
                if x == 1:
                    print('You have no requests.')
                else:
                    for j in range(1, x, 2):
                        for k in range(len(b1)):
                            print(b1[k][0])
                            if b1[k][0] == b[i][j]:
                                hospital_name = b1[k][1]
                        if b[i][j+1] == -1:
                            recipient = -1
                        else:
                            for k in a2:
                                if k[0] == b[i][j+1]:
                                    recipient = k[1]
                        print(f"""{j//2+1}. There is a request made through\nHospital name: {hospital_name}\n
                                                Hospital id: {b[i][j]}""")
                        if recipient == -1:
                            print("  The request was made by the hospital itself.")
                        else:
                            print(f"  The request was made by {recipient}, id: {b[i][j+1]}\n")
                    print("Do you want to accept a request?(Y/N)")
                    ans = input()
                    if ans == 'Y':
                        print("Choose which request to accept.")
                        aa = int(input())
                        aa = 2 * aa - 1
                        for k in range(len(b1)):
                            if b1[k][0] == b[i][aa]:
                                hospital_name = b1[k][1]
                        print(f"Hospital {hospital_name} will be notified that you accepted the blood request.")
                        print("Other requests will be ignored.")
                        f3.truncate()
                        a3.writerows(c)

        f.close()
        f1.close()
        f2.close()
        f3.close()


class Admin:

    @staticmethod
    def add_hospital(name, hos_id, pin_code, address, contact, email):
        f = open('hospital_data.csv', 'a', newline='')
        a = csv.writer(f)
        a.writerow([hos_id, name, pin_code, address, contact, email])
        f.close()

        f = open('hospital_blood_data.csv', 'a', newline='')
        a = csv.writer(f)
        a.writerow([hos_id, 0, 0, 0, 0, 0, 0, 0, 0])
        f.close()

    @staticmethod
    def view_hospitals(hos_id, pin_code):
        f = open('hospital_data.csv')
        a = csv.reader(f)
        for i in a:
            if(i[0] == hos_id or hos_id == -1) and (i[2] == pin_code or pin_code == -1):
                print(f"""Hospital name: {i[1]}\n
                Hospital id: {i[0]}\n
                Pin code: {i[2]}\n
                Address: {i[3]}\n
                Contact: {i[4]}\n
                Email: {i[5]}\n
                """)

    @staticmethod
    def view_donors(bg, pin_code, uid):
        f = open('users_data.csv')
        a = csv.reader(f)
        for i in a:
            if (i[0] == uid or uid == -1) and (i[4] == pin_code or pin_code == -1) and (i[5] == bg or bg == -1):
                print(f"""Name: {i[1]}
                User id: {i[0]}
                Contact: {i[2]}
                Email: {i[3]}
                Pin code: {i[4]}
                Blood Group: {i[5]}
                Age: {i[6]}
                Sex: {i[7]}
                Address: {i[8]}
                Allow blood requests (become a donor): {i[9]}
                """)
        f.close()


while True:
    print("1.Users portal\n2.Admin portal\n3.Exit")
    t = int(input())
    if t == 1:
        user = User()
        while True:
            print("""\n1.New User\n2.Log in\n3.Exit""")
            t1 = int(input())

            if t1 == 1:
                name = input("Enter name: ")
                uid = input("Enter id: ")
                contact = input("Enter phone number: ")
                email = input("Enter email: ")
                pin_code = input("Enter pin code: ")
                bg = input("Enter blood group(A+:a1, A-:a2, B+:b1, B-:b2, AB+:ab1, AB-:ab2, O+:o1, O-:o2\n-")
                age = input("Enter age: ")
                sex = input("Enter sex: ")
                address = input("Enter address: ")
                don = input("Allow blood requests (become a donor)(Y/N): ")
                don = True if don == 'Y' else False

                user.add_user(name, uid, contact, email, pin_code, bg, age, sex, address, don)

            elif t1 == 2:
                uid = input("Enter user id: ")
                while True:
                    print("""\n1.View my profile.\n2.Donate Blood.\n3.View Hospitals\n4.Request Blood\n5.view requests\n6.Accept requests\n""")
                    t2 = int(input())

                    if t2 == 1:
                        user.view_profile(uid)

                    elif t2 == 2:
                        print("Find donation camp by:\n1.Hospital id.\n2.pin code3.All camps\n")
                        t3 = int(input())
                        if t3 == 1:
                            pin_code = -1
                            hos_id = input("Enter hospital id: ")
                        elif t3 == 2:
                            hos_id = -1
                            pin_code = input("Enter pin code: ")
                        else:
                            pin_code = -1
                            hos_id = -1
                        user.donate_blood(uid, pin_code, hos_id)

                    elif t2 == 3:
                        print("Find hospitals by:\n1.Hospital id.\n2.pin code3.All hospitals\n")
                        t3 = int(input())
                        if t3 == 1:
                            pin_code = -1
                            hos_id = input("Enter hospital id: ")
                        elif t3 == 2:
                            hos_id = -1
                            pin_code = input("Enter pin code: ")
                        else:
                            pin_code = -1
                            hos_id = -1
                        user.view_hospitals(hos_id, pin_code)

                    elif t2 == 4:
                        hos_id = input("Enter the hospital id where you need the blood: ")
                        user.request_blood(uid, hos_id)

                    elif t2 == 5:
                        user.view_requests(uid)

                    elif t2 == 6:
                        user.accept_requests(uid)

                    else:
                        break
            else:
                break

    elif t == 2:
        admin = Admin()
        while True:
            print("1.Add hospital\n2.View hospitals\n3.View donors\n4.\n5.Exit.\n")
            t1 = int(input())
            if t1 == 1:
                hos_name = input("Enter hospital name: ")
                hos_id = input("Enter hospital id: ")
                pin_code = input("Enter pin code: ")
                address = input("Enter address: ")
                contact = input("Enter hospital contact: ")
                email = input("Enter hospital email: ")

                admin.add_hospital(hos_name, hos_id, pin_code, address, contact, email)

            elif t1 == 2:
                print("Find hospitals by:\n1.Hospital id.\n2.pin code3.All hospitals\n")
                t3 = int(input())
                if t3 == 1:
                    pin_code = -1
                    hos_id = input("Enter hospital id: ")
                elif t3 == 2:
                    hos_id = -1
                    pin_code = input("Enter pin code: ")
                else:
                    pin_code = -1
                    hos_id = -1
                admin.view_hospitals(hos_id, pin_code)

            elif t1 == 3:
                print("1. Find by user id\n2. Find by pin code\n3.All donors")
                t2 = int(input())
                if t2 == 1:
                    pin_code = -1
                    uid = input("Enter user id: ")
                elif t2 == 2:
                    uid = -1
                    pin_code = input("Enter pin code: ")
                else:
                    uid = -1
                    pin_code = -1

                print("Do you want to filter by blood group?(Y/N): ")
                ans = input()
                if ans == 'Y':
                    print("Enter blood group(A+:a1, A-:a2, B+:b1, B-:b2, AB+:ab1, AB-:ab2, O+:o1, O-:o2")
                    bg = input()
                else:
                    bg = -1

                admin.view_donors(bg, pin_code, uid)

            elif t1 == 4:
                pass

            else:
                break

    else:
        break
