import SwiftUI

// 定义一个结构体来存放用户输入的字符串形式的m和n
struct InputParams {
    var m: String
    var n: String
}

// 定义一个结构体来存放转换后的整数形式的m_和n_
struct CalculatedParams {
    var m_: Int
    var n_: Int
}

struct ContentView: View {
    // 使用@State存储用户输入的参数
    @State private var inputParams = InputParams(m: "", n: "")
    // 使用@State存储转换后的整数参数
    @State private var calculatedParams: CalculatedParams?
    // 使用@State存储计算结果
    @State private var result: Int?
    
    var body: some View {
        VStack {
            // 创建第一个输入框，用于输入m的值
            TextField("m", text: $inputParams.m)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            // 创建第二个输入框，用于输入n的值
            TextField("n", text: $inputParams.n)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            // 创建一个按钮，使用系统图标作为按钮内容
            Button(action: {
                // 按钮点击事件处理
                // 尝试将输入的字符串转换为整数并计算和
                guard let m_ = Int(inputParams.m), let n_ = Int(inputParams.n) else {
                    // 如果转换失败，不执行任何操作
                    return
                }
                let sum = m_ + n_
                // 打印结果到控制台
                print("[core]The sum is \(sum)")
                // 存储计算结果
                result = sum
                // 存储转换后的整数参数
                calculatedParams = CalculatedParams(m_: m_, n_: n_)
            }) {
                // 使用图标作为按钮内容
                Image(systemName: "pencil.line")
                    .font(/*@START_MENU_TOKEN@*/.title/*@END_MENU_TOKEN@*/)
            }
        }
    }
}

@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
