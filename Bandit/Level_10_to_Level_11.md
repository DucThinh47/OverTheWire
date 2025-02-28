# Bandit Level 10 → Level 11

Level Goal

The password for the next level is stored in the file data.txt, which contains base64 encoded data

# Solution

Đăng nhập bandit10:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image38.png?raw=true)

Dùng lệnh ***ls -al***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image39.png?raw=true)

=> Tìm được file data.txt. Đọc nội dung file: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image40.png?raw=true)

=> Nội dung được mã hóa base64. Sử dụng lệnh ***base64 -d data.txt***, trong đó: 

- ***-d***: chỉ định decode, theo sau là tên file.

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image41.png?raw=true)

=> Tìm được password bandit11: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr




