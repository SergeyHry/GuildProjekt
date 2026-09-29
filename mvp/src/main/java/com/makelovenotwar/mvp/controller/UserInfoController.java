package com.makelovenotwar.mvp.controller;
import com.makelovenotwar.mvp.entity.UserInfoEntity;
import com.makelovenotwar.mvp.repository.UserInfoRepository;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

@RestController
public class UserInfoController {

    // Wir "injizieren" (holen) das Repository hier rein
    private final UserInfoRepository userRepository;

    public UserInfoController(UserInfoRepository userInfoRepository) {
        this.userRepository = userInfoRepository;
    }

    @GetMapping("/api/users")
    public List<UserInfoEntity> getAllUsers() {
        // Hier passiert die Magie: Hole alle User direkt aus der Datenbank!
        return userRepository.findAll();
    }

    @GetMapping("/api/users/{id}")
    public UserInfoEntity getUserById(@PathVariable Long id) {
        return userRepository.findById(id).orElse(null);
    }
}