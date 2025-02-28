# Bandit Level 8 → Level 9

Level Goal

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

# Solution

Đăng nhập bandit8: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image30.png?raw=true)

Dùng lệnh ***ls- al***:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image31.png?raw=true)

Đọc nội dung file data.txt: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image32.png?raw=true)

=> Một danh sách rất dài các chuỗi được mã hóa. Dựa vào mô tả của thử thách "the only line of text that occurs only once", có thể dùng lệnh ***sort data.txt | uniq -u***, trong đó: 

- ***sort data.txt***: Sắp xếp nội dung của tệp data.txt theo thứ tự từ điển. ***uniq*** chỉ hoạt động trên các dòng liền kề giống nhau nên cần sắp xếp trước. 

- ***uniq -u***: Chỉ hiển thị những dòng không bị trùng lặp trong tệp. Các dòng xuất hiện nhiều hơn một lần sẽ bị loại bỏ hoàn toàn.

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image33.png?raw=true)

=> Tìm được password bandit9: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
