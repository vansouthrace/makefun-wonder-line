import os

ENTRY = 'Somewhere right now, light that left its star before humans existed is landing on your skin — and you call it Tuesday.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
