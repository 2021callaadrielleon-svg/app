from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta_gestor_tareas"  # necesaria para usar session


# ---------------------------------------------------------
# Estas son las MISMAS funciones de la Etapa 1 (lógica pura).
# No las cambiamos: solo dejaron de usar print() para avisar
# lo que hicieron, porque ahora el aviso lo va a mostrar el
# HTML. Reciben la lista de tareas y la devuelven modificada.
# ---------------------------------------------------------

def agregar_tarea(tareas, nombre):
    nueva_tarea = {"nombre": nombre, "completada": False}
    tareas.append(nueva_tarea)
    return tareas


def completar_tarea(tareas, numero):
    if 1 <= numero <= len(tareas):
        tareas[numero - 1]["completada"] = True
    return tareas


def eliminar_tarea(tareas, numero):
    if 1 <= numero <= len(tareas):
        tareas.pop(numero - 1)
    return tareas


# ---------------------------------------------------------
# Rutas Flask: reemplazan al menú con input() de la Etapa 1.
# Cada opción del menú ahora es una ruta distinta.
# ---------------------------------------------------------

@app.route("/")
def index():
    # session guarda la lista de tareas de cada usuario mientras
    # navega la página (reemplaza a la variable "tareas" global
    # que usábamos en el while True de la Etapa 1)
    tareas = session.get("tareas", [])
    return render_template("index.html", tareas=tareas)


@app.route("/agregar", methods=["POST"])
def agregar():
    tareas = session.get("tareas", [])
    nombre = request.form.get("nombre")  # reemplaza al input("Nombre de la tarea: ")
    if nombre:
        tareas = agregar_tarea(tareas, nombre)
    session["tareas"] = tareas
    return redirect(url_for("index"))


@app.route("/completar/<int:numero>")
def completar(numero):
    tareas = session.get("tareas", [])
    tareas = completar_tarea(tareas, numero)
    session["tareas"] = tareas
    return redirect(url_for("index"))


@app.route("/eliminar/<int:numero>")
def eliminar(numero):
    tareas = session.get("tareas", [])
    tareas = eliminar_tarea(tareas, numero)
    session["tareas"] = tareas
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
