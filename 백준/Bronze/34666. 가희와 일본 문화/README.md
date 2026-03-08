# [Bronze III] 가희와 일본 문화 - 34666 

[문제 링크](https://www.acmicpc.net/problem/34666) 

### 성능 요약

메모리: 2020 KB, 시간: 24 ms

### 분류

구현

### 제출 일자

2026년 03월 09일 00:36:11

### 문제 설명

<p>가희는 문제를 출제하기 위해 일본 관련 자료들을 찾아보곤 합니다. 일본에서 자주 볼 법한 <code>sousenkyo</code> 같은 것도 그중 하나입니다. 그런 가희의 눈에 들어온 것은 JLPT였습니다. JLPT는 일본어 능력 시험이지만, 사람들 사이에서는 "일본 문화에 관심이 많은지" 에 대한 척도로도 쓰이기 때문이에요. JLPT는 언어 지식, 독해, 청해 세 영역으로 구성되어 있으며, 응시 급수는 $1$급부터 $5$급까지 있습니다. 각 과목의 획득 점수와 총점에 따라 합격과 불합격이 나뉘게 됩니다. 급수에 따른 과락과 총점 합격선은 아래 [표 1]에 있습니다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 600px;">
<tbody>
<tr>
			<td style="text-align: center;">급수</td>
			<td style="text-align: center;">총점 최소 합격 점수</td>
			<td style="text-align: center;">언어 지식 과락</td>
			<td style="text-align: center;">독해 과락</td>
			<td style="text-align: center;">청해 과락</td>
</tr>
<tr>
			<td style="text-align: center;">$1$</td>
			<td style="text-align: center;">$100$점</td>
			<td style="text-align: center;">$18$점 이하</td>
			<td style="text-align: center;">$18$점 이하</td>
			<td style="text-align: center;">$18$점 이하</td>
</tr>
<tr>
			<td style="text-align: center;">$2$</td>
			<td style="text-align: center;">$90$점</td>
			<td style="text-align: center;">$18$점 이하</td>
			<td style="text-align: center;">$18$점 이하</td>
			<td style="text-align: center;">$18$점 이하</td>
</tr>
<tr>
			<td style="text-align: center;">$3$</td>
			<td style="text-align: center;">$95$점</td>
			<td style="text-align: center;">$18$점 이하</td>
			<td style="text-align: center;">$18$점 이하</td>
			<td style="text-align: center;">$18$점 이하</td>
</tr>
<tr>
			<td style="text-align: center;">$4$</td>
			<td style="text-align: center;">$90$점</td>
			<td style="text-align: center;">x</td>
			<td style="text-align: center;">x</td>
			<td style="text-align: center;">$18$점 이하</td>
</tr>
<tr>
			<td style="text-align: center;">$5$</td>
			<td style="text-align: center;">$80$점</td>
			<td style="text-align: center;">x</td>
			<td style="text-align: center;">x</td>
			<td style="text-align: center;">$18$점 이하</td>
</tr>
</tbody>
</table>

<ul>
<li>$4$급과 $5$급은 언어 지식과 독해 각각의 과락은 없으나, 언어 지식과 독해 점수를 합해서 $38$점 미만이면 과락</li>
<li>각 영역은 $60$점이 최고점이며 $0$점이 최저점</li>
</ul>

<p style="text-align: center;">[표 1] 급수에 따른 JLPT 합격 점수</p>

<p>사람들은 응시자에게 일본에 관심이 많은지 아닌지 질문합니다. 응시자는 아래 세 조건을 <strong>모두</strong> 만족하면 "저는 일본에 관심이 많아요." 라고 답합니다.</p>

<ol>
<li>$1$급 또는 $2$급에 응시하였습니다.</li>
<li>청해 점수가 $50$점 이상입니다.</li>
<li><strong>청해가 아닌 영역</strong>에 대해서 3-1번 조건을 만족하는 영역이 $2$개 이상이거나, 3-2번 조건을 만족하는 영역이 $1$개 이상입니다.
<ol>
<li>해당 영역의 점수에 $3$을 곱한 값보다 응시한 급수의 총점 최소 합격 점수가 더 높습니다.</li>
<li>해당 영역에서 과락을 받지 않는 최소 점수보다 $3$점 이상 높지 않습니다.</li>
</ol>
</li>
</ol>

<p>시험을 본 응시자는 $Q$명이며, 각 응시자의 응시 정보가 입력으로 주어집니다. 사람들이 각 응시자에게 일본에 관심이 많은지 아닌지 물어보았을 때, "저는 일본에 관심이 많아요."라고 답하는지 그렇지 않은지 알아봅시다.</p>

### 입력 

 <p>첫 번째 줄에 $Q$가 주어집니다.</p>

<p>두 번째 줄부터 $Q$개의 줄에 걸쳐 응시자의 응시 급수와 언어 지식, 독해, 청해 득점 점수가 공백으로 구분되어 주어집니다. 유효한 급수와 유효한 점수만 주어집니다.</p>

### 출력 

 <p>$Q$개의 줄에 걸쳐 사람들이 일본에 관심이 많은지 아닌지 물어보았을 때, 각 응시자가 "일본에 관심이 많다" 라고 답한다면 <span style="color:#e74c3c;"><code>YES</code></span>를, 아니면 <span style="color:#e74c3c;"><code>NO</code></span>를 한 줄에 하나씩 출력해 주세요.</p>

