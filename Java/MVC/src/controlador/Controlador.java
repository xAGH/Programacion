/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import modelo.Modelo;
import vista.Vista;

/**
 *
 * @author Alejo Giraldo
 */
public class Controlador implements ActionListener{
    
    private final Vista view;
    private final Modelo model;
    
    public Controlador(Vista view, Modelo model)
    {
        this.view = view;
        this.model = model;
        this.view.btnMultiplicar.addActionListener(this);
    }
    
    public void iniciar()
    {
        view.setTitle("MVC Multiplicar");
        view.setLocationRelativeTo(null);
    }
    
    public void actionPerformed(ActionEvent e)
    {
        model.setNumeroUno(Integer.parseInt(view.txtNumero1.getText()));
        model.setNumeroDos(Integer.parseInt(view.txtNumero2.getText()));
        model.multiplicar();
        view.txtResultado.setText(String.valueOf(model.getResultado()));
    }
}
