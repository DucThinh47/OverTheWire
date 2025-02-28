# Bandit Level 5 → Level 6

Level Goal

The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

human-readable

1033 bytes in size

not executable

# Solution

Đăng nhập bandit5: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image18.png?raw=true)

Truy cập thư mục /inhere và dùng lệnh ***ls -al***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image19.png?raw=true)

Có nhiều thư mục con trong thư mục /inhere, dựa vào mô tả thử thách, cần tìm file có dạng human-readable, 1033 bytes in size và not executable, có thể sử dụng lệnh sau ***find . -type f -size 1033c -print0 ! -executable | xargs -0 file***, trong đó: 

- ***-size 1033c***: chỉ định size của file là 1033

- ***! -executable***: chỉ định file không thực thi được

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image20.png?raw=true)

=> Tìm được đường dẫn của file có đầy đủ các thuộc tính như mô tả. Sử dụng lệnh ***cat***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image21.png?raw=true)

=> Tìm được password bandit6: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG



