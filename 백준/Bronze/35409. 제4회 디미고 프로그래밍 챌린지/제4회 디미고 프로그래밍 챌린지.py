h, m = map(int, input().split())
t = h * 60 + m

if 390 <= t <= 540 \
    or 590 <= t <= 600 \
    or 650 <= t <= 660 \
    or 710 <= t <= 720 \
    or 770 <= t <= 830 \
    or 880 <= t <= 890 \
    or 940 <= t <= 950 \
    or 1000 <= t <= 1370:
    print("Yes")
else:
    print("No")