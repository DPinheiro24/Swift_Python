import SwiftUI

struct LoginViewController: View {
    @State private var secretCode = ""
    @State private var isLogged = false
    @State private var navigateToCityList = false
    @State private var isGuest = false

    var body: some View {
        NavigationView {
            ZStack {
                Image("city_background")
                    .resizable()
                    .aspectRatio(contentMode: .fill)
                    .edgesIgnoringSafeArea(.all)
                
                VStack {
                    Spacer()
                    
                    HStack {
                        SecureField("Enter the secret code", text: $secretCode)
                            .textFieldStyle(RoundedBorderTextFieldStyle())
                            .frame(maxWidth: 150)
                        
                        Button("Submit") {
                            if secretCode == "1234" {
                                isLogged = true
                                navigateToCityList = true
                                isGuest = false
                                print("Logged in successfully!")
                            } else {
                                print("Incorrect secret code")
                            }
                        }
                        .font(.headline)
                        .padding(.leading, 10)
                        
                    }
                    .padding()
                    
                    Button("Enter as guest") {
                        isGuest = true
                        navigateToCityList = true
                        print("Entered as guest")
                    }
                    .font(.headline)
                    .padding()
                    .disabled(isLogged)
                    .opacity(isLogged ? 0.5 : 1.0)
                    .accentColor(.black)
                    .background(Color.gray.opacity(0.8))
                    .cornerRadius(10)
                    
                    Button("Logout") {
                        isLogged = false
                        secretCode = ""
                        isGuest = false
                        print("Logged out successfully!")
                    }
                    .font(.headline)
                    .padding()
                    .accentColor(.red)
                    .disabled(!isLogged)
                    .opacity(isLogged ? 1.0 : 0.5)
                    
                    Spacer()
                }
                .padding()
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .background(NavigationLink(destination: CityListView(isGuest: isGuest), isActive: $navigateToCityList) { EmptyView() })
            .navigationTitle("Login")
        }
    }
}
