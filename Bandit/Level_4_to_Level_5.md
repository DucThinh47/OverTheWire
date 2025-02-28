# Bandit Level 4 → Level 5

Level Goal

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

Đăng nhập bandit4: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image13.png?raw=true)

Dùng lệnh ***ls -al***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image14.png?raw=true)

Truy cập thư mục /inhere và dùng lệnh ***ls -al***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image15.png?raw=true)

Tìm được rất nhiều file, dựa vào mô tả thử thách, password nằm ở human-readable file. Dùng lệnh ***find . -type f -print0 | xargs -0 file***, trong đó: 

- ***find . -type f***: Tìm tất cả các tệp (-type f) trong thư mục hiện tại (.) và liệt kê đường dẫn của chúng.

- ***-print0 | xargs -0 file***: Nhận danh sách tệp từ **find** và chạy lệnh **file** trên mỗi tệp để xác định loại file của chúng. Sử dụng **-print0** của **find** và **-0** của **xargs** để xử lý tên tệp có ký tự đặc biệt an toàn hơn.

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image16.png?raw=true)

=> File 07 có thể đọc được. Dùng lệnh ***cat***:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image17.png?raw=true)

=> Tìm được password của bandit5: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

