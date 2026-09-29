package com.makelovenotwar.mvp.controller;
import com.makelovenotwar.mvp.dto.LoginRequest;
import com.makelovenotwar.mvp.repository.UserRepository;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import java.util.HashMap;
import java.util.Map;

public class UserAuthController {
    private final UserRepository userRepository;

    public UserAuthController(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    @PostMapping("/api/auth/login")
    public Map<String, String> login(@RequestBody LoginRequest request) {

        // Hier wird später die Logik passieren

        Map<String, String> response = new HashMap<>();
        response.put("status", "success");
        response.put("message", "Login erfolgreich für: " + request.getEmail());

        return response;
    }
}
