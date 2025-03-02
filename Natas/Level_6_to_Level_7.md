# Natas Level 6 → Level 7

Username: natas7

URL: http://natas7.natas.labs.overthewire.org

# Solution

Truy cập URL: 

![img](37)

Click Home và xem source page: 

![img](38)

Click About và xem source page: 

![img](39)

Tìm được gợi ý *password for webuser natas8 is in /etc/natas_webpass/natas8*, đồng thời thấy rằng *index.php* đang lấy tham số *page=home* để truy cập trang /home. 

=> Có thể thử lợi dụng lỗ hổng path traversal ở đây, thay giá trị tham số page thành */../../../etc/natas_webpass/natas8*:

![img](40)

=> Password natas8: xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q


