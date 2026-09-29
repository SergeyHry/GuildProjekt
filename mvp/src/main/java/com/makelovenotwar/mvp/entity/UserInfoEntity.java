package com.makelovenotwar.mvp.entity;
import jakarta.persistence.*;

@Entity // Sagt Spring Boot: Das ist eine Datenbank-Tabelle!
@Table(name = "user_info")
public class UserInfoEntity {

    @Id
    private Long userId;

    @OneToOne
    @MapsId
    @JoinColumn(name = "user_id")
    private UserEntity user;

    private String firstname;
    private String lastname;
    private String nickname;
    private String address;
    private String bio;
    private String phone;

    // Getter / Setter

    // Getter und Setter (wichtig, damit Java die Daten lesen kann)
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getBio() {
        return bio;
    }

    public void setBio(String bio) {
        this.bio = bio;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
}