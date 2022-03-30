/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package test;

import java.io.InputStream;

/**
 *
 * @author friend
 */
public class TesteLoad {
    
    public static void main(String[] args) {
        
        String className = "plugin.AllCaps";
        InputStream inputStream = CurrentClass.class.getClassLoader().getResourceAsStream(className.replace('.', '/') + ".class");
                
    }
    
}
