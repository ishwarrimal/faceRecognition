import face_recognition
import os

listOfStudents = os.listdir('./known_faces')

print(listOfStudents)

for student in listOfStudents:
    if student.find('.png') != -1:
        picture_of_me = face_recognition.load_image_file("./known_faces/"+student)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

        unknown_picture = face_recognition.load_image_file("unknown_faces/group.jpeg")
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        # Now we can see the two face encodings are of the same person with `compare_faces`!

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        if results[0] == True:
            print("{} is present".format(student.split('.')[0]))
        else:
            print("{} is absent".format(student.split('.')[0]))
        