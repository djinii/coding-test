while True:
    n, *heights = map(int, input().split())
    if n == 0:
        break
    heights.append(0)
    stack = []
    max_area = 0
    for i in range(n + 1):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    print(max_area)