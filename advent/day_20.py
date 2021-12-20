from pathlib import Path


def load_scanner_image(path: Path) -> tuple[str, list[str]]:
    with open(path, "r") as file:
        data = file.read()
    data = data.replace(".", "0")
    data = data.replace("#", "1")
    enhancement_algorithm, input_image = data.split("\n\n")
    input_image = input_image.split("\n")
    return enhancement_algorithm, input_image


def pad_image(input_image: list[str], padding: str = "0"):
    input_image = input_image.copy()
    nrows = len(input_image)
    input_image = [padding * nrows] + input_image + [padding * nrows]
    input_image = [padding + row + padding for row in input_image]
    return input_image


def enhance_image(input_image: list[str], algorithm: str):
    output_image = [row[1:-1] for row in input_image[1:-1]]
    nrows, ncols = len(input_image), len(input_image[0])
    pixels = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    for idx_row, row in enumerate(input_image):
        if idx_row == 0 or idx_row == nrows - 1:
            continue
        for idx_col, col in enumerate(row):
            if idx_col == 0 or idx_col == ncols - 1:
                continue
            string = ""
            for prow, pcol in pixels:
                string += input_image[idx_row + prow][idx_col + pcol]
            new_row = list(output_image[idx_row - 1])
            new_row[idx_col - 1] = algorithm[int(string, 2)]
            output_image[idx_row - 1] = "".join(new_row)
    return output_image


def main():
    algo, image = load_scanner_image(Path("../data/day_20_data.txt"))

    for _ in range(25):
        for _ in range(2):
            for _ in range(10):
                image = pad_image(image)
            image = enhance_image(image, algo)
        image = image[15:-15]
        image = [row[15:-15] for row in image]

    count = 0
    for row in image:
        count += row.count("1")
    print(count)


if __name__ == "__main__":
    main()
