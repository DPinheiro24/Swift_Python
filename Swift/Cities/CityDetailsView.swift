import SwiftUI

struct CityDetailsView: View {
    let city: Cidade
    @StateObject var vm = ContentViewModel()
    @State private var buildings: [CidadePredio] = []
    @State private var selectedBuilding: CidadePredio?
    @State private var residents: [Morador] = []
    @Environment(\.presentationMode) var presentationMode
    private let isGuest: Bool

    init(city: Cidade, isGuest: Bool = false) {
        self.city = city
        self.isGuest = isGuest
    }
    
    var body: some View {
        NavigationView {
            VStack {
                Text(city.cidade_nome)
                    .font(.largeTitle)
                    .fontWeight(.bold)
                    .padding(.bottom, 20)
                
                if !buildings.isEmpty {
                    Text("Buildings:")
                        .font(.title)
                        .foregroundColor(.blue)
                    
                    ScrollView {
                        LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 20) {
                            ForEach(buildings, id: \.predio_nome) { building in
                                if !building.predio_nome.isEmpty && !building.predio_tipo.isEmpty {
                                    NavigationLink(destination: BuildingResidentsView(building: building, isGuest: isGuest)) {
                                        VStack {
                                            Image(systemName: "building")
                                                .font(.system(size: 60))
                                                .foregroundColor(.blue)
                                                .padding()
                                            
                                            Text("\(building.predio_tipo) \(building.predio_nome)")
                                                .font(.headline)
                                                .foregroundColor(.blue)
                                                .multilineTextAlignment(.center)
                                        }
                                        .frame(maxWidth: .infinity)
                                        .padding()
                                        .background(Color.white)
                                        .cornerRadius(10)
                                    }
                                }
                            }
                        }
                        .padding(.horizontal, 20)
                    }
                } else {
                    Text("No buildings found")
                        .font(.title)
                        .foregroundColor(.gray)
                        .padding(.bottom, 20)
                }
                
                Spacer()
                
                Button(action: {
                    presentationMode.wrappedValue.dismiss()
                }) {
                    Text("Return")
                        .font(.headline)
                        .foregroundColor(.white)
                        .padding()
                        .background(Color.blue)
                        .cornerRadius(10)
                }
                .padding()
            }
            .padding()
            .onAppear {
                fetchBuildings()
            }
        }
    }
    
    func fetchBuildings() {
        Task {
            do {
                let buildingsData = try await vm.getDataOneCidade.getCidade(nome: city.cidade_nome)
                buildings = buildingsData
            } catch {
                print("Error fetching buildings for \(city.cidade_nome): \(error)")
            }
        }
    }
}
