// src/main/java/com/example/servidorbiblioteca/repository/ItemRepository.java
package com.example.servidorbiblioteca.repository;

import com.example.servidorbiblioteca.model.Item;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ItemRepository extends JpaRepository<Item, Long> {
}
