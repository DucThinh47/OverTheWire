# Bandit Level 12 → Level 13

Level Goal

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

# Solution

Đăng nhập bandit12: 

![img](47)

Dùng lệnh ***ls -al***: 

![img](48)

Thử đọc nội dung file data.txt: 

![img](49)

=> file được mã hóa theo dạng hex dump.

Dựa vào mô tả thử thách, tạo thư mục /tmp/thinh: 

![img](50)

Copy file data.txt vào thư mục /tmp/thinh: 

![img](51)

Dùng lệnh ***xxd -r data.txt > data***, trong đó:

- ***xxd*** là một công cụ dùng để hiển thị hoặc chuyển đổi dữ liệu dưới dạng hex dump.

- ***-r*** (reverse) giúp chuyển đổi từ hex dump về dạng nhị phân gốc.

- Kết quả file dạng nhị phân được lưu vào file data.

![img](52)

Kiểm tra định dạng file data lúc này: 

![img](53)

=> Là file gzip, nhưng hiện tại tên file đang không đúng định dạng, sử dụng lệnh ***mv data data.gz*** để chuyển về định dạng đúng: 

![img](54)

Thử giải nén file data.gz này bằng lệnh ***gzip -d data.gz***:

![img](55)

Sau khi giải nén, file có tên là data, kiểm tra định dạng file data lúc này: 

![img](56)

=> Là file bzip2, một thuật toán nén có tỷ lệ nén cao hơn so với gzip (.gz), tiếp tục đổi lại tên của file data cho đúng định dạng, dùng lệnh ***mv data data.bz2***: 

![img](57)

Giải nén file bz2 này bằng lệnh ***bzip2 -d data.bz2***: 

![img](58)

Sau khi giải nén, file mới lại tên là data, kiểm tra định dạng file data lúc này: 

![img](59)

=> Là file gzip, tiếp tục đổi tên thành data.gz và giải nén file: 

![img](60)

Kiểm tra định dạng file data lúc này: 

![img](61)

=> Là file POSIX tar archive (GNU), là một định dạng lưu trữ tệp (archive) phổ biến trên Unix/Linux, được dùng để gom nhiều tệp vào một tệp duy nhất mà không nén.

Tiếp tục đổi tên file data thành data.tar cho đúng định dạng và dùng lệnh ***tar xf data.tar*** để giải nén, trong đó: 

- ***tar***: Lệnh tar (Tape ARchive) dùng để lưu trữ và giải nén tệp .tar trong Linux/Unix.

- ***-x*** (extract): Tùy chọn này dùng để giải nén tệp .tar.

- ***-f data.tar***: -f (file) chỉ định tệp lưu trữ (data.tar) cần giải nén.

![img](62)

=> Giải nén ra được file data5.bin, kiểm tra định dạng file này: 

![img](63)

=> Là file GNU, tiếp tục đổi tên thành data.tar cho phù hợp định dạng và dùng lệnh ***tar xf data5.bin*** để giải nén: 

![img](64)

=> Giải nén xong xuất hiện file data6.bin, kiểm tra định dạng file: 

![img](65)

=> Là file bzip2, tiếp tục đổi tên thành data.bz2 và dùng lệnh ***bzip2 -d data.bz2*** để giải nén file: 

![img](66)

Giải nén xong xuất hiện file data.

Tiếp tục kiểm tra định dạng file data, chuyển đổi định dạng file cho đến khi định dạng file thành định dạng có thể đọc được: 

![img](67)

=> Tìm được password bandit13: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn








