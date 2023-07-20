//
//  ContentView.swift
//  Cities
//
//  Created by Daniel Martins on 08/07/2023.
//

import SwiftUI


struct ContentView: View {
    var body: some View {
        LoginViewController()
    }
}


    
  //  @StateObject var vm = ContentViewModel()
   // var body: some View {
        //Text("Hello, world!")
           // .padding()
            /*.task{
                do{
                    //Pesquisar por uma pessoa
                   /* let pessoa = try await vm.getDataOnePessoa.getPessoa(nome: "Maria")
                    print(pessoa)
                    //todas as pessoas na DB
                    let pessoas = try await vm.getDataTodasPessoas.getPessoa()
                    print(pessoas)*/
                    //Todos os moradores num predio
                   /* let predio = try await vm.getDataOnePredio.getPredio(nome: "Prédio 2")
                    print("Predio 2 : ",predio)
                    //Todos os predios
                    let predios = try await vm.getDataTodosPredios.getPredio()
                    print(predios)*/
                    //Todos os predios numa cidade
                   /*let cidade = try await vm.getDataOneCidade.getCidade(nome: "Cidade de Sol")
                    print (cidade)
                    //Todas as cidades
                   let cidades = try await vm.getDataAllCidades.getCidade()
                    print(cidades)*/
                    
                }
                catch{
                    print("ERRO:",error)
                }
            }*/



struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
