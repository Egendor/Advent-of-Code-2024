import re

all_input = ""
with open("input03.txt", "r") as f:
    all_input += f.read().strip()

all_match = re.findall(r"mul\([0-9]+,[0-9]+\)", all_input)

res1 = 0
for match in all_match:
    nums = [int(x) for x in re.findall("[0-9]+", match)]
    res1 += nums[0] * nums[1]
print(res1)


all_match2 = re.findall(r"(mul\([0-9]+,[0-9]+\))|(don't)|(do)", all_input)

res2 = 0
read_state = True
for instr in all_match2:
    if "don't" in instr:
        read_state = False
    elif "do" in instr:
        read_state = True
    elif "mul" in instr[0]:
        if read_state:
            nums = [int(x) for x in re.findall("[0-9]+", instr[0])]
            res2 += nums[0]*nums[1]

print(res2)
