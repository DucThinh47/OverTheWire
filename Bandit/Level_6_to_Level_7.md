# Bandit Level 6 → Level 7

Level Goal

The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7

owned by group bandit6

33 bytes in size

# Solution

Đăng nhập bandit6: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image22.png?raw=true)

Dùng lệnh ***ls -al***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image23.png?raw=true)

Dựa vào mô tả thử thách, cần tìm file có các thuộc tính: owned by user bandit7, owned by group bandit6 và 33 bytes in size. Có thể sử dụng lệnh: ***find / -type f -user bandit7 -group bandit6 -size 33c -print0 | xargs -0 file***, trong dó: 

- ***find /***: tìm kiếm từ thư mục gốc

- ***-user bandit7***: chỉ định file sở hữu bởi user bandit7

- ***-group bandit6***: chỉ định file thuộc group bandit6

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image24.png?raw=true)

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image25.png?raw=true)

=> Tìm được file bandit7.password, dùng lệnh ***cat***:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image26.png?raw=true)

=> Tìm được password bandit7: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

