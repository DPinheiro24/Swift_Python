//
//  Cidades.swift
//  Cities
//
//  Created by Daniel Martins on 09/07/2023.
//

import Foundation

typealias Cidades = [Cidade]
//[{"cidade_id":1,"cidade_nome":"SÃ£o Paulo"}
struct Cidade: Codable, Identifiable, CustomStringConvertible {
    var description: String {
        "Cidade: \(cidade_nome)"
    }
    
    var id: Int { cidade_id } // Use cidade_id as the identifier property
    
    let cidade_id: Int
    let cidade_nome: String
    
}


