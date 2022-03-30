/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */
package control;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.MultipartConfig;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author friend
 */
@WebServlet(name = "ControlUpload", urlPatterns = {"/ControlUpload"})
@MultipartConfig
public class ControlUpload extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try ( PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */

            out.println("servlet de upload ok");
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        /*
        String description = request.getParameter("description"); // Retrieves <input type="text" name="description">
        Part filePart = request.getPart("file"); // Retrieves <input type="file" name="file">
        String fileName = Paths.get(filePart.getSubmittedFileName()).getFileName().toString(); // MSIE fix.
        InputStream fileContent = filePart.getInputStream();

        File file = new File("/tmp/", fileName);
        //File file = new File("/tmp/", "somefilename.ext");

        try ( InputStream input = filePart.getInputStream()) {
            Files.copy(input, file.toPath());
        } catch (Exception ex) {
            System.out.println("Erro: "+ex.getMessage());
        }

         */
        // remover extensão para descobrir nome da classe
        //String fileNameWithoutExtension = fileName.substring(0, fileName.indexOf("."));
        String fileNameWithoutExtension = "AllCaps";

        // carregar classe
        
        File f = new File("file:/home/friend/01-github/dw2ed/fund/webap/monojava/98-microkernel-class-for-loading/build/classes");
        URL[] cp = {f.toURI().toURL()};
        URLClassLoader urlcl = new URLClassLoader(cp);
        try {
            Class myclass = urlcl.loadClass("plugin." + fileNameWithoutExtension);
            //request.setAttribute("message", "File " + fileName + " has uploaded");
            
            request.setAttribute("message", "File " + fileNameWithoutExtension + " has uploaded");
            getServletContext().getRequestDispatcher("/result.jsp").forward(request, response);
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(ControlUpload.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
