import SwiftUI

struct CityListView: View {
    @StateObject var vm = ContentViewModel()
    @State private var cities: [Cidade] = []
    @State private var selectedCity: Cidade?
    private let isGuest: Bool

    init(isGuest: Bool = false) {
        self.isGuest = isGuest
    }
    
    var body: some View {
        NavigationView {
            VStack {
                List(cities, id: \.id) { city in
                    Button(action: {
                        selectedCity = city
                    }) {
                        Text(city.cidade_nome)
                            .font(.title)
                            .foregroundColor(.white)
                            .padding(.vertical, 8)
                            .padding(.horizontal, 16)
                            .background(Color.blue)
                            .cornerRadius(10)
                    }
                    .buttonStyle(PlainButtonStyle())
                    .frame(maxWidth: .infinity, alignment: .center)
                }
                .onAppear {
                    fetchCities()
                }
                .navigationTitle("Cities")
                .sheet(item: $selectedCity) { city in
                    CityDetailsView(city: city, isGuest: isGuest)
                }
            }
        }
    }
    
    func fetchCities() {
        Task {
            do {
                let cidades = try await vm.getDataAllCidades.getCidade()
                cities = cidades
            } catch {
                print("Error fetching cities: \(error)")
            }
        }
    }
}
