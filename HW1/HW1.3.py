import sys

if len(sys.argv) > 1:
    for filename in sys.argv[1:]:
        f = open(filename, "rb")
        content = f.read()
        byte_count = len(content)

        f = open(filename, "r",encoding="utf-8")
        lines = f.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        print(line_count,word_count, byte_count,filename)

else:
    f = sys.stdin.read()
    byte_count = len(f.encode("utf-8"))
    lines = f.splitlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    print(line_count,word_count, byte_count, "stdin")


