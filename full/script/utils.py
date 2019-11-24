import re
import sys


pattern_flag = re.IGNORECASE
pattern_map = {
    "go": re.compile(r"go(\d+)\.(\d+)\.(\d+)\s", pattern_flag),
    "python": re.compile(r"^Python\s+(\d+)\.(\d+)\.(\d+)$", pattern_flag),
    "pip": re.compile(r"^pip\s+(\d+)\.(\d+)\.(\d+)\s", pattern_flag),
    "node": re.compile(r"^v(\d+)\.(\d+)\.(\d+)$", pattern_flag),
    "npm": re.compile(r"^(\d+)\.(\d+)\.(\d+)$", pattern_flag),
}


def version_string(version):
    if version is None:
        return ""
    return str.join(".", [str(n) for n in version])


def extract_version(lang, raw):
    if lang not in pattern_map:
        return None
    pattern = pattern_map[lang]
    found = pattern.search(raw)
    if found is None:
        return None
    match = found.groups()
    version = []
    for s in match:
        version.append(int(s))
    return tuple(version)


def parse_version_from_stdin():
    # read from stdin
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    # parse all lines
    versions = {}
    for l in lines:
        parts = l.split(":", 1)
        lang = parts[0].lower()
        raw_version = parts[1].strip()
        version = extract_version(lang, raw_version)
        if version is not None and len(version) >= 1:
            versions[lang] = version
    return versions
