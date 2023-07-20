//
//  Cidade_Predio.swift
//  Cities
//
//  Created by Daniel Martins on 15/07/2023.
//

import Foundation
//["PrÃ©dio1","ApartLuxo"]]

typealias CidadePredios = [CidadePredio]

struct CidadePredio: Codable, CustomStringConvertible,Identifiable {
    var description: String {
        if isEmpty {
            return "Nao existe predios nesta cidade"
        } else {
            return "Predio: \(predio_nome) Tipo de Predio: \(predio_tipo)\n"
        }
    }
    var id: String {
           predio_nome
       }
    
    var predio_nome: String
    var predio_tipo: String
    
    var isEmpty: Bool {
        return predio_nome.isEmpty && predio_tipo.isEmpty
    }
}

