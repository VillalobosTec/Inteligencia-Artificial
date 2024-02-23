package paquete;

public class Arbol {

    private Nodo raiz;

    public Arbol(){

    }
    
    public boolean Encontrado(String string) {
        return Encontrado(this.raiz, string);  
    }

    private boolean Encontrado(Nodo n, String busqueda) {
        if (n == null) {
            return false;
        }
        if (busqueda.equals(n.getDato())) {
            return true;
        } else if (busqueda.compareTo(n.getDato()) < 0) {
            return Encontrado(n.getIzquierda(), busqueda);
        } else {
            return Encontrado(n.getDerecha(), busqueda);
        }
    }

    public void insertar(String dato) {
        if (this.raiz == null) {
            this.raiz = new Nodo(dato);
        } else {
            this.insertar(this.raiz, dato);
        }
    }

    public void Vacio() {
        if (this.raiz ==null) {
            System.out.println("Arbol Vacio");
        } else {
            System.out.println("No esta vacio pa");
        }
    }

    private void insertar(Nodo padre, String dato) {
        if (dato.compareTo(padre.getDato()) <= 0) {
            if (padre.getDerecha() == null) {
                padre.setDerecha(new Nodo(dato));
            } else {
                this.insertar(padre.getDerecha(), dato);
            }
        } else {
            if (padre.getIzquierda() == null) {
                padre.setIzquierda(new Nodo(dato));
            } else {
                this.insertar(padre.getIzquierda(), dato);
            }
        }
    }


    private void inorden(Nodo n) {
        if (n != null) {
            inorden(n.getIzquierda());
            n.imprimirDato();
            inorden(n.getDerecha());
        }
    }

    public void inorder() {
        this.inorden(this.raiz);
    }

}
