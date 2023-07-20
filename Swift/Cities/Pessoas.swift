//
//  Pessoas.swift
//  Cities
//
//  Created by Daniel Martins on 08/07/2023.
//

//[{"pessoa_id":1,"pessoa_nome":"JoÃ£o","emprego":"Professor","predio_nome":"PrÃ©dio1"}

import Foundation

typealias Pessoas = [Pessoa]

struct Pessoa:Codable,Identifiable, CustomStringConvertible{
    var description: String{
        "nome: \(pessoa_nome) profissao: \(emprego) "
    }
    var id : Int?
    var pessoa_nome : String
    var emprego: String
    var predio_nome : String
}
