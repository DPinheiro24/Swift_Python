//
//  LoadData.swift
//  Cities
//
//  Created by Daniel Martins on 08/07/2023.
//

import Foundation
class LoadData:ObservableObject{
    var baseURL:URL
    init(url:String) {
        if let url = URL(string: url) {
                   self.baseURL = url
               } else {
                   fatalError("URL Invalida! \(url)")
               }
    }
    //Funcao para ir buscar todas as pessoas
    func getPessoa() async throws -> [Pessoa]{
        let req = URLRequest(url: self.baseURL)
        let (data,httpResp) = try await URLSession.shared.data(for:req)
        
        guard (httpResp as? HTTPURLResponse)?.statusCode == 200 else{
            fatalError("Erro na resposta do http")
        }
        let listaPessoas = try JSONDecoder().decode(Pessoas.self, from: data)
        
        return listaPessoas
    }
    //Funcao para ir buscar uma pessoa
    func getPessoa(nome: String) async throws -> Pessoa{
        
        self.baseURL.appendPathComponent("\(nome)")
        let req = URLRequest(url: self.baseURL)
        let (data,httpResp) = try await URLSession.shared.data(for:req)
        
        guard (httpResp as? HTTPURLResponse)?.statusCode == 200 else{
            fatalError("Erro na resposta do http")
        }
        let pessoa = try JSONDecoder().decode(Pessoa.self, from: data)
        
        self.baseURL.deleteLastPathComponent()
        
        return pessoa
    }
    //função vai buscar todos os predios
        func getPredio() async throws -> [Predio]{
            let req = URLRequest(url: self.baseURL)
            let (data,httpResp) = try await URLSession.shared.data(for:req)
            
            guard (httpResp as? HTTPURLResponse)?.statusCode == 200 else{
                fatalError("Erro na resposta do http")
            }
            let listaPredios = try JSONDecoder().decode(Predios.self, from: data)
            
            return listaPredios
        }
    // função vai buscar todos os moradores de um predio
    func getPredio(nome: String) async throws -> Moradores {
        self.baseURL.appendPathComponent("\(nome)")
        let req = URLRequest(url: self.baseURL)
        let (data, httpResp) = try await URLSession.shared.data(for: req)
        
        guard (httpResp as? HTTPURLResponse)?.statusCode == 200 else {
            fatalError("Erro na resposta do http")
        }
        
        let moradores = try JSONDecoder().decode(Moradores.self, from: data)
        
        
        return moradores
    }


    // função vai buscar todos os predios numa cidade
    func getCidade(nome: String) async throws -> [CidadePredio] {
        self.baseURL.appendPathComponent("\(nome)")
        let req = URLRequest(url: self.baseURL)
        let (data, httpResp) = try await URLSession.shared.data(for: req)
        
        guard (httpResp as? HTTPURLResponse)?.statusCode == 200 else {
            fatalError("Erro na resposta do http")
        }
        
        let jsonArray = try JSONDecoder().decode([[String]].self, from: data)
        
        if jsonArray.isEmpty {
            return [CidadePredio(predio_nome: "", predio_tipo: "")]
        } else {
            let cidadepredios = jsonArray.map { innerArray -> CidadePredio in
                guard innerArray.count >= 2 else {
                    fatalError("Invalid format in inner array")
                }
                let predio_nome = innerArray[0]
                let predio_tipo = innerArray[1]
                return CidadePredio(predio_nome: predio_nome, predio_tipo: predio_tipo)
            }
            
            self.baseURL.deleteLastPathComponent()
            
            return cidadepredios
        }
    }



    
    //função vai buscar todas as cidades
        func getCidade() async throws -> [Cidade]{
            let req = URLRequest(url: self.baseURL)
            let (data,httpResp) = try await URLSession.shared.data(for:req)
            
            guard (httpResp as? HTTPURLResponse)?.statusCode == 200 else{
                fatalError("Erro na resposta do http")
            }
            let listaCidades = try JSONDecoder().decode(Cidades.self, from: data)
            
            return listaCidades
        }
    
    // funcao para criar cidade
    func createCity(nome: String) async throws -> Cidade {
            let url = URL(string: "http://127.0.0.1:8000/cidade")!
            var request = URLRequest(url: url)
            request.httpMethod = "POST"
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")
            
            let body = ["nome": nome]
            request.httpBody = try JSONEncoder().encode(body)
            
            let (data, _) = try await URLSession.shared.data(for: request)
            return try JSONDecoder().decode(Cidade.self, from: data)
        }
 

}
