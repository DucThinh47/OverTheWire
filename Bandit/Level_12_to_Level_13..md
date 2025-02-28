# Bandit Level 12 → Level 13

Level Goal

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

# Solution

Đăng nhập bandit12: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image47.png?raw=true)

Dùng lệnh ***ls -al***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image48.png?raw=true)

Thử đọc nội dung file data.txt: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image49.png?raw=true)

=> file được mã hóa theo dạng hex dump.

Dựa vào mô tả thử thách, tạo thư mục /tmp/thinh: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image50.png?raw=true)

Copy file data.txt vào thư mục /tmp/thinh: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image51.png?raw=true)

Dùng lệnh ***xxd -r data.txt > data***, trong đó:

- ***xxd*** là một công cụ dùng để hiển thị hoặc chuyển đổi dữ liệu dưới dạng hex dump.

- ***-r*** (reverse) giúp chuyển đổi từ hex dump về dạng nhị phân gốc.

- Kết quả file dạng nhị phân được lưu vào file data.

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image52.png?raw=true)

Kiểm tra định dạng file data lúc này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image53.png?raw=true)

=> Là file gzip, nhưng hiện tại tên file đang không đúng định dạng, sử dụng lệnh ***mv data data.gz*** để chuyển về định dạng đúng: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image54.png?raw=true)

Thử giải nén file data.gz này bằng lệnh ***gzip -d data.gz***:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image55.png?raw=true)

Sau khi giải nén, file có tên là data, kiểm tra định dạng file data lúc này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image56.png?raw=true)

=> Là file bzip2, một thuật toán nén có tỷ lệ nén cao hơn so với gzip (.gz), tiếp tục đổi lại tên của file data cho đúng định dạng, dùng lệnh ***mv data data.bz2***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image57.png?raw=true)

Giải nén file bz2 này bằng lệnh ***bzip2 -d data.bz2***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image58.png?raw=true)

Sau khi giải nén, file mới lại tên là data, kiểm tra định dạng file data lúc này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image59.png?raw=true)

=> Là file gzip, tiếp tục đổi tên thành data.gz và giải nén file: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image60.png?raw=true)

Kiểm tra định dạng file data lúc này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image61.png?raw=true)

=> Là file POSIX tar archive (GNU), là một định dạng lưu trữ tệp (archive) phổ biến trên Unix/Linux, được dùng để gom nhiều tệp vào một tệp duy nhất mà không nén.

Tiếp tục đổi tên file data thành data.tar cho đúng định dạng và dùng lệnh ***tar xf data.tar*** để giải nén, trong đó: 

- ***tar***: Lệnh tar (Tape ARchive) dùng để lưu trữ và giải nén tệp .tar trong Linux/Unix.

- ***-x*** (extract): Tùy chọn này dùng để giải nén tệp .tar.

- ***-f data.tar***: -f (file) chỉ định tệp lưu trữ (data.tar) cần giải nén.

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image62.png?raw=true)

=> Giải nén ra được file data5.bin, kiểm tra định dạng file này: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image63.png?raw=true)

=> Là file GNU, tiếp tục đổi tên thành data.tar cho phù hợp định dạng và dùng lệnh ***tar xf data5.bin*** để giải nén: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image64.png?raw=true)

=> Giải nén xong xuất hiện file data6.bin, kiểm tra định dạng file: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image65.png?raw=true)

=> Là file bzip2, tiếp tục đổi tên thành data.bz2 và dùng lệnh ***bzip2 -d data.bz2*** để giải nén file: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image66.png?raw=true)

Giải nén xong xuất hiện file data.

Tiếp tục kiểm tra định dạng file data, chuyển đổi định dạng file cho đến khi định dạng file thành định dạng có thể đọc được: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Bandit/images/image67.png?raw=true)

=> Tìm được password bandit13: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn








