/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package test;

import java.io.File;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;

/**
 *
 * @author friend
 */
public class TesteLoad {

    public static void main(String[] args) {

        String className = "plugin.AllCaps";

        File file = new File("/home/friend/01-github/dw2ed/fund/webap/monojava/98-microkernel-class-for-loading/build/classes/");

        try {
            // Convert File to a URL
            URL url = file.toURI().toURL();          // file:/c:/myclasses/
            URL[] urls = new URL[]{url};

            // Create a new class loader with the directory
            ClassLoader cl = new URLClassLoader(urls);

            // Load in the class; MyClass.class should be located in
            // the directory file:/c:/myclasses/com/mycompany
            //Class cls = cl.loadClass("com.mycompany.MyClass");
            Class cls = cl.loadClass(className);

            try {
                Constructor<?> constructor = cls.getConstructor();
                Object obj = constructor.newInstance();

                Method m;

                m = obj.getClass().getMethod("pluginAction", String.class);
                
                System.out.println("resultado do método: " + 
                        m.invoke(obj, "Aplicado nesta frase"));
                
            } catch (IllegalAccessException | 
                    IllegalArgumentException | 
                    InstantiationException | 
                    NoSuchMethodException | 
                    SecurityException | 
                    InvocationTargetException ex) {
                System.out.println("ERRO: "+ex.getMessage());
            }

            System.out.println("Execução OK");
        } catch (MalformedURLException | ClassNotFoundException e) {
            System.out.println(e.getMessage());
        }
        System.out.println("Fim do programa");

    }

}