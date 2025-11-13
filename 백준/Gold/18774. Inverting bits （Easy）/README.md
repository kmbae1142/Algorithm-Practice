# [Gold V] Inverting bits (Easy) - 18774 

[문제 링크](https://www.acmicpc.net/problem/18774) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

해 구성하기, 비트마스킹

### 제출 일자

2025년 11월 14일 00:45:43

### 문제 설명

<p>The wannabe scientist Kleofáš has recently developed a new processor. The processor has got 26 registers, labeled <code>A</code> to <code>Z</code>. Each register is an 8-bit unsigned integer variable.</p>

<p>This new processor is incredibly simple. It only supports the instructions specified in the table below. (In all instructions, <code>R</code> is a name of a register, <code>C</code> is a constant, and <code>X</code> is either the name of a register or a constant. All constants are 8-bit unsigned integers, i.e., numbers from 0 to 255.)</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td>syntax</td>
			<td>semantics</td>
		</tr>
		<tr>
			<td><code>and R X</code></td>
			<td>Compute the bitwise and of the values <code>R</code> and <code>X</code>, and store it in <code>R</code>.</td>
		</tr>
		<tr>
			<td><code>or R X</code></td>
			<td>Compute the bitwise or of the values <code>R</code> and <code>X</code>, and store it in <code>R</code>.</td>
		</tr>
		<tr>
			<td><code>not R</code></td>
			<td>Compute the bitwise not of the value <code>R</code>, and store it in <code>R</code>.</td>
		</tr>
		<tr>
			<td><code>shl R C</code></td>
			<td>Take the value in <code>R</code>, shift it to the left by <code>C</code> bits, and store the result in <code>R</code>.</td>
		</tr>
		<tr>
			<td><code>shr R C</code></td>
			<td>Take the value in <code>R</code>, shift it to the right by <code>C</code> bits, and store the result in <code>R</code>.</td>
		</tr>
		<tr>
			<td><code>mov R X</code></td>
			<td>Store the value <code>X</code> into <code>R</code>.</td>
		</tr>
		<tr>
			<td><code>get R</code></td>
			<td>Read an 8-bit unsigned integer and store it in <code>R</code>.</td>
		</tr>
		<tr>
			<td><code>put R</code></td>
			<td>Output the content of the register <code>R</code> as an 8-bit unsigned integer.</td>
		</tr>
	</tbody>
</table>

<p>Notes:</p>

<ul>
	<li>After any instruction other than not, if the second argument was a register name, its content remains unchanged.</li>
	<li>Whenever <code>shl</code> or <code>shr</code> is called, the shifted value of the first argument is truncated on one end and padded with zeroes on the other end. For example, if <code>X</code> equals to binary 10110110, then <code>X shr 2</code> equals to 00101101.</li>
</ul>

<p><strong>Example task</strong></p>

<p>Assume that the input contains an arbitrary two 8-bit unsigned integers a and b. Write a program that will read these numbers and produce an integer z such that z = 0 if and only if a = b. (That is, if a and b differ, z must be positive.)</p>

<p><strong>Problem specification</strong></p>

<p>For each data set, you have to write a program for Kleofáš’s processor that solves the following task: The input for your program is a sequence of integers, each of them a 0 or a 1. The output of your program must be a sequence of their negations, in order. (That is, change each 0 into a 1 and vice versa.)</p>

<p>The sequence contains exactly 7 integers. In your program, you may only use the instruction not at most once. Your program must have at most 100 instructions.</p>

<p>Note that you have to use each of the instructions <code>get</code> and <code>put</code> exactly 7 times.</p>

### 입력 

 <p>This problem has no input.</p>

### 출력 

 <p>Send us your program as a plain ASCII text. Each line of the text may either contain one complete instruction, or just whitespace. If you submit anything that is not a proper program, it will be judged “Wrong answer” and you will get an appropriate error message.</p>

