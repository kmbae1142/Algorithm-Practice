# [Silver V] PAUL 문자열 (Easy) - 34924 

[문제 링크](https://www.acmicpc.net/problem/34924) 

### 성능 요약

메모리: 37112 KB, 시간: 108 ms

### 분류

구현, 문자열, 홀짝성

### 제출 일자

2026년 03월 09일 00:36:11

### 문제 설명

<p><strong>이 문제는 Hard 버전과 굵게 표시된 제약 조건을 제외하면 동일합니다.</strong></p>

<p>PAUL 문자열은 <span style="color:#e74c3c;"><code>P</code></span>,<span style="color:#e74c3c;"><code>A</code></span>,<span style="color:#e74c3c;"><code>U</code></span>,<span style="color:#e74c3c;"><code>L</code></span>을 각각 하나 이상 포함하는 알파벳 대문자로 이루어진 문자열이다. 모그는 길이 $N$의 PAUL 문자열을 선물받았다. 선물받은 문자열을 가지고 놀던 모그는 "이 문자열의 이웃한 두 문자를 삭제한 뒤 남은 부분을 이어 붙이는 연산을 반복해 정확히 <span style="color:#e74c3c;"><code>PAUL</code></span>만 남길 수 있을까?" 하는 궁금증이 생겼다.</p>

<p>머리가 좋지 않은 모그 대신 궁금증을 해결해 주자.</p>

### 입력 

 <p>첫째 줄에 모그가 선물받은 PAUL 문자열의 길이 $N$이 주어진다. $(4\le N\le 100\,000)$</p>

<p>둘째 줄에 모그가 선물받은 길이 $N$의 PAUL 문자열이 주어진다. 이 문자열에서 <span style="color:#e74c3c;"><code>P</code></span>,<span style="color:#e74c3c;"><code>A</code></span>,<span style="color:#e74c3c;"><code>U</code></span>,<span style="color:#e74c3c;"><code>L</code></span>은 <strong>정확히 한 번씩</strong> 등장한다.</p>

### 출력 

 <p>정확히 <span style="color:#e74c3c;"><code>PAUL</code></span>만 남길 수 있다면 <span style="color:#e74c3c;"><code>YES</code></span>, 그렇지 않다면 <span style="color:#e74c3c;"><code>NO</code></span>를 출력한다.</p>

