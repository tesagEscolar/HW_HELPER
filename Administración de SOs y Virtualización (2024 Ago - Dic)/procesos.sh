bash
#!/bin/bash

# Este script permite al usuario mostrar y eliminar procesos sin necesidad de usar los comandos ps y kill directamente.

# Función para mostrar la lista de procesos
mostrar_procesos() {
  echo "Lista de procesos:"
  ps aux | awk '{print $2 " "$11 " "$10}'
}

# Función para eliminar un proceso
eliminar_proceso() {
  echo "Introduce el PID del proceso a eliminar:"
  read pid
  if [[ -z "$pid" ]]; then
    echo "Debes introducir un PID válido."
    return 1
  fi
  if [[ ! $(ps -p "$pid" > /dev/null 2>&1) ]]; then
    echo "El proceso con PID $pid no existe."
    return 1
  fi
  echo "Estás seguro de que quieres eliminar el proceso con PID $pid? (s/n)"
  read respuesta
  if [[ "$respuesta" == "s" ]]; then
    kill -9 "$pid"
    echo "Proceso eliminado."
  else
    echo "Cancelando la eliminación."
  fi
}

# Menú principal
while true; do
  echo "Opciones:"
  echo "1. Mostrar procesos"
  echo "2. Eliminar proceso"
  echo "3. Salir"
  echo "Elige una opción:"
  read opcion

  case "$opcion" in
    1)
      mostrar_procesos
      ;;
    2)
      eliminar_proceso
      ;;
    3)
      echo "Saliendo..."
      exit 0
      ;;
    *)
      echo "Opción inválida."
      ;;
  esac
done
