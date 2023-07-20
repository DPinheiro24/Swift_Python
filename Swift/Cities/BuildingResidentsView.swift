import SwiftUI

struct BuildingResidentsView: View {
    let building: CidadePredio
    @StateObject var vm = ContentViewModel()
    @State private var residents: [Morador] = []
    private let isGuest: Bool
    
    init(building: CidadePredio, isGuest: Bool = false) {
        self.building = building
        self.isGuest = isGuest
    }
    
    var body: some View {
        VStack {
            VStack(alignment: .leading, spacing: 10) {
                Text("Building:")
                    .font(.title)
                    .foregroundColor(.blue)
                
                Text("\(building.predio_nome)")
                    .font(.headline)
                    .fontWeight(.semibold)
                    .foregroundColor(.blue)
                
                if !isGuest {
                    Text("Residents:")
                        .font(.title)
                        .foregroundColor(.blue)
                } else {
                    Text("Guest users cannot view residents")
                        .font(.title)
                        .foregroundColor(.red)
                }
            }
            .padding()
            .background(Color.gray.opacity(0.2))
            .cornerRadius(10)
            .padding(.bottom, 10)
            
            if !isGuest {
                List(residents, id: \.pessoa_nome) { resident in
                    VStack(alignment: .leading) {
                        Text("\(resident.pessoa_nome)")
                            .font(.title2)
                            .fontWeight(.bold)
                            .foregroundColor(.primary)
                        
                        Text(resident.emprego)
                            .font(.subheadline)
                            .foregroundColor(.secondary)
                    }
                    .padding(.vertical, 8)
                    .padding(.horizontal, 16)
                    .background(Color.white)
                    .cornerRadius(10)
                    .padding(.horizontal)
                }
                .listStyle(GroupedListStyle())
                .onAppear {
                    Task {
                        await fetchResidents()
                    }
                }
            }
        }
        .navigationBarTitleDisplayMode(.inline)
    }
    
    func fetchResidents() async {
        do {
            let residentsData = try await vm.getDataOnePredio.getPredio(nome: building.predio_nome)
            residents = residentsData
        } catch {
            print("Error fetching residents for \(building.predio_nome): \(error)")
        }
    }
}
