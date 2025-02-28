# Bandit Level 7 → Level 8

Level Goal

The password for the next level is stored in the file data.txt next to the word millionth

# Solution

Đăng nhập bandit7: 

![img](27)

Dùng lệnh ***ls -al***:

![img](28)

=> Tìm được file ***data.txt***. Dùng lệnh ***cat*** nhưng kết quả là một danh sách username và password rất dài. 

Dựa vào mô tả thử thách, mật khẩu liên quan đến username millionth, có thể sử dụng lệnh để lọc kết quả: ***cat data.txt | grep 'millionth'***:

![img](29)

=> Tìm được password bandit8: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc