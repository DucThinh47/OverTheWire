# Bandit Level 10 → Level 11

Level Goal

The password for the next level is stored in the file data.txt, which contains base64 encoded data

# Solution

Đăng nhập bandit10:

![img](38)

Dùng lệnh ***ls -al***: 

![img](39)

=> Tìm được file data.txt. Đọc nội dung file: 

![img](40)

=> Nội dung được mã hóa base64. Sử dụng lệnh ***base64 -d data.txt***, trong đó: 

- ***-d***: chỉ định decode, theo sau là tên file.

![img](41)

=> Tìm được password bandit11: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr




