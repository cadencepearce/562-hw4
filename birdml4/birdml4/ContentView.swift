// With code from Simone Giordano:
// https://github.com/simgio99/envsoundclassifier/blob/main/envsoundclassifier/ListenButton.swift

import SwiftUI
struct ContentView: View {
    
    @ObservedObject var observer: AudioStreamObserver
    @State var text: String = ""
    private var streamManager: AudioStreamManager
    
    init() {
        observer = AudioStreamObserver()
        streamManager = AudioStreamManager()
        streamManager.resultObservation(with: observer)
    }
    var body: some View {
        VStack {
            Spacer()
            Text(observer.currentSound)
                    .padding()
                ChartView(observer: observer)
        
            Spacer()
            ListenButton(streamManager: streamManager)
               
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
