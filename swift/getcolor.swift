import SwiftUI
struct 滑动条: View {
    @Binding var 颜色值: Double
    var body: some View {
        HStack {
            Button(action: {
                if 颜色值 > 0 {
                    颜色值 -= 1
                }
            }) {
                Image(systemName: "plus.square")
            }
            .padding()
            Slider(value: $颜色值, in: 0...255, step: 1) {
            }
            TextField("", value: Binding(get: { 颜色值 }, set: { 新的颜色值 in
                颜色值 = min(max(0, 新的颜色值), 255)
            }), formatter: 格式化())
            .frame(width: 80)
            .textFieldStyle(RoundedBorderTextFieldStyle())
            .keyboardType(.numberPad)
            Button(action: {
                if 颜色值 < 255 {
                    颜色值 += 1
                }
            }) {
                Image(systemName: "minus.square")
            }
            .padding()
        }
    }
    
    func 格式化() -> NumberFormatter {
        let 格式 = NumberFormatter()
        格式.numberStyle = .none
        return 格式
    }
}
struct 视图: View {
    @State private var 颜色: [Double] = [255, 255, 255]
    
    var body: some View {
        VStack {
            Rectangle()
                .fill(Color(red: 颜色[0] / 255, green: 颜色[1] / 255, blue: 颜色[2] / 255))
                .frame(width: 400, height: 300)
                .padding()
            
            ForEach(0..<3, id: \.self) { index in
                滑动条(颜色值: $颜色[index])
            }
        }
    }
    
}
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            视图()
        }
    }
}
