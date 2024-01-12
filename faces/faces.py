a = ["Hello", "😀", "Goodbye", "😥" ]
faces= input().split(" ")

for face in faces:
    if face == a[0] and len(faces) < 3:
        print(a[0], " " + a[1])
    elif face == a[2] and len(faces) < 3:
        print(a[2], " " + a[3])
    elif face == a[2] and len(faces):
        print(a[0], " " + a[1], " " + a[2], " " + a[3])    