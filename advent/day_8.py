from pathlib import Path


def read_displays(path: Path):
    with open(path, "r") as file:
        data = file.read()
    data = data.split("\n")

    input_lines, output_lines = [], []
    for line in data:
        input_values, output_values = [], []
        ivals, ovals = line.split("|")
        for ival in ivals.split():
            input_values.append(set(sorted(ival)))
        for oval in ovals.split():
            output_values.append(set(sorted(oval)))
        input_lines.append(input_values)
        output_lines.append(output_values)
    return input_lines, output_lines


def get_pattern(inputs):
    patterns = {"069": [], "235": []}
    for inp in inputs:
        length = len(inp)
        if length == 2:
            patterns["1"] = inp
        elif length == 3:
            patterns["7"] = inp
        elif length == 4:
            patterns["4"] = inp
        elif length == 7:
            patterns["8"] = inp
        elif length == 6:
            if inp not in patterns["069"]:
                patterns["069"].append(inp)
        elif length == 5:
            if inp not in patterns["235"]:
                patterns["235"].append(inp)

    eg = patterns["8"] - (patterns["4"] | patterns["7"])

    for num in patterns["069"]:
        if eg - num:
            patterns["9"] = num
            patterns["069"].remove(num)

    cd = patterns["069"][0] ^ patterns["069"][1]
    c = cd & patterns["1"]
    f = c ^ patterns["1"]
    zero = patterns["069"][0] if c & patterns["069"][0] else patterns["069"][1]
    patterns["0"] = zero
    patterns["069"].remove(zero)
    patterns["6"] = patterns.pop("069")[0]

    for num in patterns["235"]:
        if not c & num:
            patterns["5"] = num
        elif not f & num:
            patterns["2"] = num
        else:
            patterns["3"] = num
    patterns.pop("235")
    return patterns


def main():
    inputs, outputs = read_displays(Path("./data/day_8_data.txt"))

    combined_outputs = []
    for out in outputs:
        combined_outputs.extend(out)

    count = 0
    for out in combined_outputs:
        if len(out) in [2, 4, 3, 7]:
            count += 1
    print(f"Total number of one, four, seven, eight in output values is {count}!")

    values = []
    for inp, out in zip(inputs, outputs):
        pattern = get_pattern(inp)
        number = ""
        for value in out:
            for pat in pattern:
                if value == pattern[pat]:
                    number += pat
        values.append(int(number))
    print(sum(values))
