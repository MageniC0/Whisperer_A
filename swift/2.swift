import SwiftUI

// 参数结构体
struct Params {
    var m: String
    var n: String
}

struct ContentView: View {
    @State private var inputText = ""
    @State private var params: Params?
    
    var body: some View {
        VStack {
            TextField("", text: $inputText)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            Button(action: {
                handleInput(input: inputText)
            }) {
                Image(systemName: "pencil.line")
                    .font(.title)
            }
        }
    }
    
    private func handleInput(input: String) {
        switch input {
        case "a":
            test1()
        case let x where x.hasPrefix("b "):
            if let (m, n) = parseInput(input) {
                self.params = Params(m: m, n: n)
                test2(params: self.params)
            }
        default:
            print("?")
        }
    }
}

func test1() {
    print("[test_1]_________")
    print("(一些信息)")
}

func test2(params: Params?) {
    guard let params = params else { return }
    print("[test_2]_________")
    print("收到参数m = \(params.m), n = \(params.n)")
}

// 类似于正则表达式的设计
func parseInput(_ input: String) -> (m: String, n: String)? {
    guard input.hasPrefix("b ") else { return nil }
    let parts = input.dropFirst(2).split(separator: " ")
    guard parts.count == 2 else { return nil }
    return (String(parts[0]), String(parts[1]))
}

@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

