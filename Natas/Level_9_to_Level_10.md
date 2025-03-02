# Natas Level 9 → Level 10

Username: natas10

URL: http://natas10.natas.labs.overthewire.org

# Solution

Truy cập URL:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image48.png?raw=true)

Thử search ***; cat /etc/natas_webpass/natas11***: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image49.png?raw=true)

=> Website đã lọc những ký tự nguy hiểm.

Click View sourcecode: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image50.png?raw=true)

Có thể thấy các ký tự */[;|&]/* đã được lọc. Có một cách để bypass, sử dụng .* , nếu nhập input ".* /etc/natas_webpass/natas11" thì câu lệnh grep -i $key dictionary.txt có thể trở thành grep -i .* /etc/natas_webpass/natas11 dictionary.txt, lệnh này sẽ tìm tất cả các dòng trong file, hoặc có thể nói là in ra toàn bộ nội dung file. 

Nhập .* /etc/natas_webpass/natas11 và click search: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image51.png?raw=true)

=> Password natas11: UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk
