# [Gold II] Fibonacci - 7677 

[문제 링크](https://www.acmicpc.net/problem/7677) 

### 성능 요약

메모리: 33432 KB, 시간: 40 ms

### 분류

수학, 정수론, 분할 정복을 이용한 거듭제곱, 피사노 주기

### 제출 일자

2025년 5월 25일 10:25:40

### 문제 설명

<p>In the Fibonacci integer sequence, F<sub>0</sub> = 0, F<sub>1</sub> = 1, and F<sub>n</sub> = F<sub>n−1</sub> + F<sub>n−2</sub> for n ≥ 2. For example, the first ten terms of the Fibonacci sequence are:</p>

<p>0, 1, 1, 2, 3, 5, 8, 13, 21, 34, . . .</p>

<p>An alternative formula for the Fibonacci sequence is</p>

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 109%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mrow><mjx-mo class="mjx-s3"><mjx-c class="mjx-c5B TEX-S3"></mjx-c></mjx-mo><mjx-mtable style="min-width: 5.108em;"><mjx-table><mjx-itable><mjx-mtr><mjx-mtd style="padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D439 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.106em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msub><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-bottom: 0.2em;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D439 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.106em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-texatom></mjx-script></mjx-msub><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr><mjx-mtr><mjx-mtd style="padding-right: 0.5em; padding-top: 0.2em;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D439 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.106em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-texatom></mjx-script></mjx-msub><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-top: 0.2em;"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D439 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em; margin-left: -0.106em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msub><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr></mjx-itable></mjx-table></mjx-mtable><mjx-mo class="mjx-s3"><mjx-c class="mjx-c5D TEX-S3"></mjx-c></mjx-mo></mjx-mrow><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mrow><mjx-mo class="mjx-s3"><mjx-c class="mjx-c5B TEX-S3"></mjx-c></mjx-mo><mjx-mtable justify="left" style="min-width: 2em;"><mjx-table><mjx-itable><mjx-mtr><mjx-mtd style="padding-right: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-bottom: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr><mjx-mtr><mjx-mtd style="padding-right: 0.5em; padding-top: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd><mjx-mtd style="padding-left: 0.5em; padding-top: 0.2em;"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr></mjx-itable></mjx-table></mjx-mtable><mjx-mo class="mjx-s3"><mjx-c class="mjx-c5D TEX-S3"></mjx-c></mjx-mo></mjx-mrow><mjx-script style="vertical-align: 1.177em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">[</mo><mtable columnspacing="1em" rowspacing="4pt"><mtr><mtd><msub><mi>F</mi><mrow data-mjx-texclass="ORD"><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></mtd><mtd><msub><mi>F</mi><mrow data-mjx-texclass="ORD"><mi>n</mi></mrow></msub></mtd></mtr><mtr><mtd><msub><mi>F</mi><mrow data-mjx-texclass="ORD"><mi>n</mi></mrow></msub></mtd><mtd><msub><mi>F</mi><mrow data-mjx-texclass="ORD"><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msub></mtd></mtr></mtable><mo data-mjx-texclass="CLOSE">]</mo></mrow><mo>=</mo><msup><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">[</mo><mtable columnspacing="1em" rowspacing="4pt"><mtr><mtd><mn>1</mn></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mn>1</mn></mtd><mtd><mn>0</mn></mtd></mtr></mtable><mo data-mjx-texclass="CLOSE">]</mo></mrow><mi>n</mi></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\[\begin{bmatrix} F_{ n+1 } & F_{ n } \\ F_{ n } & F_{ n-1 } \end{bmatrix}=\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^n\]</span> </mjx-container></p>

<p>Given an integer n, your goal is to compute the last 4 digits of F<sub>n</sub>.</p>

### 입력 

 <p>The input test file will contain multiple test cases. Each test case consists of a single line containing n (where 0 ≤ n ≤ 1,000,000,000). The end-of-file is denoted by a single line containing the number -1.</p>

### 출력 

 <p>For each test case, print the last four digits of Fn. If the last four digits of Fn are all zeros, print ‘0’; otherwise, omit any leading zeros (i.e., print F<sub>n</sub> mod 10000).</p>

