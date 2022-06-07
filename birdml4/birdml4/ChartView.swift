//
//  ChartView.swift
//  birdml4
//
//  Created by Cady Pearce on 6/6/22.
//
// With code from Simone Giordano:
// https://github.com/simgio99/envsoundclassifier/blob/main/envsoundclassifier/ListenButton.swift

import SwiftUI

struct ChartView: View {
    @ObservedObject var observer: AudioStreamObserver
    var body: some View {
        
        
        VStack(alignment: .leading) {
            RoundedRectangle(cornerRadius: 2.0)
                .foregroundColor(.clear)
                .frame(width: 250, height: 1)
            ForEach(0..<observer.topResults.count, id: \.self) { index in
                    RoundedRectangle(cornerRadius: 2.0)
                        .frame(width: 250 * observer.topResults[index].confidence, height: 20, alignment: .center)
                        .animation(.linear)
                }
            }
    }
}



struct ChartView_Previews: PreviewProvider {
    static var previews: some View {
        ChartView(observer: AudioStreamObserver())
    }
}
