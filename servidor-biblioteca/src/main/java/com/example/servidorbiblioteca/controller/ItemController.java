// src/main/java/com/example/servidorbiblioteca/controller/ItemController.java
package com.example.servidorbiblioteca.controller;

import com.example.servidorbiblioteca.model.Item;
import com.example.servidorbiblioteca.repository.ItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/itens")
@CrossOrigin(origins = "*")
public class ItemController {

    @Autowired
    private ItemRepository itemRepository;

    @GetMapping
    public List<Item> listar() {
        return itemRepository.findAll();
    }

    @PostMapping
    public Item criar(@RequestBody Item item) {
        System.out.println("Criando item: " + item.getTitulo() + ", Autor: " + item.getAutor() + ", Tipo: " + item.getTipo());
        return itemRepository.save(item);
    }

    @GetMapping("/{id}")
    public Item buscar(@PathVariable Long id) {
        return itemRepository.findById(id).orElseThrow();
    }

    @PutMapping("/{id}")
    public Item atualizar(@PathVariable Long id, @RequestBody Item item) {
        item.setId(id);
        return itemRepository.save(item);
    }

    @DeleteMapping("/{id}")
    public void deletar(@PathVariable Long id) {
        itemRepository.deleteById(id);
    }
}
