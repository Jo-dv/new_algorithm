# [Gold V] 동전 - 3363 

[문제 링크](https://www.acmicpc.net/problem/3363) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2025년 7월 18일 23:46:17

### 문제 설명

<p>여러분은 양팔 저울 하나와 동전 12개(1, 2, ..., 12 의 번호)를 가지고 있는데, 그 중 하나는 모조품입니다. 모조품은 다른 동전보다 가볍거나 무겁습니다. </p>

<p>양팔 저울로 세 번 측정하여 모조품을 찾고,  그것이 무거운지 가벼운지 밝히는 프로그램을 작성하세요.</p>

### 입력 

 <p>무게를 측정한 결과 데이터가 아래와 같은 형식의 표준 입력으로 주어지게 됩니다.</p>

<p>A B C D x E F G H</p>

<p>A, B, C, D, E, F, G, H 는 서로 다른 8 개의 동전들의 숫자이고, x 는 <, >, =  중에 하나입니다. 다음과 같은 의미를 지닙니다.</p>

<ul>
	<li>< : A, B, C, D 의 총합은 E, F, G, H 의 총합보다 작다</li>
	<li>> : A, B, C, D 의 총합은 E, F, G, H 의 총합보다 크다</li>
	<li>= : A, B, C, D 의 총합은 E, F, G, H 의 총합과 같다</li>
</ul>

### 출력 

 <p>프로그램은 표준출력에 모조품의 번호를 출력하고, 다른 동전보다 무거운 경우에는 + 를, 가벼운 경우에는 - 를 이어서 출력합니다.</p>

<p>세 번의 측정 데이터가 모순되는 경우에는 "impossible" 을 출력해야 합니다.</p>

<p>데이터가 모순되지는 않지만 모조품의 번호를 알아내기에 불충분하거나, 무거운지 가벼운지 알 수 없는 경우에는 "indefinite" 를 출력해야 합니다.</p>

