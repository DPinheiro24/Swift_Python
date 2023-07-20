//
//  ContentViewModel.swift
//  Cities
//
//  Created by Daniel Martins on 08/07/2023.
//

import Foundation
class ContentViewModel:ObservableObject{
    var getDataOnePessoa = LoadData(url: "http://127.0.0.1:8000/pessoa")
    var getDataTodasPessoas = LoadData(url: "http://127.0.0.1:8000/pessoas")
    var getDataOnePredio = LoadData(url:"http://127.0.0.1:8000/predio")
    var getDataTodosPredios = LoadData(url: "http://127.0.0.1:8000/predios")
    var getDataOneCidade = LoadData(url: "http://127.0.0.1:8000/cidade")
    var getDataAllCidades = LoadData(url: "http://127.0.0.1:8000/cidades")
}

