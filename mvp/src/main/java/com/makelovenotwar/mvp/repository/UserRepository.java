package com.makelovenotwar.mvp.repository;
import com.makelovenotwar.mvp.entity.UserEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends JpaRepository<UserEntity, Long> {
    // Spring Boot generiert hier automatisch alle Befehle wie .findAll(), .save(), .findById() etc. hinter den Kulissen!
}