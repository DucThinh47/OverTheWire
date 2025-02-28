# Bandit Level 11 → Level 12

Level Goal

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

# Solution

Đăng nhập bandit11: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image42.png?raw=true)

Dùng lệnh ***ls -al***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image43.png?raw=true)

Thử đọc nội dung file data.txt: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image44.png?raw=true)

=> Nội dung được mã hóa, theo mô tả của thử thách: "all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions", nghĩa là thay thế một chữ cái bằng chữ cái thứ 13 sau nó trong bảng chữ cái Latin. Ví dụ A -> N, B -> O, C -> P,... Truy cập Wikipedia ROT13 và tìm ra lệnh giải mã: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image45.png?raw=true)

=> Dùng lệnh ***cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'***:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image46.png?raw=true)

=> Tìm ra password bandit12: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

