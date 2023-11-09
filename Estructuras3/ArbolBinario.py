from NodoAbb import NodoABB


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo, clave, valor):
        if nodo is None:
            return NodoABB(clave, valor)

        if clave < nodo.clave:
            nodo.izquierdo = self._insertar(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar(nodo.derecho, clave, valor)

        return nodo

    def buscar(self, clave):
        return self._buscar(self.raiz, clave)

    def _buscar(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo.valor
        elif clave < nodo.clave:
            return self._buscar(nodo.izquierdo, clave)
        else:
            return self._buscar(nodo.derecho, clave)

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo is not None:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append((nodo.clave, nodo.valor))
            self._inorden(nodo.derecho, resultado)

    def eliminar(self, clave):
        self.raiz = self._eliminar(self.raiz, clave)

    def _eliminar(self, nodo, clave):
        if nodo is None:
            return nodo

        if clave < nodo.clave:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, clave)
        elif clave > nodo.clave:
            nodo.derecho = self._eliminar(nodo.derecho, clave)
        else:
            # Nodo con la clave a eliminar
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            nodo.clave, nodo.valor = self._min_valor(nodo.derecho)
            nodo.derecho = self._eliminar(nodo.derecho, nodo.clave)
        return nodo

    def _min_valor(self, nodo):
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo.clave, nodo.valor

    def valor_maximo(self):
        if self.raiz is None:
            return None
        nodo = self.raiz
        while nodo.derecho is not None:
            nodo = nodo.derecho
        return nodo.valor

    def valor_minimo(self):
        if self.raiz is None:
            return None
        nodo = self.raiz
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo.valor

    def mostrar_arbol(self):
        self._mostrar_arbol(self.raiz, "")

    def _mostrar_arbol(self, nodo, prefijo):
        if nodo is not None:
            print(prefijo + "├─" + str(nodo.clave) + ": " + str(nodo.valor))
            self._mostrar_arbol(nodo.izquierdo, prefijo + "│  ")
            self._mostrar_arbol(nodo.derecho, prefijo + "   ")

    def recorrido_inorder(self):
        resultado = []
        self._recorrido_inorder(self.raiz, resultado)
        return resultado

    def _recorrido_inorder(self, nodo, resultado):
        if nodo is not None:
            self._recorrido_inorder(nodo.izquierdo, resultado)
            resultado.append(nodo.clave)
            self._recorrido_inorder(nodo.derecho, resultado)
