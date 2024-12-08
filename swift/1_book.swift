
import Foundation

func test1() {
    print("[test_1]_")
}

func test2() {
    print("[test_2]_")
}

func main() {
    test1()
    test2()
}

if CommandLine.arguments.count > 1 {
    do {
        main()
    } catch {
        print("[\(error)]")
    }
}
