# Bandit Level 6 → Level 7

Level Goal

The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7

owned by group bandit6

33 bytes in size

# Solution

Đăng nhập bandit6: 

![img](22)

Dùng lệnh ***ls -al***: 

![img](23)

Dựa vào mô tả thử thách, cần tìm file có các thuộc tính: owned by user bandit7, owned by group bandit6 và 33 bytes in size. Có thể sử dụng lệnh: ***find / -type f -user bandit7 -group bandit6 -size 33c -print0 | xargs -0 file***, trong dó: 

- ***find /***: tìm kiếm từ thư mục gốc

- ***-user bandit7***: chỉ định file sở hữu bởi user bandit7

- ***-group bandit6***: chỉ định file thuộc group bandit6

![img](24)

![img](25)

=> Tìm được file bandit7.password, dùng lệnh ***cat***:

![img](26)

=> Tìm được password bandit7: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

