"""Entry for make.fun: The Robot Vacuum's Best Excuse.

A vacuum that skipped a spot to protect a crumb nature reserve.
"""
import os

LINE = "I didn't miss that spot — I left it as a nature reserve for the crumbs, who have lived there longer than you have."
MAX_CHARS = 140


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
