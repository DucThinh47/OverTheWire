# Natas Level 6 → Level 7

Username: natas7

URL: http://natas7.natas.labs.overthewire.org

# Solution

Truy cập URL: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image37.png?raw=true)

Click Home và xem source page: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image38.png?raw=true)

Click About và xem source page: 

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image39.png?raw=true)

Tìm được gợi ý *password for webuser natas8 is in /etc/natas_webpass/natas8*, đồng thời thấy rằng *index.php* đang lấy tham số *page=home* để truy cập trang /home. 

=> Có thể thử lợi dụng lỗ hổng path traversal ở đây, thay giá trị tham số page thành */../../../etc/natas_webpass/natas8*:

![img](https://github.com/DucThinh47/OverTheWire/blob/main/Natas/images/image40.png?raw=true)

=> Password natas8: xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q


