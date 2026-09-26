import PDFKit
let a = CommandLine.arguments
guard let d = PDFDocument(url: URL(fileURLWithPath: a[1])) else { print("fail"); exit(1) }
print(d.pageCount)
try! (d.string ?? "").write(toFile: a[2], atomically: true, encoding: .utf8)
