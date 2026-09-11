FROM python
# กำหนดโฟลเดอร์ทำงานหลักภายใน Container
WORKDIR /app
# คัดลอกไฟล์รายการ Library เข้าไปติดตั้งก่อน
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
# คัดลอกไฟล์สคริปต์ทั้งหมดในโฟลเดอร์ worker เข้าไปใน Container
COPY . .
# คำสั่งสำหรับเริ่มรันสคริปต์เมื่อ Container ทำงาน
CMD ["python", "consumer.py"]