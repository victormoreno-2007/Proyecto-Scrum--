# Proyecto Scrum: Red Social Musical 🎵

## Integrantes del Equipo

- **Scrum Master:** Victor Moreno  
- **Product Owner:** Darío Alejandro Romero  
- **Developers:**  
  - Victor Moreno  
  - Darío Alejandro Romero  
  - Daniel Plazas  
  - Adrian Bayona  

---

## Descripción del Proyecto

Desarrollamos una red social musical en Python con interfaz de consola, enfocada en la gestión de usuarios, recomendaciones de música y creación de playlists. El proyecto cumple con los requisitos del mini-sprint, incluyendo registro de usuarios, interacción con playlists y persistencia de datos en archivos JSON.

### Funcionalidades Clave

- **Gestión de Usuarios:** Registro e inicio de sesión.  
- **Recomendaciones Musicales:** Exploración por géneros y tops globales.  
- **Playlists:** Creación, visualización y gestión de canciones.  
- **Interacción:** Likes y comentarios en playlists.  

---

## Proceso Scrum

### Sesión 1: Planificación (5/7/2025)  
[Reunión de organización](https://cdn.discordapp.com/attachments/1391086022447599638/1391099835284848720/Scrum_1.png)  
- Definición del Product Backlog y asignación de roles.  
- Priorización de historias de usuario:  
  - Épica 1: Gestión de Usuarios (Adrian y Darío).  
  - Épica 2: Publicación de Contenidos (Victor).  
  - Épica 3: Interfaz de Usuario (Daniel).  

---

### Sesión 2: Desarrollo (6/7/2025)  
[Avance inicial](https://cdn.discordapp.com/attachments/1391086022447599638/1391456118152106065/Captura_desde_2025-07-06_11-29-34.png)  
- Implementación del registro y login (`registro.py`, `iniciosesion.py`).  
- Diseño del menú principal (`main.py`).  
- Daily Scrum: Bloqueos resueltos con pair programming.  

---

### Sesión 3: Revisión (7/7/2025)  
[Avance final](https://cdn.discordapp.com/attachments/1391086022447599638/1391982685122990211/image.png)  
- Integración de módulos:  
  - `recomendacion.py`: Búsqueda por géneros.  
  - `gestionCanciones.py`: Likes y comentarios.  
- Sprint Review: Demostración de funcionalidades.  

---

## Estructura del Código

```plaintext
.
├── main.py               # Menú principal
├── registro.py           # Registro de usuarios
├── iniciosesion.py       # Autenticación
├── recomendacion.py      # Recomendaciones musicales
├── gestionCanciones.py   # Gestión de playlists
├── usuarios.json         # Datos de usuarios
└── informacionCantantes.json  # Base de datos musical
```

---

## Cómo Ejecutar el Proyecto

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/victormoreno-2007/Proyecto-Scrum--
   ```
2. Ejecuta el menú principal:  
   ```bash
   python3 main.py
   ```

---

## Retrospectiva

### Logros ✅  
- Cumplimiento del 100% de las historias de usuario priorizadas.  
- Uso efectivo de JSON para persistencia de datos.  

### Mejoras 🔄  
- Implementar pruebas automatizadas.  
- Mejorar manejo de errores en la interfaz.  

---

## Contribuciones Individuales

| Miembro            | Tareas Principales                                                                 |
|--------------------|-----------------------------------------------------------------------------------|
| **Darío**          | Menú principal, submenú de recomendaciones de cantantes.                          |
| **Victor**         | Registro de usuarios, submenú de visualización de playlists.                      |
| **Daniel**         | Submenú de gestión de playlists, menú principal.                                  |
| **Adrian Bayona**  | Submenú de agregar playlists, menú de inicio de sesión.                           |

---

## Presentación Final  
[Discord Nitro](https://cdn.discordapp.com/attachments/1391086022447599638/1391982904661250209/Captura_desde_2025-07-07_22-22-42.png)  
*Nota: Discord requirió actualización a Nitro para videollamadas durante el desarrollo.*  

## Presentacion Diapositivas
[Presentacion](https://www.canva.com/design/DAGsoI2F2PQ/lyXhlOLdBLp3Gf-csVXYeA/edit?utm_content=DAGsoI2F2PQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
--- 

**Repositorio:** [GitHub](https://github.com/victormoreno-2007/Proyecto-Scrum--)  
**Licencia:** MIT.  

--- 
🎶 *"La música es el lenguaje del espíritu"* - Proyecto desarrollado bajo metodología Scrum.
