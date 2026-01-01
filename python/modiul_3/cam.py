# import cv2
# cam = cv2.videoCapture(0)
# while True:
#     _, frame=cam.read()
#     cv2.imshow('my cam',frame)
#     cv2.waitKey(1)


# with open ('message.text','w') as file:
#       file.write('I love you , python')


# with open('message.text','a') as file:
#     file.write('I love you ,python ')


# with open ('newmessage.text','w') as file:
    # file.write('I love don\'t to discuss')

with open('newmessage.text','r') as file:
    text=file.read()
    print(text)
