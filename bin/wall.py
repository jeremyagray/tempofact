"""Generate a wall calendar."""

import datetime
import sys

header = """\\documentclass[12pt]{article}
\\usepackage{lmodern}
\\usepackage[margin=0.5in]{geometry}
\\usepackage{tcolorbox}
\\pagestyle{empty}

\\setlength{\\parindent}{0pt}

\\newtcolorbox{datebox}{
  halign=justify,
  valign=center,
  nobeforeafter,
  width=1.6in,
  height=1.5in,
  sharp corners,
  colback=white
}

\\newtcolorbox{holidaybox}{
  top=0in,
  right=0in,
  bottom=0in,
  left=0in,
  before skip=0in,
  right skip=0in,
  after skip=0in,
  left skip=0in,
  nobeforeafter,
  width=3.9in,
  height=1.5in,
  sharp corners,
  colback=white
}

\\newtcolorbox{eventbox}{
  top=0in,
  right=0in,
  bottom=0in,
  left=0in,
  before skip=0in,
  right skip=0in,
  after skip=0in,
  left skip=0in,
  width=5.5in,
  height=4in,
  sharp corners,
  colback=white
}

\\begin{document}
"""

footer = """\\end{document}
"""


def generate():
    """Generate a wall calendar."""
    month = int(sys.argv[1])
    year = int(sys.argv[2])

    this = datetime.datetime(year=year, month=month, day=1)
    next = datetime.datetime(year=year, month=month + 1, day=1)
    days = (next - this).days

    print(header)

    for day in range(1, days + 1):
        print(
            """\\begin{datebox}
  {\\fontsize{1in}{1in}\\textbf{"""
            + str(day)
            + """}}
\\end{datebox}%
\\begin{holidaybox}
  \\begin{LARGE}
  \\end{LARGE}
\\end{holidaybox}

\\begin{eventbox}
  \\begin{LARGE}
  \\end{LARGE}
\\end{eventbox}
"""
        )
        if day != days:
            print("\\pagebreak")

    print(footer)


if __name__ == "__main__":
    sys.exit(generate())
