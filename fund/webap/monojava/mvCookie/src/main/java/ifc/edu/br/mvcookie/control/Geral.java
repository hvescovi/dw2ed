/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */
package ifc.edu.br.mvcookie.control;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import java.io.IOException;
import java.io.PrintWriter;

/**
 *
 * @author friend
 */
@WebServlet(name = "Geral", urlPatterns = {"/Geral"})
public class Geral extends HttpServlet {

    // existe o cookie que define a autorização para uso do cookie?
    boolean autorizadoExiste = false;

    // pode usar cookies? Sim, se o cookie existe e está como "sim"
    boolean podeUsarCookies = false;

    // inicializa como false: quando o servlet é carregado, não analisou nada
    boolean analisouCookies = false;

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
        response.setContentType("text/html;charset=UTF-8");
        try ( PrintWriter out = response.getWriter()) {

            // ativar a sessão
            HttpSession sessao = request.getSession(true);

            // já analisou cookies?
            if (sessao.getAttribute("analisouCookies") != null) {
                analisouCookies = (boolean) sessao.getAttribute("analisouCookies");
            } else {
                analisouCookies = false;
            }

            if (!analisouCookies) {
                // se não havia analisado, agora vai analisar :-)
                // persiste essa informação na sessão de que já analisou os cookies
                sessao.setAttribute("analisouCookies", true);

                // analisa os cookies
                // livro goncalves2007desenvolvimento, pg 101
                Cookie listaCookies[] = request.getCookies();
                if (listaCookies != null) {
                    for (Cookie c : listaCookies) {
                        if (c.getName().equals("mvCookie-1-cookie-autorizado")) {
                            autorizadoExiste = true;
                            podeUsarCookies = c.getValue().equals("sim");
                            break;
                        }
                    }
                }
                // persiste as informações sobre os cookies de autorização e uso
                // para verificar na página JSP
                sessao.setAttribute("autorizadoExiste", autorizadoExiste ? "sim" : "não");
                sessao.setAttribute("podeUsarCookies", podeUsarCookies ? "sim" : "não");
            } else {
                // recupera valores analisados antes (fechou e abriu browser?)
                String autorizadoExisteSTR = (String) sessao.getAttribute("autorizadoExiste");
                autorizadoExiste = ((autorizadoExisteSTR != null) && (autorizadoExisteSTR.equals("sim")));

                if (autorizadoExiste) {
                    String podeUsarCookiesSTR = (String) sessao.getAttribute("podeUsarCookies");
                    podeUsarCookies = ((podeUsarCookiesSTR != null) && (podeUsarCookiesSTR.equals("sim")));

                }
            }

            String op = request.getParameter("op");
            if (op == null) {
                getServletContext().getRequestDispatcher("/inicial.jsp").forward(request, response);
            } else if (op.equals("um") || op.equals("dois") || op.equals("tres")) {
                if (op.equals("dois") && (podeUsarCookies)) {
                    // procura o cookie
                    Cookie listaCookies[] = request.getCookies();
                    if (listaCookies != null) {
                        for (Cookie c : listaCookies) {
                            if (c.getName().equals("mvCookie-1-visitasPGdois")) {
                                // incrementa o número de visitas
                                int v = Integer.parseInt(c.getValue());
                                v++;
                                String novoValor = String.valueOf(v);
                                // atualiza o cookie
                                c.setValue(novoValor);
                                response.addCookie(c);

                                // envia o valor das visitas para ser mostrado na página destino
                                request.setAttribute("visitas", novoValor);
                                break;
                            }
                        }
                    }
                }

                // tem cookies criados?
                String cookies = "";
                Cookie listaCookies[] = request.getCookies();
                if (listaCookies != null) {
                    for (Cookie c : listaCookies) {
                        cookies += c.getName() + "|";
                    }
                }
                sessao.setAttribute("cookies", cookies);

                getServletContext().getRequestDispatcher("/" + op + ".jsp").forward(request, response);
            } else if (op.equals("aceitarCookies")) {
                sessao.setAttribute("autorizadoExiste", "sim");
                sessao.setAttribute("podeUsarCookies", "sim");

                //Controle de visita de páginas da página 2
                //goncalves2007desenvolvimento, pg 99
                Cookie pg2 = new Cookie("mvCookie-1-visitasPGdois", "0");
                response.addCookie(pg2);

                // usa redirect para, após o clique, 
                // não permanecer na barra de endereços: Geral?op=aceitarCookies
                response.sendRedirect(request.getContextPath() + "/Geral");
                //getServletContext().getRequestDispatcher("/inicial.jsp").forward(request, response);
            } else if (op.equals("rejeitarCookies")) {
                sessao.setAttribute("autorizadoExiste", "sim");
                sessao.setAttribute("podeUsarCookies", "nao");
                response.sendRedirect(request.getContextPath() + "/Geral");
                //getServletContext().getRequestDispatcher("/inicial.jsp").forward(request, response);
            } else {
                out.print("op inválido: " + op);
            }
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
        response.setContentType("text/html;charset=UTF-8");
        try ( PrintWriter out = response.getWriter()) {

            out.println("servlet geral operante");
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

    @Override
    public void init() {

    }
}
