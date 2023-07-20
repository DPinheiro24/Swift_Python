//
//  Moradores.swift
//  Cities
//
//  Created by Daniel Martins on 09/07/2023.
//

import Foundation
typealias Moradores = [Morador]

struct Morador: Codable,CustomStringConvertible{
    var description: String{
    "Nome: \(pessoa_nome) Emprego: \(emprego) \n"
    }
 var  pessoa_nome : String
 var emprego: String
    
}
