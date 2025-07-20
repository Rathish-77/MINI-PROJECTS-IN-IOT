import cv2
vid = cv2.VideoCapture(0)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH) #getting width of image from cam
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = vid.get(cv2.CAP_PROP_FPS)# frame / seconds
print("width %d,height %d" % (width, height))
print("fps %f" % (fps))
grabbed, frame = vid.read()
#if os.path.exists("./output"):
#    shutil.rmtree("./output")
#os.mkdir("./output")

fourcc = cv2.VideoWriter.fourcc(*"XVID")

videowriter = cv2.VideoWriter("./21june2025.mkv",fourcc,15,(int(width), int(height)))
i=1

while grabbed:
    print(i,"\n")

    i=i+1
    videowriter.write(frame)
    #cv2.waitKey(1600) optional w r to laptops
    grabbed, frame = vid.read()
vid.release()
videowriter.release()
