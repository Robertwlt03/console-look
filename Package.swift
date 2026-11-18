// swift-tools-version:6.0
// The Swift half of console-look: the same terminal look as src/console_look.py.
//
// Start:  add https://github.com/Robertwlt03/console-look as a package dependency, then
//         import ConsoleLook; swift test runs the tests
// Needs:  Swift 6
import PackageDescription

let package = Package(
    name: "ConsoleLook",
    platforms: [.macOS(.v13)],  // Linux needs no entry; Swift Testing and Regex need macOS 13
    products: [
        .library(name: "ConsoleLook", targets: ["ConsoleLook"])
    ],
    targets: [
        .target(name: "ConsoleLook"),
        .testTarget(name: "ConsoleLookTests", dependencies: ["ConsoleLook"]),
    ]
)
