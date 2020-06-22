import os

def text_from_image_file(image_name,lang):
    os.system('tesseract {} temp -l {}'.format(image_name, lang)) //ใช้คอมมานด์ไลน์
    read = open('temp'+'.txt','r',encoding='utf-8').read() //เปิดไฟล์ที่สร้างไว้มาอ่าน
    os.remove('temp.txt') //ลบไฟล์ที่สร้างไว้
    return read //รีเทิร์นค่าที่อ่านได้

if __name__ == '__main__':
    print(text_from_image_file("Blog/7002054.jpg", "tha"))//เรียกใช้ฟังค์ชันแล้วปรินต์ออกมา