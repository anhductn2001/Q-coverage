# Q-coverage
Đảm bảo Q – Coverage nhằm tối ưu thời gian sống của mạng và cân bằng tải trong mạng
![image](https://user-images.githubusercontent.com/62016666/166641607-3951902b-1750-4d31-bf4e-77cc280e616a.png)
![image](https://user-images.githubusercontent.com/62016666/166641628-e1b0b32a-35e0-4afa-abe2-7d5c3ee5c82d.png)
Ứng dụng chính của mạng cảm biến là theo dõi các target bằng cách triển khai các sensor.
Một target được bao phủ nếu nó nằm trong vùng bán kính cảm nhận của 1 cảm biến.
Tuy nhiên mỗi sensor thì sẽ có một giới hạn năng lượng nhất định,  và mỗi điểm target thì có 1 mức độ quan trọng nhất định.

Vì vậy nên mạng cảm biến Q-coverage được triển khai để đảm bảo cho từng mục tiêu với mức độ quan trọng khác nhau, công suất hoạt động khác nhau sẽ được bao phủ bởi 1 số lượng cảm biến khác nhau.
Gọi vector Q={q1, q2 ,…,qm} là yêu cầu bao phủ cho m target, bài toán Q- coverage có liên quan đến việc tối đa hóa tuổi thọ của mạng khi có ít nhất qj sensor bao phủ target thứ j tại mọi thời điểm.
Q-coverage là bài toán NP-complete và được giải quyết bằng một thuật toán heuristic.


