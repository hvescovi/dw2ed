/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package plugin;

/**
 *
 * @author friend
 */
public class AllCaps {

    private String pluginName = "AllCaps";
    private String pluginDescription = "Convert all characters to uppercase";

    public String getPluginName() {
        return pluginName;
    }

    public void setPluginName(String pluginName) {
        this.pluginName = pluginName;
    }

    public String getPluginDescription() {
        return pluginDescription;
    }

    public void setPluginDescription(String pluginDescription) {
        this.pluginDescription = pluginDescription;
    }
    
    
    public String pluginAction(String parameter) {
        return parameter.toUpperCase();
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // teste da classe
        AllCaps ac = new AllCaps();
        System.out.println(ac.pluginAction("Deixe-me maiúsculo"));                
    }
    
}