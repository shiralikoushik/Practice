class open_file:
    def __init__(koushik, f_name, mode):
        koushik.f_name = f_name
        koushik.mode = mode

    def __enter__(koushik):
        koushik.f = open(koushik.f_name, koushik.mode)
        return koushik.f

    def __exit__(koushik, exe_type, a, b):
        koushik.f.close()


with open_file("text.txt", "w") as f:
    f.write("Hi")

print(f.closed)
