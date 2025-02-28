# Bandit Level 11 → Level 12

Level Goal

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

# Solution

Đăng nhập bandit11: 

![img](42)

Dùng lệnh ***ls -al***: 

![img](43)

Thử đọc nội dung file data.txt: 

![img](44)

=> Nội dung được mã hóa, theo mô tả của thử thách: "all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions", nghĩa là thay thế một chữ cái bằng chữ cái thứ 13 sau nó trong bảng chữ cái Latin. Ví dụ A -> N, B -> O, C -> P,... Truy cập Wikipedia ROT13 và tìm ra lệnh giải mã: 

![img](45)

=> Dùng lệnh ***cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'***:

![img](46)

=> Tìm ra password bandit12: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

