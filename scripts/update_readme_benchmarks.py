import json
import os

benchmark_names = set()
benches_dir = "target/criterion"
for dir in os.listdir(path=benches_dir):
    benchmark_names.add(dir.strip(" BASE").strip(" CRATE"))

benchmarks = []
for benchmark_name in benchmark_names:
    def load_estimate(suffix, subdir):
        with open(f"{benches_dir}/{benchmark_name} {suffix}/{subdir}/estimates.json", "r") as f:
            d = json.load(f)
            return int(d["median"]["point_estimate"])

    bw = load_estimate("BASE", "web")
    lw = load_estimate("CRATE", "web")
    bn = load_estimate("BASE", "native")
    ln = load_estimate("CRATE", "native")
    benchmarks.append((benchmark_name, bw, lw, bn, ln))

lines = "\n".join(f"| {name} | {bw}ns | {lw}ns | {bn}ns | {ln}ns |" for (name, bw, lw, bn, ln) in benchmarks)


with open("README.md", "r") as f_readme:
    readme = f_readme.read()

    section_header = "# Performance"
    section_start = readme.find(section_header) + len(section_header)
    section_end = readme.find("#", section_start)

    readme = readme[0:section_start] + f"""

| Benchmark | Base (Web) | λ-Wasm (Web) | Base (Native) | λ-Wasm (Native) |
| --- | ---: | ---: | ---: | ---: |
{lines}

""" + readme[section_end:]

with open("README.md", "w") as f_readme:
    f_readme.write(readme)