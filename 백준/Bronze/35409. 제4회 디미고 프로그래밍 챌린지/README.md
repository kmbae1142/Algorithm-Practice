# [Bronze IV] 제4회 디미고 프로그래밍 챌린지 - 35409 

[문제 링크](https://www.acmicpc.net/problem/35409) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현, 많은 조건 분기

### 제출 일자

2026년 4월 16일 10:36:13

### 문제 설명

<p>디미고 프로그래밍 챌린지에 참가하는 학생들은 학교 일과를 준수하며 참가해야 한다. 일과를 준수하는 디미고 학생들은 아래에 명시한 시간대에만 코드를 제출할 수 있다.</p>

<table class="time-table table table-bordered">
<tbody>
<tr>
<th>코드를 제출할 수 있는 시간대</th>
</tr>
<tr>
<td>06:30-09:00</td>
</tr>
<tr>
<td>09:50-10:00</td>
</tr>
<tr>
<td>10:50-11:00</td>
</tr>
<tr>
<td>11:50-12:00</td>
</tr>
<tr>
<td>12:50-13:50</td>
</tr>
<tr>
<td>14:40-14:50</td>
</tr>
<tr>
<td>15:40-15:50</td>
</tr>
<tr>
<td>16:40-22:50</td>
</tr>
</tbody>
</table>

<p><span style="color:#e74c3c;"><code>09:00</code></span>이나 <code><span style="color:#e74c3c;">10:50</span></code> 등 시작 시간과 종료 시간에 맞춰서 제출해도 된다.</p>

<p>ibasic은 디미고 프로그래밍 챌린지에 참여해서 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H$</span></mjx-container>시 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>분에 코드를 제출했다. ibasic이 학교 일과를 준수하면서 코드를 제출하였는지 판단하시오.</p>

### 입력 

 <p>첫 번째 줄에 ibasic이 코드를 제출한 시각을 나타내는 두 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>H</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$H$</span></mjx-container>와 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 공백으로 구분되어 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D43B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c3B"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>0</mn><mo>≤</mo><mi>H</mi><mo>≤</mo><mn>23</mn><mo>;</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(0\le H\le 23;$</span></mjx-container> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>M</mi><mo>≤</mo><mn>59</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0\le M\le 59)$</span> </mjx-container></p>

### 출력 

 <p>첫 번째 줄에 ibasic이 학교 일과를 준수하면서 코드를 제출하였다면 <code><span style="color:#e74c3c;">Yes</span></code>를, 아니라면 <code><span style="color:#e74c3c;">No</span></code>를 출력한다.</p>

