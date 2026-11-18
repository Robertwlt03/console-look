# console-look

One shared look for everything your scripts and tools print in a terminal, in Python and in Swift:
a heading, result lines with a mark, dimmed details and hints, and a frame that sums up.

```text
Build  release

 ✔ Compiled  12.4 s
 ✔ Signed  Developer ID
 › Packing the disk image
 ╭────────────────╮
 │ ✔ Built        │
 │   dist/App.dmg │
 ╰────────────────╯
```

## What it does

- **Same pieces everywhere:** `heading`, `passed`, `failed`, `step`, `note`, `stopped`, `frame`
  and `data` in Python and Swift; Python adds `group`, `entry`, `table` and a spinner while a
  command runs.
- **Questions (Python):** yes or no, a line of text with a check, or a list to walk with the arrow
  keys.
- **Any language:** Python imports it, Swift adds it as a package, and make, shells or other
  languages call the `console-look` command one piece at a time.
- **Behaves in logs:** no spinner and no color outside a terminal, colors on GitHub Actions
  (Python), and `NO_COLOR` or `FORCE_COLOR` to decide yourself
  ([no-color.org](https://no-color.org)).
- **Nothing to install besides itself:** the Python half uses only the standard library.

## Install

Python 3.13 or newer, on macOS or Linux:

```bash
pip install git+https://github.com/Robertwlt03/console-look@v0.1.0
```

Swift 6, in `Package.swift`:

```swift
.package(url: "https://github.com/Robertwlt03/console-look", from: "0.1.0"),
```

Then add the product `ConsoleLook` to your target.

## Use

In Python:

```python
import console_look as console

console.heading("Build", "release")
console.passed("Compiled", "12.4 s")
if console.wait("Packing the disk image", ["hdiutil", "create", "…"]) != 0:
    console.stopped("Packing failed", hints=("Run it again with more space free",))
console.frame("Built", ["dist/App.dmg"], console.SUCCESS)
```

From make or a shell:

```make
build:
	console-look heading "Build" "release"
	console-look wait "Compiling" swift build -c release
	console-look frame success "Built" ".build/release/App"
```

In Swift:

```swift
import ConsoleLook

Console.heading("Self test")
Console.passed("Sizes match du", detail: "12 folders")
Console.frame("All checks held", details: ["12 folders"], passed: true)
```

## How it works

- **One heading per command:** the first heading sets `CONSOLE_HEADED`, so a script that another
  command starts leaves out its own.
- **Steps of a bigger command:** with `CONSOLE_STEP` set, a frame shrinks to one result line, so
  only the outer command draws a frame.
- **Spacing:** only the heading starts with a blank line, and every block ends with one, so two
  blank lines never meet.
- **Plain data:** `data` prints text another program reads, such as GitHub's workflow commands,
  never colored.

## Contribute

Issues and pull requests are welcome. Before a pull request, run both test suites:

```bash
PYTHONPATH=src python3 -m unittest discover -s Tests
```

```bash
swift test
```

## License

[MIT](LICENSE)
