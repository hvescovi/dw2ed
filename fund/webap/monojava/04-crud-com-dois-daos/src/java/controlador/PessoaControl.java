package controlador;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */
import dao.PessoaDAO;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import modelo.Pessoa;

/**
 *
 * @author friend
 */
@WebServlet(urlPatterns = {"/pessoa"})
public class PessoaControl extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    // DAO para ser usado no servlet
    PessoaDAO pdao = new PessoaDAO();

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

        // ações get:
        // sem parâmetro: recuperar todos os elementos
        // com parâmetro r: recuperar elemento individual
        // com parâmetro d: excluir elemento
        // com parâmetro f: abrir formulário de inclusão
        
        String retrieve = request.getParameter("r");
        String delete = request.getParameter("d");
        String form = request.getParameter("f");
        if (retrieve != null) {
            // exibe alguém específico?
            try ( PrintWriter out = response.getWriter()) {
                /* TODO output your page here. You may use following sample code. */
                out.println("deve exibir alguém específico");
            }
        } else if (delete != null) {
            if (pdao.removerPessoa(delete)) {
                request.setAttribute("msg", "Pessoa removida com sucesso");
            } else {
                request.setAttribute("msg", "Ocorreu algum erro ao excluir a pessoa");
            }
            getServletContext().getRequestDispatcher("/mensagem.jsp")
                               .forward(request, response);                                
        } else if (form != null) {
             getServletContext().getRequestDispatcher("/form.jsp")
                               .forward(request, response);   
        } else { // exibe todos
            // obtém dados
            ArrayList<Pessoa> registros = pdao.retornarPessoas();
            // insere no request
            request.setAttribute("registros", registros);
            // encaminha a resposta 
            getServletContext().getRequestDispatcher("/listar.jsp").forward(request, response);            
            //response.sendRedirect(request.getContextPath() + "/listar.jsp");
        }

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

        // configuração para corrigir questões de acento
        request.setCharacterEncoding("utf8");
        
        String cpf = request.getParameter("nome");
        String nome = request.getParameter("nome");
        String email = request.getParameter("email");
        String telefone = request.getParameter("telefone");

        Pessoa nova = new Pessoa(cpf, nome, email, telefone);
        pdao.incluirPessoa(nova);

        request.setAttribute("msg", "Pessoa incluída com sucesso");
        getServletContext().getRequestDispatcher("/mensagem.jsp").forward(request, response);            
        //response.sendRedirect("mensagem.jsp");
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
