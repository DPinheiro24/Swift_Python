//
//  Predios.swift
//  Cities
//
//  Created by Daniel Martins on 09/07/2023.
//

import Foundation
//[{"predio_id":1,"predio_nome":"PrÃ©dio 2","predio_tipo":"Residencial","cidade_nome":"SÃ£o Paulo"}
typealias Predios = [Predio]
struct Predio:Codable,Identifiable, CustomStringConvertible{
    var description: String {
            "Predio: \(predio_nome ?? "") Tipo: \(predio_tipo ?? "") Cidade: \(cidade_nome ?? "")"
        }
    var id : Int?
    var predio_nome : String?
    var predio_tipo: String?
    var cidade_nome: String?
}
