# Bandit Level 9 → Level 10

Level Goal

The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

# Solution

Đăng nhập bandit9: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image34.png?raw=true)

Dùng lệnh ***ls -al*** tìm được file data.txt: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image35.png?raw=true)

Đọc nội dung file data.txt: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image36.png?raw=true)

=> Nội dung file có vẻ đã bị mã hóa. Dựa vào mô tả thử thách "one of the few human-readable strings, preceded by several ‘=’ characters", có thể sử dụng lệnh ***cat data.txt | strings | grep '='***, trong đó: 

- ***strings***: Lọc ra các chuỗi có thể đọc được(human-readable) từ file.

- ***grep '='***: Lọc ra chỉ những dòng có chứa dấu =.

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image37.png?raw=true)

=> Tìm được password bandit10: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey


