import cv2 as cv

# อ่านรูปภาพ
img = cv.imread('homepage ridebox.png')

# เช็กว่ามีรูปจริงไหม 
if img is None:
    print("ไม่พบไฟล์ภาพ!")
    exit()

# 3. แสดงรูปและเช็กปุ่มกด
cv.imshow('Image', img)
key = cv.waitKey(0) & 0xFF

# กด s safe image,กดปุ่มอื่น ปิด window
if key == ord('s'):
    cv.imwrite('saved_image.png', img)

cv.destroyAllWindows()