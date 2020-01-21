

def read_from_file(file_name: str = "dataset.txt"):
    with open(file_name, "r") as f:
        attributes_line = f.read()
        attributes = attributes_line.split()


def ID3(examples, target_attribute, attributes):
    print("SHIT")


if __name__ == "__main__":
    print("hello")
