package paquete;
import paquete.Nodo;
import paquete.Arbol;
public class arbol_binario {
    public static void main(String[] args) {
        Arbol arbol = new Arbol();
        arbol.insertar("Ola");
        arbol.insertar("ayudame diosito");
        arbol.insertar("ya quedo?");
        arbol.insertar("yo creo que si");
        arbol.inorder();
        arbol.Vacio();
        System.out.println("palabra encontrada o nombre: " + arbol.Encontrado("Ola"));
    }
}