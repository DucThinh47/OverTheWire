# Bandit Level 4 → Level 5

Level Goal

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

Đăng nhập bandit4: 

![img](13)

Dùng lệnh ***ls -al***: 

![img](14)

Truy cập thư mục /inhere và dùng lệnh ***ls -al***: 

![img](15)

Tìm được rất nhiều file, dựa vào mô tả thử thách, password nằm ở human-readable file. Dùng lệnh ***find . -type f -print0 | xargs -0 file***, trong đó: 

- ***find . -type f***: Tìm tất cả các tệp (-type f) trong thư mục hiện tại (.) và liệt kê đường dẫn của chúng.

- ***-print0 | xargs -0 file***: Nhận danh sách tệp từ **find** và chạy lệnh **file** trên mỗi tệp để xác định loại file của chúng. Sử dụng **-print0** của **find** và **-0** của **xargs** để xử lý tên tệp có ký tự đặc biệt an toàn hơn.

![img](16)

=> File 07 có thể đọc được. Dùng lệnh ***cat***:

![img](17)

=> Tìm được password của bandit5: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

