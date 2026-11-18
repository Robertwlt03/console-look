import Testing

@testable import ConsoleLook

@Test("Every line of a frame is as wide as its border")
func frameLinesLineUp() {
    let frame = Console.framed("Built", details: ["build/App.app", "longer detail"], passed: true)
    let lines = frame.split(separator: "\n")
    // Without the color codes, so FORCE_COLOR does not change what is measured.
    let widths = Set(lines.map { line in line.replacing(/\u{1B}\[[0-9;]*m/, with: "").count })
    #expect(lines.count == 5)  // border, outcome, two details, border
    #expect(widths.count == 1)
}

@Test("A failed frame shows the failed mark")
func failedFrameShowsItsMark() {
    #expect(Console.framed("Tests failed", details: [], passed: false).contains("✘ Tests failed"))
}
