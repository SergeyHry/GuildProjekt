package com.makelovenotwar.mvp.repository;

import com.makelovenotwar.mvp.entity.UserInfoEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserInfoRepository extends JpaRepository<UserInfoEntity, Long> {
    // Spring Boot generiert hier automatisch alle Befehle wie .findAll(), .save(), .findById() etc. hinter den Kulissen!
}