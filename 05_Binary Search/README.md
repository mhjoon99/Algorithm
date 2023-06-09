# 이진 탐색(Binary Search)

## 1️⃣ 범위를 반씩 좁혀가는 탐색

### 순차 탐색(Sequential Search)
- **순차 탐색**: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 순차로 데이터를 탐색한다는 의미
- 구현 간단
- 특징: 데이터 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인해야 함
- 데이터의 개수가 N개일 때 최대 N번의 비교 연산이 필요하므로 **순차 탐색의 최악의 경우 시간 복잡도: O(N)**

### 이진 탐색:반으로 쪼개면서 탐색하기
- **이진 탐색**: 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것
- 특징
    - 배열 내부의 데이터가 정렬되어 있어야만 사용 가능
    - 데이터가 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있음
    - 탐색 범위를 절반씩 좁혀가며 데이터를 탐색

#### 예시: 이미 정렬된 10개의 데이터 중에서 값이 4인 원소를 찾기
![image](https://github.com/mhjoon99/Algorithm/assets/70474860/e7074f92-22f6-48b6-8c64-13a962b2b64b)
![image](https://github.com/mhjoon99/Algorithm/assets/70474860/2d724002-4943-44db-a8ab-6573635fdfa3)
![image](https://github.com/mhjoon99/Algorithm/assets/70474860/fd2e5196-4d23-47f2-b75d-8f13ec4ab874)
