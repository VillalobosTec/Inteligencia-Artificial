package paquete;

public class Nodo {
    private String dato;
    private Nodo izquierda, derecha;

    public Nodo(String dato) {
        this.dato = dato;
        this.izquierda = derecha = null;
    }

    public String getDato() {
        return dato;
    }

    public Nodo getIzquierda() {
        return izquierda;
    }

    public void setIzquierda(Nodo izquierda) {
        this.izquierda = izquierda;
    }

    public Nodo getDerecha() {
        return derecha;
    }

    public void setDerecha(Nodo derecha){
        this.derecha = derecha;
    }
    
    public void imprimirDato() {
       System.out.println(this.getDato()); 
    }
}